from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, Float, ForeignKey, Integer, String
from contrib.models import BaseModel


class AtletaModel(BaseModel):
    __tablename__ = "atletas"
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100),nullable=False)
    cpf: Mapped[str] = mapped_column(String(11),nullable=False, unique=True)
    idade: Mapped[int] = mapped_column(Integer,nullable=False)
    peso: Mapped[float] = mapped_column(Float,nullable=False)
    altura: Mapped[float] = mapped_column(Float,nullable=False)
    sexo: Mapped[str] = mapped_column(String(1),nullable=False)
    creation_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    categoria: Mapped['CategoriaModel'] = relationship(back_populates="atletas")
    categoria_id: Mapped[int] = mapped_column(ForeignKey("categoria.pk_id"))
    centro_treinamento: Mapped['CentroModel'] = relationship(back_populates="atletas")
    centro_treinamento_id: Mapped[int] = mapped_column(ForeignKey("centro_treinamento.pk_id"))