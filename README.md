# 🤖 Tech Questions Bot

A Telegram-integrated chatbot that asks random technical multiple-choice questions using Dialogflow + Flask + Open Trivia DB. This bot engages users with MCQs and provides answers upon request.

---

## 📸 Demo Screenshot

![Tech Questions Bot Demo](Screenshot%202025-06-03%20111603.png)

---

## 🧠 Features

- Fetches tech-based MCQs (CS category) via [Open Trivia DB](https://opentdb.com/)
- Randomized options (A/B/C/D format)
- Understands answer choices (A/B/C/D) and tells if correct
- Asks "Do you want the answer?" if the user gets it wrong
- Deployable via [Render](https://render.com/) as a public webhook for Dialogflow

---

## 🛠 Tech Stack

| Component      | Technology       |
|----------------|------------------|
| Bot Platform   | Telegram (via Dialogflow integration) |
| Backend        | Python + Flask   |
| Webhook Server | Render           |
| Data Source    | [Open Trivia DB](https://opentdb.com/api_config.php) |
| Bot Logic      | Dialogflow CX/ES |

---

## 🚀 Setup & Deployment

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/Tech_questions_Bot.git
cd Tech_questions_Bot
