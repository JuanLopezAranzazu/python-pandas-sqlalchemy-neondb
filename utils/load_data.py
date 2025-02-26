import pandas as pd
from models.director import Director
from models.movie import Movie

# ruta del archivo csv
csv_file = "./data/movies_data.csv"

# cargar datos del dataset
def load_data(file_path):
  return pd.read_csv(file_path)

# cargar los datos en la db
def load_db(db):
  try:
    dataFrame = load_data(csv_file)

    # borrar filas duplicadas
    dataFrame.dropna(inplace=True)

    # transformar la columna gross a numérica
    dataFrame["Gross"] = dataFrame["Gross"].str.replace(',', '').astype(int)

    # cargar los datos en la tabla de directores
    if db.query(Director).count() == 0:
      for director in dataFrame["Director"].unique():
        db.add(Director(name=director))
      db.commit()
      print("Datos de directores cargados correctamente")

    # cargar los datos en la tabla de películas
    if db.query(Movie).count() == 0:
      for _, row in dataFrame.iterrows():
        movie = Movie(
          title=row["Series_Title"],
          overview=row["Overview"],
          rating=row["IMDB_Rating"],
          meta_score=row["Meta_score"],
          votes=row["No_of_Votes"],
          gross=row["Gross"],
          director_id=db.query(Director).filter(Director.name == row["Director"]).first().id
        )
        db.add(movie)
      db.commit()
      print("Datos de películas cargados correctamente")
  except Exception as e:
    print(f"Error al cargar los datos: {e}")
