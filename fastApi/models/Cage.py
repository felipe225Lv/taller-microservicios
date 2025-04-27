from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base

class Cage(Base):
    __tablename__ = "cages"
    
    id = Column(Integer, primary_key=True) 
    name = Column(String)
    location = Column(String)
    
    animals = relationship("Animal", back_populates="cage")
