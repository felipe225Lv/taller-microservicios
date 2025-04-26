from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .Base import Base  # Asumiendo que tu clase Base está en un archivo Base.py

class Cage(Base):
    __tablename__ = "cages"
    
    id = Column(Integer, primary_key=True)  # Primary key
    name = Column(String)
    location = Column(String)
    
    animals = relationship("Animal", back_populates="cage")  # One-to-many relationship with Animal
