from typing import List
from uuid import uuid4
from fastapi import APIRouter, Body

from categorias.model import CategoriaModel
from categorias.schemas import CategoriaIn, CategoriaOut
from contrib.dependencias import DatabaseDependency


router = APIRouter()

@router.post("/create",
             response_model=CategoriaOut)
async def create_atleta(db_session: DatabaseDependency, categoria_in: CategoriaIn=Body(...))->CategoriaOut:
    
    categoria_out = CategoriaOut(id=uuid4(), **categoria_in.model_dump())
    categoria_model = CategoriaModel(**categoria_out.model_dump())
    
    db_session.add(categoria_model)
    await db_session.commit()
    
    
    return categoria_out

