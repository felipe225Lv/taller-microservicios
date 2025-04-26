from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from Schemes.Animal_Scheme import AnimalCreate, AnimalResponse
from Services.Animal_Service import create_animal, read_animal, read_animals, delete_animal

router = APIRouter(
    prefix="/animals",
    tags=["Animals"]
)

@router.post("/", status_code=201, response_model=AnimalResponse)
def create_animal_route(animal: AnimalCreate, db: Session = Depends(get_db)):
    return create_animal(animal=animal, db=db)

@router.get("/{animal_id}", response_model=AnimalResponse)
def get_animal_route(animal_id: int, db: Session = Depends(get_db)):
    return read_animal(animal_id=animal_id, db=db)

@router.delete("/{animal_id}")
def delete_animal_route(animal_id: int, db: Session = Depends(get_db)):
    return delete_animal(animal_id=animal_id, db=db)

@router.get("/", response_model=list[AnimalResponse])
def get_animals_route(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return read_animals(skip=skip, limit=limit, db=db)
