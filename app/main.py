from fastapi import FastAPI
from app.api.v1 import classify

app = FastAPI(
    title="Email Classifier API",
    version="1.0.0",
    description="API para classificar emails e sugerir respostas automáticas."
)

# Inclui rotas da API
app.include_router(classifier_router, prefix="/api/v1")
app.include_router(upload_router, prefix="/api/v1")
