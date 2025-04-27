from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastApi.db.session import get_db
from fastApi.Schemes.Cage_Scheme import CageCreate, CageResponse
from fastApi.Services.Cage_Service import create_cage, get_cage, get_all_cages, delete_cage

router = APIRouter(
    prefix="/cages",
    tags=["Cages"]
)

@router.post("/", status_code=201, response_model=CageResponse)
def create_cage_route(cage: CageCreate, db: Session = Depends(get_db)):
    return create_cage(cage=cage, db=db)

@router.get("/{cage_id}", response_model=CageResponse)
def get_cage_route(cage_id: int, db: Session = Depends(get_db)):
    return get_cage(cage_id=cage_id, db=db)

@router.delete("/{cage_id}")
def delete_cage_route(cage_id: int, db: Session = Depends(get_db)):
    return delete_cage(cage_id=cage_id, db=db)

@router.get("/", response_model=list[CageResponse])
def get_cages_route(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_all_cages(skip=skip, limit=limit, db=db)
