# Ama Arogya - AI-Driven Public Health Chatbot for Rural Odisha

## Project Overview

Ama Arogya is an AI-powered chatbot designed to bridge the health information gap for rural and semi-urban populations in Odisha. The chatbot provides accurate, accessible, and multilingual health awareness information through WhatsApp and SMS channels.

## Features

- **Multilingual Support**: Responds in Odia, Hindi, and English
- **Symptom Checker**: Guided conversational flow for common symptoms
- **Health Information**: Provides information on maternal care, vaccination, hygiene, and nutrition
- **Emergency Response**: Advises on when to seek immediate medical help
- **Simple Interface**: Easy to use for non-technical users

## Technology Stack

- **NLP Framework**: Rasa Open Source 3.6.21
- **Backend**: FastAPI (Python)
- **Database**: SQLite (for health content storage)
- **Deployment**: Local deployment with ngrok for testing

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.10+ installed
- Git installed

### 1. Clone and Navigate
```bash
git clone https://github.com/SpicychieF05/Odisha_ChatBot.git
cd Odisha_ChatBot
```

### 2. Setup Virtual Environment
```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows Git Bash/WSL
# or on Unix: source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Initialize Database
```bash
python database.py
```

### 5. Train Rasa Model (if needed)
```bash
rasa train
```

### 6. Start the Server
```bash
python -m uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

### 7. Access the Application
- **Demo Frontend**: http://localhost:8001/
- **Alternative Demo**: http://localhost:8001/demo
- **Analytics Dashboard**: http://localhost:8001/dashboard
- **API Documentation**: http://localhost:8001/docs
- **Health Check**: http://localhost:8001/health

### 8. Test the Chatbot

**Option 1: Web Interface**
Open http://localhost:8001/ in your browser and start chatting!

**Option 2: Command Line Test**
```bash
curl -X POST "http://localhost:8001/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello, I have a fever", "sender_id": "test_user", "language": "en"}'
```

**Option 3: Run Test Script**
```bash
python test_chat.py
```

### Sample Queries to Try
- **English**: "Hello, I have a fever and headache"
- **Hindi**: "गर्भावस्था के दौरान क्या सावधानी बरतनी चाहिए?"
- **Odia**: "ନମସ୍କାର, ଟିକା ସମ୍ବନ୍ଧରେ ଜାଣିବାକୁ ଚାହୁଁଛି"
- **Vaccination**: "Tell me about vaccination schedule"
- **Maternal Care**: "pregnancy care advice"

### Stop the Server
Press `Ctrl+C` in the terminal where the server is running.

## API Endpoints

- `GET /`: Demo frontend interface
- `GET /demo`: Alternative demo route  
- `GET /health`: Health check
- `GET /dashboard`: Analytics dashboard
- `GET /docs`: API documentation
- `POST /chat`: Send message to chatbot

### Chat Request Format
```json
{
  "message": "Hello",
  "sender_id": "user123", 
  "language": "en"
}
```

### Chat Response Format
```json
{
  "response": "Hello! How can I help you?",
  "language": "en",
  "intent": "greet"
}
```

---

## Project Details

- Project: **Odisha Health Chatbot**
- Brief introduction: An AI-driven WhatsApp chatbot providing timely, localised public health information and referrals to users in Odisha. The bot supports English, Hindi, and Odia and is optimized for low-bandwidth, text-first interactions.
- Problem it solves: Reduces barriers to basic healthcare information for rural users who may lack easy access to clinics, trained personnel, or reliable information sources. It offers symptom guidance, vaccination schedules, maternal care tips, outbreak alerts, and links to local resources.
- Target users: Rural and semi-urban residents of Odisha, community health workers (ASHA, ANM), NGOs, and local health administrators.

## Features

- Multilingual support (Odia, Hindi, English)
- Symptom checker and triage guidance
- Vaccination schedules and reminders
- Maternal and neonatal health guidance
- Infectious-disease outbreak alerts and basic preventive measures
- Local facility lookup and referral suggestions (based on configurable DB)
- FAQ and health tips library
- Analytics dashboard (basic usage stats)
- WhatsApp integration via Twilio (primary channel) with optional SMS fallback

## Technologies Used

- Python 3.8+ (recommended 3.10)
- Rasa Open Source (NLU + Core)
- Flask (webhook / API)
- SQLite (simple file-based datastore)
- SQLAlchemy (ORM)
- Twilio API (WhatsApp messaging)
- Ngrok (for local webhook testing)
- Uvicorn / Gunicorn (production ASGI/WGI server options)
- Frontend: minimal HTML/JS for dashboard (served from Flask)
- Testing: pytest (basic tests provided)

## Architecture Overview

High-level flow:

1. User sends a message from WhatsApp to the project's Twilio number.
2. Twilio forwards the message to the configured Flask webhook endpoint.
3. Flask receives the webhook, extracts message and metadata, and forwards the text to Rasa's REST webhook (or directly runs Rasa NLU pipeline locally).
4. Rasa processes the message, identifies intent/entities, and returns the best response or action.
5. Flask records the interaction in SQLite and sends the chosen response back to the user via Twilio's API.

Components:
- WhatsApp (User) → Twilio (Messaging webhook) → Flask (webhook & application logic) → Rasa (NLU & dialogue manager) → SQLite (content & logs) → Twilio (response delivery)

## Setup & Installation

Below are step-by-step instructions to run the project locally. These steps assume you are on Windows with Bash (WSL or Git Bash) or a Unix-like shell.

1. Clone the repository

```bash
git clone https://github.com/SpicychieF05/Odisha_ChatBot.git
cd Odisha_ChatBot
```

2. Create and activate a Python virtual environment

```bash
python -m venv .venv
source .venv/Scripts/activate    # Windows (Git Bash/WSL)
# or on Unix: source .venv/bin/activate
```

3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. Initialize the database (sample data)

```bash
python database.py
```

5. Train the Rasa model

```bash
# If you installed Rasa inside the virtualenv
rasa train
```

6. Start the Flask app (local development)

```bash
export FLASK_APP=main.py         # On Windows PowerShell: $env:FLASK_APP="main.py"
flask run --host=0.0.0.0 --port=5000
```

7. Expose local webhook with Ngrok (for Twilio testing)

```bash
ngrok http 5000
```

Copy the `https://...ngrok.io` forwarding URL and paste it into Twilio's webhook configuration for incoming messages.

Notes:
- If you use `uvicorn` (ASGI) or deploy in production, prefer `uvicorn main:app --host 0.0.0.0 --port 8000` or Gunicorn with an ASGI worker.
- Rasa can run as a separate server (`rasa run` and `rasa run actions`) or be called via the Python API — the repo has wiring for either option.

## Configuration

Copy `.env.example` (if present) to `.env` and add your Twilio credentials and other settings. Example `.env` contents:

```env
# Twilio
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+1415xxxxxxx

# App
FLASK_ENV=development
SECRET_KEY=replace-with-a-secret
DATABASE_URL=sqlite:///health_chatbot.db

# Rasa
RASA_SERVER_URL=http://localhost:5005
```

Make sure the Twilio number is a WhatsApp-enabled sender (configured via Twilio console) and that the webhook URL matches the Ngrok or deployed URL.

## Usage Instructions

Example request/response flows you can try from WhatsApp (or via Twilio Test Console):

- Greeting

```
User: Hi
Bot: Hello! I'm Odisha Health Assistant. How can I help you today? (Supports Odia/Hindi/English)
```

- Symptom check

```
User: I have fever and chills
Bot: Based on your symptoms you might have a viral infection. If your temperature is above 38°C or you experience severe symptoms, please visit the nearest health centre. Would you like nearby facility information?
```

- Vaccination schedule

```
User: When should my child get the next vaccine?
Bot: The recommended schedule is: BCG at birth, OPV at 6,10,14 weeks, DPT at 6,10,14 weeks, Measles at 9 months. Do you want the nearest immunization centre?
```

Responses include language detection where possible. If language is not detected, the bot will default to English.

## Admin Panel (Optional)

If an admin panel is included, it will usually be accessible at `/admin` or via a small React/Flask template. Use the credentials in the `.env` or a seeded admin account to log in. The panel allows:

- Viewing and searching user interactions
- Editing knowledge base entries
- Broadcasting alerts (requires Twilio Notify or separate script)

If you do not have an admin UI bundled, consider using `sqlitebrowser` or `DB Browser for SQLite` to inspect `health_chatbot.db`.

## Development Notes / Roadmap

Suggested next steps and improvements:

- Add conversational fallback and escalation to human operator
- Implement appointment booking integration with local PHCs
- Add SMS fallback using Twilio SMS for users without WhatsApp
- Improve NLU by adding more Odia/Hindi training examples and domain-specific synonyms
- Add automated tests for Rasa stories and Flask endpoints
- Containerize the app with Docker and provide a `docker-compose` for quick deploy
- Implement role-based admin panel and secure webhooks with HMAC verification

## Contributing Guidelines

We welcome contributions. To contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make changes and add tests where applicable
4. Run tests and ensure the project builds
5. Submit a pull request describing your changes

For issues, please open an issue in the GitHub repo with steps to reproduce and expected behavior.

Code style:
- Follow PEP8 for Python code
- Keep Rasa training data tidy and include language tags when adding multilingual examples

## License

This project is licensed under the MIT License — see the `LICENSE` file for details.

## Optional: API Endpoints

- `POST /webhook/twilio` — Twilio incoming WhatsApp webhook (receives messages)
- `POST /chat` — Internal chat endpoint (for programmatic testing)
- `GET /dashboard` — Simple analytics dashboard
- `GET /health` — Health check endpoint for load balancers

Example: Sending a programmatic chat request

```bash
curl -X POST http://localhost:5000/chat \
   -H "Content-Type: application/json" \
   -d '{"message":"I have a fever","sender_id":"user123","language":"en"}'
```

## Optional: Database Schema

- `HealthContent` table: id, topic, language, content, updated_at
- `UserInteraction` table: id, sender_id, message, response, intent, language, timestamp

Inspect `database.py` for the concrete SQLAlchemy models and sample data loader.

## Known Issues

- Rasa model files and `.rasa` cache can be large — they are ignored by `.gitignore` and should be trained locally.
- Some Odia/Hindi phrases may require additional training data for reliable intent recognition.

## References

- Rasa documentation: https://rasa.com/docs/
- Twilio WhatsApp: https://www.twilio.com/whatsapp
- Ngrok: https://ngrok.com/docs

---

If you'd like, I can also:
- Add a `.env.example` to the repo
- Create a `Dockerfile` and `docker-compose.yml` for local dev
- Add a short troubleshooting section for common issues (Rasa training, Twilio webhook errors)

---

Project maintained by the Odisha Health Chatbot contributors.
3. Run: `ngrok http 8000`
4. Use the generated HTTPS URL for external access

### WhatsApp Integration (Future)

To integrate with WhatsApp Business API:

1. Set up a Meta for Developers account
2. Create a WhatsApp Business app
3. Configure webhooks to point to your deployed API
4. Implement WhatsApp message handling in the `/chat` endpoint

## Contributing

This is an MVP for a hackathon project. Contributions and improvements are welcome!

## License

This project is developed for educational and humanitarian purposes.