from fastapi import APIRouter
from app.models.schemas import EmailRequest, EmailResponse
from app.services.classifier_service import classify_email

router = APIRouter()


@router.post("/", response_model=EmailResponse)
def classify_email_endpoint(email: EmailRequest):
    """
    Recebe um texto de email e retorna categoria + resposta sugerida.
    """
    return classify_email(email.text)
