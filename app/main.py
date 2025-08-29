from fastapi import FastAPI
from app.api.v1.classify import router as classify_router
from app.api.v1.upload import router as upload_router

app = FastAPI(
    title="Email Classifier API",
    version="1.0.0",
    description="API para classificar emails e sugerir respostas automáticas."
)

# Inclui rotas da API
app.include_router(classify_router, prefix="/api/v1")
app.include_router(upload_router, prefix="/api/v1")
