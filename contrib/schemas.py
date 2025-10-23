from datetime import datetime
from typing import Annotated
from pydantic import UUID4, BaseModel, Field

class BaseSchema(BaseModel):
    class Config:
        extra = 'forbid'
        from_attributes = True
        
class OutMixin(BaseModel):
    id: Annotated[UUID4, Field(description="Identificador único")]
    created_at: Annotated[datetime, Field(description="Data e hora de criação do registro")]