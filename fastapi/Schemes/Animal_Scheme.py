from pydantic import BaseModel

class AnimalBase(BaseModel):
    species: str
    number_of_legs: int  # Corregido a int

class AnimalCreate(AnimalBase):
    pass

class AnimalResponse(AnimalBase):
    id: int

    class Config:
        orm_mode = True
