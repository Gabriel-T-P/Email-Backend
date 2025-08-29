from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.nlp_service import process_file
from app.services.classifier_service import classify_email

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
    Endpoint que recebe arquivos `.txt` ou `.pdf` e aplica NLP.
    """
    if not file.filename.endswith((".txt", ".pdf")):
        raise HTTPException(status_code=400, detail="Formato de arquivo não suportado")

    file_bytes = await file.read()

    processed_text = process_file(file_bytes, file.filename)

    result = classify_email(processed_text)

    return {
        "category": result["category"],
        "response": result["response"],
        "content": processed_text
    }
