from pydantic import BaseModel

# Schema para enviar foto (guardar URL no banco)
class FotoCreate(BaseModel):
    foto_url: str

# Schema para deletar foto (identificar pelo ID da receita ou da foto)
class FotoDelete(BaseModel):
    receita_id: int
