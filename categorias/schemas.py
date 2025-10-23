from typing import Annotated

from pydantic import UUID4, Field
from contrib.schemas import BaseSchema


class CategoriaIn(BaseSchema):
    
    nome: Annotated[str, Field(description="Nome da categoria", examples=["Força"])]
    
class CategoriaOut(CategoriaIn):
    id: Annotated[UUID4, Field(description="Identificador único da categoria")]
    
    pass