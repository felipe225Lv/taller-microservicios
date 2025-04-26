from sqlalchemy.orm import Session
from models.Cage import Cage
from Schemes.Cage_Scheme import CageCreate

def create_cage(db: Session, cage: CageCreate):
    db_cage = Cage(**cage.dict())
    db.add(db_cage)
    db.commit()
    db.refresh(db_cage)
    return db_cage

def get_cage(db: Session, cage_id: int):
    return db.query(Cage).filter(Cage.id == cage_id).first()
