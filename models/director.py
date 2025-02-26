from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base

# tabla de dimension director
class Director(Base):
  __tablename__ = "director"

  id = Column(Integer, primary_key=True)
  name = Column(String) # nombre del director

  movies = relationship("Movie", back_populates="director", cascade="all, delete")
