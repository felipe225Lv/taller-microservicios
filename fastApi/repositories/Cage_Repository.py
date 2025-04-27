from sqlalchemy.orm import Session
from fastApi.models.Cage import Cage
from fastApi.Schemes.Cage_Scheme import CageCreate

def save_cage(db: Session, cage: CageCreate):
    db_cage = Cage(**cage.dict())
    db.add(db_cage)
    db.commit()
    db.refresh(db_cage)
    return db_cage

def find_cage(db: Session, cage_id: int):
    return db.query(Cage).filter(Cage.id == cage_id).first()

def remove_cage(db: Session, cage_id: int):
    delete = db.query(Cage).filter(Cage.id == cage_id).delete()
    db.commit()
    return delete

def find_all_cage(db: Session):
    return db.query(Cage).all()
