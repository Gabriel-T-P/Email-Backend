import io
import pytest
from fastapi.testclient import TestClient
from app.main import app
from tests.utils import make_pdf_bytes  # helper de PDF

client = TestClient(app)

@pytest.mark.parametrize(
    "filename, content, expected_category, content_type",
    [
        ("email.txt", b"Preciso de atualizacao do meu pedido", "Produtivo", "text/plain"),
        ("email.txt", b"Feliz Natal a todos", "Improdutivo", "text/plain"),
        ("email.pdf", make_pdf_bytes("Problema com meu pedido"), "Produtivo", "application/pdf"),
        ("email.pdf", make_pdf_bytes("Obrigado pelo suporte"), "Produtivo", "application/pdf"),
    ]
)
def test_classify_file_valid(filename, content, expected_category, content_type):
    # Prepara o arquivo para envio
    if filename.endswith(".pdf") and isinstance(content, bytes):
        file_content = io.BytesIO(content)
    else:
        file_content = io.BytesIO(content)

    response = client.post(
        "/api/v1/file",
        files={"file": (filename, file_content, content_type)},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["category"] == expected_category
    assert "response" in data
    assert "content" in data
    assert isinstance(data["content"], str)
    assert len(data["content"]) > 0

def test_classify_file_invalid_format():
    file_content = b"Sou uma imagem, nao um email"
    response = client.post(
        "/api/v1/file",
        files={"file": ("foto.jpg", io.BytesIO(file_content), "image/jpeg")},
    )
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "Formato de arquivo não suportado"
