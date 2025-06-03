from flask import Flask, request, jsonify
import requests, html, random, json

app = Flask(__name__)

# In-memory session state
session_memory = {}

@app.route('/', methods=['POST'])
def webhook():
    req = request.get_json(silent=True)
    print("Dialogflow Request:", json.dumps(req, indent=2))

    session_id = req.get('session')
    qr = req.get('queryResult', {})
    intent_name = qr.get('intent', {}).get('displayName', '')
    user_message = qr.get('queryText', '').strip().lower()

    # Initialize session state
    session = session_memory.get(session_id, {"step": 0})

    # STEP 2: Yes/No answer confirmation
    if session["step"] == 2:
        if user_message in ["yes", "y", "yeah", "sure"]:
            return reveal_or_skip_answer(session_id, True)
        if user_message in ["no", "n", "nope"]:
            return reveal_or_skip_answer(session_id, False)
        return jsonify({'fulfillmentText': "Please reply with 'Yes' or 'No'."})

    # STEP 1: User answered A/B/C/D
    if session["step"] == 1 and user_message in ["a", "b", "c", "d"]:
        return evaluate_answer(session_id, user_message)

    # Get new question
    if intent_name == "Get_Tech_Question":
        return ask_question(session_id)

    # Default fallback
    return jsonify({
        'fulfillmentText': "Send 'Give me a question' to get started!"
    })


def ask_question(session_id):
    try:
        resp = requests.get("https://opentdb.com/api.php?amount=1&category=18&type=multiple").json()
        if resp.get("response_code") or not resp.get("results"):
            raise ValueError("No question available")

        q = resp["results"][0]
        question = html.unescape(q["question"])
        correct = html.unescape(q["correct_answer"])
        options = [html.unescape(o) for o in q["incorrect_answers"]] + [correct]
        random.shuffle(options)

        # Save step, correct answer, and shuffled options
        session_memory[session_id] = {
            "step": 1,
            "correct_answer": correct,
            "options": options
        }

        formatted = "\n".join(f"{chr(65+i)}. {opt}" for i, opt in enumerate(options))
        text = f"🧠 *Tech Question:*\n{question}\n\n{formatted}\n\nReply with A, B, C, or D."
        return jsonify({'fulfillmentText': text})

    except Exception as e:
        print("ask_question error:", e)
        return jsonify({'fulfillmentText': "Sorry, couldn't fetch a question. Try again later."})


def evaluate_answer(session_id, user_choice_letter):
    state = session_memory.get(session_id, {})
    correct = state.get("correct_answer", "")
    options = state.get("options", [])
    step = state.get("step", 0)

    if not correct or step != 1:
        return jsonify({'fulfillmentText': "Please ask for a new question to begin."})

    index = ord(user_choice_letter.upper()) - 65

    if index < 0 or index >= len(options):
        return jsonify({'fulfillmentText': "Invalid option. Please reply with A, B, C, or D."})

    selected = options[index]
    if selected == correct:
        session_memory.pop(session_id, None)  # Clear session
        return jsonify({'fulfillmentText': "✅ Correct! Well done!"})
    else:
        state["step"] = 2
        session_memory[session_id] = state
        return jsonify({'fulfillmentText': "❌ That's not correct. Do you want the answer? (Yes/No)"})


def reveal_or_skip_answer(session_id, reveal: bool):
    state = session_memory.get(session_id, {})
    answer = state.get("correct_answer", "N/A")
    session_memory.pop(session_id, None)  # Clear session after response
    if reveal:
        return jsonify({'fulfillmentText': f"✅ The correct answer is: {answer}"})
    else:
        return jsonify({'fulfillmentText': "👍 Alright! If you'd like another question, just ask."})


if __name__ == "__main__":
    app.run(debug=True)
