from fastapi import APIRouter, UploadFile, File, HTTPException

router = APIRouter()

@router.post(
    "/file",
    summary="Classificar email a partir de arquivo (.txt ou .pdf)",
    description="""
Recebe um arquivo `.txt` ou `.pdf`, extrai o conteúdo e retorna:

- A categoria atribuída (**Produtivo** ou **Improdutivo**)
- Uma resposta automática sugerida
- Prévia do conteúdo extraído do arquivo
    """,
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
