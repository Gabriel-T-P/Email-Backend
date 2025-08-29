# 📧 Email Classifier API

Este projeto é uma API construída em **FastAPI** para classificar emails em **Produtivo** ou **Improdutivo** e sugerir respostas automáticas.  
Agora a API também suporta **upload de arquivos .txt e .pdf**, extraindo o conteúdo e processando-o.

---

## 🚀 Funcionalidades

- Endpoint `/api/v1/classify/` que recebe texto bruto de email e retorna:
  - Categoria (`Produtivo` ou `Improdutivo`)
  - Resposta sugerida

- Endpoint `/api/v1/upload/` que permite enviar arquivos `.txt` ou `.pdf` e retorna:
  - Texto extraído do arquivo
  - Categoria e resposta sugerida

- Documentação automática via **Swagger UI** em `/docs`.

- Testes unitários básicos com **pytest**.

- Pré-processamento de texto com **NLTK** (remoção de stopwords, lematização).

---

## 🛠️ Instalação e Setup

### 1. Clonar o repositório
```bash
git clone git@github.com:Gabriel-T-P/Email-Backend.git
cd Email-Backend
```

### 2. Criar e ativar ambiente virtual
```bash
# Criar o ambiente virtual
python3 -m venv venv_email

# Ativar no Linux/Mac
source venv_email/bin/activate

# Ativar no Windows (PowerShell)
venv_email\Scripts\activate
```

Você saberá que está ativo quando aparecer `(venv_email)` no início da linha do terminal.

### 3. Instalar dependências
O projeto separa dependências de produção e desenvolvimento:

- **Produção (FastAPI, Uvicorn, PyPDF2, NLTK):**
```bash
pip install -r requirements.txt
```

- **Desenvolvimento (pytest, flake8):**
```bash
pip install -r requirements-dev.txt
```

### 4. Baixar recursos do NLTK
Antes de rodar a aplicação pela primeira vez, inicialize os recursos do NLTK:
```bash
python3 setup_nltk.py
```

---

## ▶️ Rodando a aplicação

```bash
uvicorn app.main:app --reload
```

A aplicação ficará disponível em:
- **API Root:** http://127.0.0.1:8000  
- **Swagger Docs:** http://127.0.0.1:8000/docs  

---

## 🧪 Rodando os testes

```bash
pytest
```

Exemplo de teste:  
- Texto: `"Feliz Natal para todos!"` → Categoria esperada: `Improdutivo`.  
- Texto: `"Preciso de atualização do meu pedido"` → Categoria esperada: `Produtivo`.  

---

## 📂 Estrutura do Projeto

```
app/
├── api/
│   └── v1/
│       ├── classify.py         # Endpoints da API
│       └── upload.py           # Endpoint para upload de arquivos
├── core/
│   └── config.py               # Configurações do projeto
├── models/
│   └── schemas.py              # Schemas Pydantic (request/response)
├── services/
│   ├── classifier_service.py   # Lógica de classificação (mock inicial)
│   └── nlp_service.py          # Lógica de pré-processamento NLP
├── main.py                     # Ponto de entrada da aplicação
setup_nltk.py                   # Script para baixar recursos do NLTK
tests/
├── test_classify.py            # Testes unitários para classificação de texto
├── test_upload.py              # Testes unitários para upload de arquivos
└── utils.py                    # helpers reutilizáveis nos testes
```

