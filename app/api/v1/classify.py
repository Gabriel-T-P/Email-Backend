from fastapi import APIRouter
from app.models.email import EmailRequest
from app.models.response import ClassifyResponse
from app.services.classifier_service import classify_email
from app.services.nlp_service import preprocess_text

router = APIRouter()

@router.post(
    "/text",
    response_model=ClassifyResponse,
    summary="Classificar email a partir de texto puro",
    description="""
Recebe o conteúdo de um email como **texto simples** e retorna:

- A categoria atribuída (**Produtivo** ou **Improdutivo**)
- Nível de confiança da resposta entre e 0 e 1
- Tempo de processamento em ms
- Contagem de palavras
- Booleano para sucesso ou falha
- Erro (opcional)
- Uma resposta automática sugerida
    """,
)
async def classify_text(email: EmailRequest):
    """
    Endpoint que recebe texto puro de email, pré-processa e classifica.
    """
    processed_text = preprocess_text(email.text)
    
    result = classify_email(processed_text)

    return result
