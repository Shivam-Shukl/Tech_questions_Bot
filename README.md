# 🤖 Tech Questions Bot

A Telegram-integrated chatbot that asks random technical multiple-choice questions using Dialogflow + Flask + Open Trivia DB. This bot engages users with MCQs and provides answers upon request.

---

## 📸 Screenshots

### Interview_questions
The telegram bot name at telgram.

<img src="https://github.com/user-attachments/assets/8c9a192b-5ad8-4be8-897d-7b4f2d44355e" width ="1000"/>

<img src="https://github.com/user-attachments/assets/541f1443-60e3-4bd4-a2b0-415d1ce5b49f" width="1000"/>

---

## 📺 Demo Video

[![Watch the demo](https://img.youtube.com/vi/H7RFMYL9KSk/0.jpg)](https://youtu.be/H7RFMYL9KSk)

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

### 1 Clone the Repository
```bash
git clone https://github.com/yourusername/Tech_questions_Bot.git
cd Tech_questions_Bot
```
### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create `main.py` with this code

```bash
python app.py
```

---
Visit: http://localhost:5000
### 4. Deploy on Render

#### Option A: Manual Deploy

- Login to Render
- Click "New Web Service" → Connect to this repo
- Use:
   - Build Command: pip install -r requirements.txt
   - Start Command: python app.py

#### Option B: Auto Deploy using render.yaml

- Make sure your repo includes the following:

```yaml
# render.yaml
services:
  - type: web
    name: tech-question-bot
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python app.py
    envVars:
      - key: FLASK_ENV
        value: production

```

---

### 5. Webhook Integration
- Go to Dialogflow Console
- Enable Webhook Fulfillment
- Use your Render-deployed HTTPS URL (e.g. https://your-app.onrender.com/)
- Attach this webhook to your Get_Tech_Question intent
---

### 6.Sample Commands (Telegram)
```text
/start
get me a question
A
Yes
```
---
### 📁 Project Structure

```bash
Tech_questions_Bot/
├── app.py               # Main Flask app with webhook logic
├── requirements.txt     # Dependencies
├── render.yaml          # (Optional) Render deploy config
└── Screenshot*.png      # Bot demo screenshot

```
---
### 🧑‍💻 Author

- #### Shivam Shukla
- Feel free to connect with me on 💼 [LinkedIn](https://www.linkedin.com/in/shivam-shukla-a462b3223/) 


---

