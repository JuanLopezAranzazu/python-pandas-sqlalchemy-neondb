from db.database import engine, Base, SessionLocal
# modelos
from models.director import Director
from models.movie import Movie
# utilidades
from utils.load_data import load_db
from utils.create_graphs import generate_graphs

def main():
  # crear las tablas en la base de datos
  try:
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas correctamente")
  except Exception as e:
    print("Error al crear las tablas:", e)

  # crear una sesión de la base de datos
  db = SessionLocal()

  # verificar que la sesión está activa
  try:
    db.execute("SELECT 1")
    print("Sesión activa")
  except Exception as e:
    print("Error al crear la sesión:", e)

  # cargar los datos en la base de datos
  load_db(db)
  
  # generar gráficos
  generate_graphs(db)

if __name__ == "__main__":
  main()
