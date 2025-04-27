from sqlalchemy.orm import Session
from fastapi import HTTPException
from fastApi.models.Animal import Animal
from fastApi.repositories.Animal_Repository import save_animal, find_animal, find_all_animals, remove_animal

def get_all_animals(db: Session, skip: int = 0, limit: int = 10):
    return find_all_animals(db, skip=skip, limit=limit)

def create_animal(db: Session, animal: Animal):
    return save_animal(db, animal)

def get_animal(db: Session, animal_id: int):
    animal = find_animal(db, animal_id)
    if not animal:
        raise HTTPException(status_code=404, detail="Animal not found")
    return animal   

def delete_animal(db: Session, animal_id: int):
    return remove_animal(db, animal_id)
