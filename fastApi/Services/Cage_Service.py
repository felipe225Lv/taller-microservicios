from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.Cage import Cage
from repositories.Cage_Repository import find_cage, save_cage, find_all_cage, remove_cage

def get_all_cages(db: Session, skip: int = 0, limit: int = 10):
    return find_all_cage(db, skip=skip, limit=limit)

def create_cage(db: Session, cage: Cage):
    return save_cage(db, cage)

def get_cage(db: Session, cage_id: int):
    cage = find_cage(db, cage_id)
    if not cage:
        raise HTTPException(status_code=404, detail="Cage not found")
    return cage

def delete_cage(db: Session, cage_id: int):
    return remove_cage(db, cage_id)
