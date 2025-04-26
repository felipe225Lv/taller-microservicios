from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.Cage import Cage
from Schemes.cage_schema import CageCreate  # Asegúrate que el nombre coincida

def read_cages(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Cage).offset(skip).limit(limit).all()

def create_cage(db: Session, cage: CageCreate):
    db_cage = Cage(name=cage.name, location=cage.location)
    db.add(db_cage)
    db.commit()
    db.refresh(db_cage)
    return db_cage

def read_cage(db: Session, cage_id: int):
    db_cage = db.query(Cage).filter(Cage.id == cage_id).first()
    if db_cage is None:
        raise HTTPException(status_code=404, detail="Cage not found")
    return db_cage

def delete_cage(db: Session, cage_id: int):
    db_cage = db.query(Cage).filter(Cage.id == cage_id).first()
    if db_cage is None:
        raise HTTPException(status_code=404, detail="Cage not found")
    db.delete(db_cage)
    db.commit()
    return {"message": "Cage deleted successfully"}
