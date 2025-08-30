from fastapi import APIRouter, UploadFile, File
from app.services.classifier_service import classify_email
from app.services.nlp_service import process_file
from app.models.response import ClassifyResponse

router = APIRouter()

@router.post(
    "/file",
    response_model=ClassifyResponse,
    summary="Classificar email a partir de arquivo (.txt ou .pdf)",
    description="""
Recebe um arquivo `.txt` ou `.pdf`, extrai o conteúdo e retorna:

- A categoria atribuída (**Produtivo** ou **Improdutivo**)
- Nível de confiança da resposta entre e 0 e 1
- Tempo de processamento em ms
- Contagem de palavras
- Booleano para sucesso ou falha
- Erro (opcional)
- Uma resposta automática sugerida
    """,
)
async def classify_file(file: UploadFile = File(...)):
    """
    Endpoint que recebe arquivos `.txt` ou `.pdf` e aplica NLP.
    """
    if not file.filename.endswith((".txt", ".pdf")):
        return ClassifyResponse(success=False, error="Formato de arquivo não suportado")

    file_bytes = await file.read()
    processed_text = process_file(file_bytes, file.filename)

    return classify_email(processed_text)