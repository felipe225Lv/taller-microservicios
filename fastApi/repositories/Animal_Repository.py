from sqlalchemy.orm import Session
from models.Animal import Animal
from Schemes.Animal_Scheme import AnimalCreate

def save_animal(db: Session, animal: AnimalCreate):
    db_animal = Animal(**animal.dict())
    db.add(db_animal)
    db.commit()
    db.refresh(db_animal)
    return db_animal

def find_animal(db: Session, animal_id: int):
    return db.query(Animal).filter(Animal.id == animal_id).first()

def remove_animal(db: Session, animal_id: int):
    deleted = db.query(Animal).filter(Animal.id == animal_id).delete()
    db.commit()
    return deleted

def find_all_animals(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Animal).offset(skip).limit(limit).all()
