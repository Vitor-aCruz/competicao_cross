from fastapi import APIRouter, Body

from atleta.schemas import AtletaIn
from contrib.dependencias import DatabaseDependency


router = APIRouter()

@router.post("/create")
async def create_atleta(db_session: DatabaseDependency, atleta_in: AtletaIn=Body(...)):
    
    
    
    pass