from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .Base import Base  # Asumiendo que tu clase Base está en un archivo Base.py

class Animal(Base):
    __tablename__ = "animals"
    
    id = Column(Integer, primary_key=True)
    species = Column(String)
    color = Column(String)
    number_of_legs = Column(Integer)
    cage_id = Column(Integer, ForeignKey("cages.id"))  # Foreign key to Cage
    
    cage = relationship("Cage", back_populates="animals")
