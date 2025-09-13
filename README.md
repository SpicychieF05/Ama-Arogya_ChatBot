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

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate  # On Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Training the Model

1. Initialize Rasa project:
   ```bash
   rasa init --no-prompt
   ```
2. Train the model:
   ```bash
   rasa train
   ```

## Running the Chatbot

1. Start the FastAPI backend:
   ```bash
   uvicorn main:app --reload
   ```
2. Test the API at `http://localhost:8000`

## API Endpoints

- `GET /`: Root endpoint
- `GET /health`: Health check
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

## Project Structure

```
├── actions/              # Custom actions
├── data/                 # Training data (NLU, stories, rules)
├── models/               # Trained models
├── main.py               # FastAPI backend
├── domain.yml            # Domain configuration
├── config.yml            # Rasa configuration
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Deployment

### Local Deployment

1. Start the FastAPI server:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

2. Access the API at `http://localhost:8000`
3. View the dashboard at `http://localhost:8000/dashboard`

### Public Deployment with ngrok

1. Install ngrok: `winget install Ngrok.Ngrok`
2. Start your local server
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