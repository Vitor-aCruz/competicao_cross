from typing import Annotated

from pydantic import Field
from contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    
    nome: Annotated[str, Field(description="Nome do CT", examples=["Power Gym"])]
    endereco: Annotated[str, Field(description="Endereço do CT", examples=["Rua das Flores, 123"])]
    proprietario: Annotated[str, Field(description="Nome do proprietário do CT", examples=["Carlos Silva"])]