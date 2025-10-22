
from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import Integer, String
from contrib.models import BaseModel


class CentroModel(BaseModel):
    __tablename__ = "centro_treinamento"
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100),nullable=False, unique=True)
    endereco: Mapped[str] = mapped_column(String(200),nullable=False)
    proprietario: Mapped[str] = mapped_column(String(100),nullable=False)
    atleta: Mapped['AtletaModel'] = relationship(back_populates="centro_treinamento")
    