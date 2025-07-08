from pydantic import BaseModel, PositiveFloat, EmailStr, field_validator
from enum import Enum
from datetime import datetime
from typing import Optional

class CategoriaBase(str, Enum):
    categoria1 = "Eletrônico"
    categoria2 = "Eletrodoméstico"
    categoria3 = "Móveis"
    categoria4 = "Roupas"
    categoria5 = "Calçados"

class ProdutoBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    preco: PositiveFloat
    categoria: str
    email_fornecedor: EmailStr

    @field_validator("categoria")
    def validar_categoria(cls, v):
        if v in [item.value for item in CategoriaBase]:
            return v
        raise ValueError("Categoria inválida")
    
class ProdutoCreate(ProdutoBase):
    pass

class ProdutoResponse(ProdutoBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class ProdutoUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    preco: Optional[PositiveFloat] = None
    categoria: Optional[str] = None
    email_fornecedor: Optional[EmailStr] = None

    @field_validator("categoria", mode="before")
    def validar_categoria(cls, v):
        if v is None:
            return v
        if v in [item.value for item in CategoriaBase]:
            return v
        raise ValueError("Categoria inválida")