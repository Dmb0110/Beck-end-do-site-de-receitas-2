from typing import Optional, List
from pydantic import BaseModel, ConfigDict, Field
import base64

# Modelo para requisição de login
class LoginRequest(BaseModel):
    username: str = Field(...,min_length=3,max_length=50)
    password: str = Field(..., min_length=2)

# Modelo para requisição de registro de usuário
class RegisterRequest(BaseModel):
    username: str
    password: str

# Modelo para criação de uma nova receita
class CriarReceita(BaseModel):
    nome_da_receita: str = Field(..., min_length=3,max_length=100)
    ingredientes: str = Field(..., min_length=3, max_length=500)
    modo_de_preparo: str = Field(..., min_length=5)
'''
# Modelo de saída de receita (inclui ID)
class ReceitaOut(BaseModel):
    id: int
    nome_da_receita: str
    ingredientes: str
    modo_de_preparo: str
    foto: str | None = None

    model_config = ConfigDict(from_attributes=True)

    @classmethod
    def model_validate(cls, obj):
        data = super().model_validate(obj)
        if obj.foto:
            data.foto = base64.b64encode(obj.foto).decode('utf-8')
        return data
'''

class ReceitaOut(BaseModel):
    id: int
    nome_da_receita: str
    ingredientes: str
    modo_de_preparo: str
    foto: str | None = None

    model_config = ConfigDict(from_attributes=True)

    @classmethod
    def model_validate(cls, obj):
        data = super().model_validate(obj)
        # Se for string (URL), não faz encode
        data.foto = obj.foto
        return data

# Modelo para atualização parcial de receita
class Atualizar(BaseModel):
    nome_da_receita: Optional[str] = Field(None, min_length=3, max_length=100)
    ingredientes: Optional[str] = None
    modo_de_preparo: Optional[str] = Field(None, min_length=5)

# Modelo para resposta de exclusão
class Deletar(BaseModel):
    success: bool
    detail: Optional[str] = None
