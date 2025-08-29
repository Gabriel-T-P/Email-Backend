from fastapi import APIRouter
from pydantic import BaseModel
from app.services.nlp_service import preprocess_text
from app.services.classifier_service import classify_email

router = APIRouter()


class EmailInput(BaseModel):
    content: str


@router.post(
    "/text",
    summary="Classificar email a partir de texto puro",
    description="""
Recebe o conteúdo de um email como **texto simples** e retorna:

- A categoria atribuída (**Produtivo** ou **Improdutivo**)
- Uma resposta automática sugerida
    """,
)
async def classify_text(email: EmailInput):
    """
    Endpoint que recebe texto puro de email, pré-processa e classifica.
    """
    processed_text = preprocess_text(email.content)

    result = classify_email(processed_text)

    return result
