from fastapi import APIRouter, Body

from categorias.schemas import CategoriaIn, CategoriaOut
from contrib.dependencias import DatabaseDependency


router = APIRouter()

@router.post("/create",
             response_model=CategoriaOut)
async def create_atleta(db_session: DatabaseDependency, categoria_in: CategoriaIn=Body(...))->CategoriaOut:
    
    
    
    pass