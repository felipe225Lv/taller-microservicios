from sqlalchemy.orm import Session
from models.Animal import Animal
from Schemes.Animal_Scheme import AnimalCreate

def create_animal(db: Session, animal: AnimalCreate):
    db_animal = Animal(**animal.dict())
    db.add(db_animal)
    db.commit()
    db.refresh(db_animal)
    return db_animal

def get_animal(db: Session, animal_id: int):
    return db.query(Animal).filter(Animal.id == animal_id).first()
