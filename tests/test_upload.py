import io
import pytest
from fastapi.testclient import TestClient
from app.main import app
from tests.utils import make_pdf_bytes, make_txt_bytes

client = TestClient(app)

@pytest.mark.parametrize(
    "filename, file_bytes, expected_category, content_type",
    [
        ("email.txt", make_txt_bytes("Preciso de atualização do meu pedido"), "Produtivo", "text/plain"),
        ("email.txt", make_txt_bytes("Feliz Natal a todos!"), "Improdutivo", "text/plain"),
        ("email.pdf", make_pdf_bytes("Problema com meu pedido"), "Produtivo", "application/pdf"),
        ("email.pdf", make_pdf_bytes("Obrigado pelo suporte"), "Improdutivo", "application/pdf"),
    ]
)
def test_classify_file_valid(filename, file_bytes, expected_category, content_type):
    """
    Testa arquivos válidos (.txt e .pdf) e verifica categoria, resposta e conteúdo.
    """
    response = client.post(
        "/api/v1/file",
        files={"file": (filename, io.BytesIO(file_bytes), content_type)},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["category"] == expected_category
    assert "response" in data
    assert "content" in data
    assert isinstance(data["content"], str)
    assert len(data["content"]) > 0

@pytest.mark.parametrize(
    "filename, file_bytes, content_type",
    [
        ("foto.jpg", b"Sou uma imagem, nao um email", "image/jpeg"),
        ("documento.docx", b"Conteudo qualquer", "application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    ]
)
def test_classify_file_invalid_format(filename, file_bytes, content_type):
    """
    Testa arquivos com formatos não suportados.
    """
    response = client.post(
        "/api/v1/file",
        files={"file": (filename, io.BytesIO(file_bytes), content_type)},
    )
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "Formato de arquivo não suportado"
