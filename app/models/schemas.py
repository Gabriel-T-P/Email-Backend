from pydantic import BaseModel, Field


class EmailRequest(BaseModel):
    text: str = Field(
        ...,
        description="Texto bruto do email recebido.",
        example="Preciso de atualização do meu chamado #12345"
    )


class EmailResponse(BaseModel):
    category: str = Field(
        ...,
        description="Categoria do email: Produtivo ou Improdutivo",
        example="Produtivo"
    )
    response: str = Field(
        ...,
        description="Resposta automática sugerida pelo sistema",
        example="Recebemos sua solicitação e em breve retornaremos."
    )
