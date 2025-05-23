from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from Schemes.Animal_Scheme import AnimalCreate, AnimalResponse
from Services.Animal_Service import create_animal, get_animal, get_all_animals, delete_animal

router = APIRouter(
    prefix="/animals",
    tags=["Animals"]
)

@router.post("/", status_code=201, response_model=AnimalResponse)
def create_animal_route(animal: AnimalCreate, db: Session = Depends(get_db)):
    return create_animal(db, animal)

@router.get("/{animal_id}", response_model=AnimalResponse)
def get_animal_route(animal_id: int, db: Session = Depends(get_db)):
    return get_animal(db, animal_id)

@router.delete("/{animal_id}")
def delete_animal_route(animal_id: int, db: Session = Depends(get_db)):
    return delete_animal(db, animal_id)

@router.get("/", response_model=list[AnimalResponse])
def get_animals_route(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_all_animals(db, skip=skip, limit=limit)
