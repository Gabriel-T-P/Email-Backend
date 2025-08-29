from fastapi import APIRouter
from pydantic import BaseModel

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
    Endpoint que recebe texto puro de email.
    """
    return {
        "category": "Produtivo",
        "response": "Olá, recebemos sua solicitação e estamos verificando.",
    }
