import io
import pytest
from fastapi.testclient import TestClient
from app.main import app
from tests.utils import make_pdf_bytes  # helper de PDF

client = TestClient(app)

def test_classify_file_txt():
    file_content = b"Este eh um email de teste em TXT."
    response = client.post(
        "/api/v1/file",
        files={"file": ("email.txt", io.BytesIO(file_content), "text/plain")},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["category"] == "Improdutivo"
    assert "response" in data
    assert "content" in data

def test_classify_file_pdf():
    pdf_bytes = make_pdf_bytes("Conteúdo de teste em PDF")
    response = client.post(
        "/api/v1/file",
        files={"file": ("email.pdf", io.BytesIO(pdf_bytes), "application/pdf")},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["category"] == "Improdutivo"
    assert "response" in data
    assert "content" in data

def test_classify_file_invalid_format():
    file_content = b"Sou uma imagem, nao um email"
    response = client.post(
        "/api/v1/file",
        files={"file": ("foto.jpg", io.BytesIO(file_content), "image/jpeg")},
    )
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "Formato de arquivo não suportado"
