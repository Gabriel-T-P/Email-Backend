import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestClassifierText:

    def test_classify_text_productive(self):
        response = client.post("/api/v1/text", json={"text": "Preciso de atualização do meu pedido"})
        assert response.status_code == 200
        data = response.json()

        assert data["success"] is True
        assert "data" in data
        assert "classification" in data["data"]
        assert data["data"]["classification"]["category"] in ["produtivo", "improdutivo"]
        assert isinstance(data["data"]["classification"]["confidence"], float)
        assert "response" in data["data"]
        assert "analysis" in data["data"]
        assert isinstance(data["data"]["analysis"]["wordCount"], int)

    def test_classify_text_unproductive(self):
        response = client.post("/api/v1/text", json={"text": "Feliz Natal a todos!"})
        assert response.status_code == 200
        data = response.json()

        assert data["success"] is True
        assert data["data"]["classification"]["category"] == "improdutivo"
        assert "Obrigado" in data["data"]["response"]

    def test_classify_text_special_chars(self):
        response = client.post("/api/v1/text", json={"text": "@cliente #pedido 123!!!"})
        assert response.status_code == 200
        data = response.json()

        assert data["success"] is True
        assert "classification" in data["data"]
        assert "analysis" in data["data"]

    def test_classify_text_missing_field(self):
        response = client.post("/api/v1/text", json={})
        assert response.status_code == 422  # erro de validação Pydantic
