from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

# tabla de hechos movie
class Movie(Base):
  __tablename__ = "movie"

  id = Column(Integer, primary_key=True)
  title = Column(String) # titulo de la pelicula
  overview = Column(String) # descripcion de la pelicula
  rating = Column(Float) # calificacion de la pelicula
  meta_score = Column(Float) # puntaje de la pelicula
  votes = Column(Integer) # votos de la pelicula
  gross = Column(Integer) # ganancias de la pelicula
  director_id = Column(Integer, ForeignKey("director.id")) # director de la pelicula

  director = relationship("Director", back_populates="movies")
