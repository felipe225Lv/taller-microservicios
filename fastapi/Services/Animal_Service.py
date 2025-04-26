from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.Animal import Animal
from Schemes.animal_schema import AnimalCreate

def read_animals(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Animal).offset(skip).limit(limit).all()

def create_animal(db: Session, animal: AnimalCreate):
    db_animal = Animal(
        species=animal.species,
        number_of_legs=animal.number_of_legs
    )
    db.add(db_animal)
    db.commit()
    db.refresh(db_animal)
    return db_animal

def read_animal(db: Session, animal_id: int):
    db_animal = db.query(Animal).filter(Animal.id == animal_id).first()
    if db_animal is None:
        raise HTTPException(status_code=404, detail="Animal not found")
    return db_animal

def delete_animal(db: Session, animal_id: int):
    db_animal = db.query(Animal).filter(Animal.id == animal_id).first()
    if db_animal is None:
        raise HTTPException(status_code=404, detail="Animal not found")
    db.delete(db_animal)
    db.commit()
    return {"message": "Animal deleted successfully"}
