from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import func
from database import SessionLocal, HealthContent, UserInteraction, get_db
from typing import Optional

app = FastAPI(title="Ama Arogya - Public Health Chatbot API", version="1.0.0")


class ChatRequest(BaseModel):
    message: str
    sender_id: str
    language: Optional[str] = "en"


class ChatResponse(BaseModel):
    response: str
    language: str
    intent: Optional[str] = None


def get_health_content(topic: str, language: str, db: Session):
    """Get health content from database"""
    content = db.query(HealthContent).filter(
        HealthContent.topic == topic,
        HealthContent.language == language
    ).first()
    return content


def log_interaction(sender_id: str, message: str, response: str, intent: str, language: str, db: Session):
    """Log user interaction"""
    interaction = UserInteraction(
        sender_id=sender_id,
        message=message,
        response=response,
        intent=intent,
        language=language
    )
    db.add(interaction)
    db.commit()


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest, db: Session = Depends(get_db)):
    """
    Handle chatbot messages
    """
    message = request.message.lower()
    language = request.language
    intent = "general"
    response = ""

    # Check for specific topics and get content from database
    if any(word in message for word in ["vaccination", "टीका", "ଟୀକା"]):
        content = get_health_content("vaccination", language, db)
        if content:
            response = content.content
            intent = "vaccination"
        else:
            # Fallback responses
            if language == "hi":
                response = "टीकाकरण बच्चों के स्वास्थ्य के लिए महत्वपूर्ण है। नियमित टीकाकरण कार्यक्रम का पालन करें।"
            elif language == "or":
                response = "ଟୀକାକରଣ ପିଲାମାନଙ୍କ ସ୍ୱାସ୍ଥ୍ୟ ପାଇଁ ଗୁରୁତ୍ୱପୂର୍ଣ୍ଣ। ନିୟମିତ ଟୀକାକରଣ କାର୍ଯ୍ୟକ୍ରମର ଅନୁସରଣ କରନ୍ତୁ।"
            else:
                response = "Vaccination is important for children's health. Follow the regular vaccination schedule."
            intent = "vaccination"

    elif any(word in message for word in ["pregnancy", "maternal", "गर्भावस्था", "ଗର୍ଭାବସ୍ଥା"]):
        content = get_health_content("maternal_care", language, db)
        if content:
            response = content.content
            intent = "maternal_care"
        else:
            # Fallback responses
            if language == "hi":
                response = "गर्भावस्था के दौरान नियमित जांच और संतुलित आहार महत्वपूर्ण है।"
            elif language == "or":
                response = "ଗର୍ଭାବସ୍ଥା ସମୟରେ ନିୟମିତ ଯାଞ୍ଚ ଏବଂ ସନ୍ତୁଲିତ ଆହାର ଗୁରୁତ୍ୱପୂର୍ଣ୍ଣ।"
            else:
                response = "During pregnancy, regular check-ups and balanced diet are important."
            intent = "maternal_care"

    elif any(word in message for word in ["fever", "ज्वर", "ଜ୍ବର"]):
        if language == "hi":
            response = "बुखार के लिए पर्याप्त आराम लें और हाइड्रेटेड रहें। यदि बुखार 3 दिनों से अधिक समय तक बना रहता है तो डॉक्टर से संपर्क करें।"
        elif language == "or":
            response = "ଜ୍ବର ପାଇଁ ଯଥେଷ୍ଟ ବିଶ୍ରାମ ନିଅନ୍ତୁ ଏବଂ ପାଣି ପିଅନ୍ତୁ। ଯଦି ଜ୍ବର 3 ଦିନରୁ ଅଧିକ ସମୟ ପାଇଁ ରହିଥାଏ ତେବେ ଡାକ୍ତରଙ୍କ ସହିତ ଯୋଗାଯୋଗ କରନ୍ତୁ।"
        else:
            response = "For fever, take adequate rest and stay hydrated. If fever persists for more than 3 days, consult a doctor."
        intent = "symptom_report"

    elif any(word in message for word in ["hello", "hi", "namaste", "ନମସ୍କାର"]):
        if language == "hi":
            response = "नमस्ते! मैं आपकी मदद कैसे कर सकता हूँ?"
        elif language == "or":
            response = "ନମସ୍କାର! ମୁଁ ଆପଣଙ୍କୁ କିପରି ସାହାଯ୍ୟ କରିପାରେ?"
        else:
            response = "Hello! How can I help you?"
        intent = "greet"

    else:
        if language == "hi":
            response = "मैं आपकी मदद करने के लिए यहाँ हूँ। कृपया अधिक जानकारी दें।"
        elif language == "or":
            response = "ମୁଁ ଆପଣଙ୍କୁ ସାହାଯ୍ୟ କରିବା ପାଇଁ ଏଠାରେ ଅଛି। ଦୟାକରି ଅଧିକ ସୂଚନା ଦିଅନ୍ତୁ।"
        else:
            response = "I'm here to help you. Please provide more information."

    # Log the interaction
    log_interaction(request.sender_id, request.message,
                    response, intent, language, db)

    return ChatResponse(
        response=response,
        language=language,
        intent=intent
    )


@app.get("/")
async def root():
    """
    Root endpoint
    """
    return {"message": "Ama Arogya - Public Health Chatbot API", "status": "running"}


@app.get("/health")
async def health():
    """
    Health check endpoint
    """
    return {"status": "healthy"}


@app.get("/stats")
async def get_stats(db: Session = Depends(get_db)):
    """
    Get basic statistics
    """
    total_interactions = db.query(UserInteraction).count()
    language_stats = db.query(UserInteraction.language, func.count(
        UserInteraction.id)).group_by(UserInteraction.language).all()

    return {
        "total_interactions": total_interactions,
        "language_distribution": dict(language_stats)
    }


@app.get("/dashboard", response_class=HTMLResponse)
async def get_dashboard():
    """
    Serve the analytics dashboard
    """
    with open("dashboard.html", "r", encoding="utf-8") as f:
        return f.read()
