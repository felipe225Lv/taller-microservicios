from typing import Optional
from pydantic import BaseModel
from fastApi.Schemes.Cage_Scheme import CageResponse

class AnimalBase(BaseModel):
    species: str
    number_of_legs: int

class AnimalCreate(AnimalBase):
    pass

class AnimalResponse(AnimalBase):
    id: int
    cage: Optional [CageResponse] = None
    
    class Config:
        from_attributes = True
