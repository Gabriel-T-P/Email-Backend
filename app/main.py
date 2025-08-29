from fastapi import FastAPI
from app.api.v1.endpoints import classify

app = FastAPI(
    title="Email Classifier API",
    version="1.0.0",
    description="API para classificar emails e sugerir respostas automáticas."
)

# Inclui rotas da API
app.include_router(classify.router, prefix="/api/v1/classify", tags=["classify"])
