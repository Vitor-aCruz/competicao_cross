from typing import Annotated

from pydantic import Field
from contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    
    nome: Annotated[str, Field(description="Nome do CT", example="Power Gym")]
    endereco: Annotated[str, Field(description="Endereço do CT", example="Rua das Flores, 123")]
    proprietario: Annotated[str, Field(description="Nome do proprietário do CT", example="Carlos Silva")]