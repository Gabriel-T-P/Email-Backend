import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Melhorar testes quando classificador estiver pronto 

class TestClassifierText:

    def test_classify_text_productive(self):
        response = client.post("/api/v1/text", json={"content": "Preciso de atualização do meu pedido"})
        assert response.status_code == 200
        data = response.json()
        assert "category" in data
        assert "response" in data

    def test_classify_text_unproductive(self):
        response = client.post("/api/v1/text", json={"content": "Feliz Natal a todos!"})
        assert response.status_code == 200
        data = response.json()
        assert "category" in data
        assert "response" in data

    def test_classify_text_special_chars(self):
        response = client.post("/api/v1/text", json={"content": "@cliente #pedido 123!!!"})
        assert response.status_code == 200
        data = response.json()
        assert "category" in data
        assert "response" in data

    def test_classify_text_missing_field(self):
        response = client.post("/api/v1/text", json={})
        assert response.status_code == 422  # erro de validação Pydantic
