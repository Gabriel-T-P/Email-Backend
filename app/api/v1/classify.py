from fastapi import APIRouter, UploadFile, File, HTTPException
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
    responses={
        200: {
            "description": "Classificação realizada com sucesso",
            "content": {
                "application/json": {
                    "example": {
                        "category": "Produtivo",
                        "response": "Olá, recebemos sua solicitação e estamos verificando.",
                    }
                }
            },
        },
        400: {"description": "Erro de validação no input"},
    },
)
async def classify_text(email: EmailInput):
    """
    Endpoint que recebe texto puro de email.
    """
    return {
        "category": "Produtivo",
        "response": "Olá, recebemos sua solicitação e estamos verificando.",
    }


@router.post(
    "/file",
    summary="Classificar email a partir de arquivo (.txt ou .pdf)",
    description="""
Recebe um arquivo `.txt` ou `.pdf`, extrai o conteúdo e retorna:

- A categoria atribuída (**Produtivo** ou **Improdutivo**)
- Uma resposta automática sugerida
- Prévia do conteúdo extraído do arquivo
    """,
    responses={
        200: {
            "description": "Classificação realizada com sucesso",
            "content": {
                "application/json": {
                    "example": {
                        "category": "Improdutivo",
                        "response": "Obrigado pela mensagem!",
                        "content": "Feliz Natal e um próspero Ano Novo!",
                    }
                }
            },
        },
        400: {"description": "Arquivo inválido ou não suportado"},
    },
)
async def classify_file(file: UploadFile = File(...)):
    """
    Endpoint que recebe arquivos `.txt` ou `.pdf`.
    Ainda não implementa o processamento de NLP.
    """
    if not file.filename.endswith((".txt", ".pdf")):
        raise HTTPException(status_code=400, detail="Formato de arquivo não suportado")

    # Simulação do conteúdo extraído
    dummy_content = "Feliz Natal e um próspero Ano Novo!"

    return {
        "category": "Improdutivo",
        "response": "Obrigado pela mensagem!",
        "content": dummy_content,
    }
