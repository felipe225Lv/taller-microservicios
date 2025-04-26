from pydantic import BaseModel

class CageBase(BaseModel):
    name: str
    location: str

class CageCreate(CageBase):
    pass

class CageResponse(CageBase):
    id: int

    class Config:
        orm_mode = True
