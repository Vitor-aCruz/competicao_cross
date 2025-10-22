
from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import Integer, String
from contrib.models import BaseModel


class CategoriaModel(BaseModel):
    __tablename__ = "categoria"
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100),nullable=False, unique=True)
    atleta: Mapped['AtletaModel'] = relationship(back_populates="categoria")
    