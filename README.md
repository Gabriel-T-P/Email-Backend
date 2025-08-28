# 📧 Email Classifier API

Este projeto é uma API construída em **FastAPI** para classificar emails em **Produtivo** ou **Improdutivo** e sugerir respostas automáticas.  
No momento, a API está com um classificador **mockado** (regra simples). Futuramente será integrado um modelo de Machine Learning com **scikit-learn**.

---

## 🚀 Funcionalidades

- Endpoint `/api/v1/classify/` que recebe um texto de email e retorna:
  - Categoria (`Produtivo` ou `Improdutivo`)
  - Resposta sugerida

- Documentação automática via **Swagger UI** em `/docs`.

---

## 🛠️ Instalação e Setup

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/email-classifier-api.git
cd email-classifier-api
```

### 2. Criar e ativar ambiente virtual

# Criar o ambiente virtual
```bash
python3 -m venv venv_email
```
# Ativar no Linux/Mac
```bash
source venv_email/bin/activate
```

# Ativar no Windows (PowerShell)
```bash
venv_email\Scripts\activate
```
Você saberá que está ativo quando aparecer (venv_email) no início da linha do terminal.

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

## ▶️ Rodando a aplicação
```bash
uvicorn app.main:app --reload
```
A aplicação ficará disponível em:
- API Root: http://127.0.0.1:8000
- Swagger Docs: http://127.0.0.1:8000/docs
