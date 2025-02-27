import os
import pandas as pd
from sqlalchemy.sql import func
import matplotlib.pyplot as plt
from models.director import Director
from models.movie import Movie

# directorio
graphs_dir = "graphs"

# grafica top 5 promedio de calificación por director
def plot_directors_by_rating(db):
  # obtener datos
  results = (
    db.query(Director.name, func.avg(Movie.rating).label("rating"))
    .join(Movie)
    .group_by(Director.name)
    .order_by(func.avg(Movie.rating).desc())
    .limit(5)
    .all()
  )

  # crear dataframe
  df = pd.DataFrame(results, columns=["name", "rating"])

  # crear gráfica
  plt.figure(figsize=(10, 6))
  plt.bar(df["name"], df["rating"], color="skyblue")
  plt.xlabel("Director")
  plt.ylabel("Promedio de calificación")
  plt.title("Top 5 promedio de calificación por director")
  plt.xticks(rotation=90)
  plt.ticklabel_format(style="plain", axis="y")
  plt.tight_layout()

  # guardar gráfica
  plt.savefig(os.path.join(graphs_dir, "directors_by_rating.png"))
  plt.close()

# grafica top 5 peliculas por votos
def plot_movies_by_votes(db):
  # obtener datos
  results = (
    db.query(Movie.title, Movie.votes)
    .order_by(Movie.votes.desc())
    .limit(5)
    .all()
  )

  # crear dataframe
  df = pd.DataFrame(results, columns=["title", "votes"])

  # crear gráfica
  plt.figure(figsize=(10, 6))
  plt.bar(df["title"], df["votes"], color="skyblue")
  plt.xlabel("Pelicula")
  plt.ylabel("Votos")
  plt.title("Top 5 peliculas por votos")
  plt.xticks(rotation=90)
  plt.ticklabel_format(style="plain", axis="y")
  plt.tight_layout()

  # guardar gráfica
  plt.savefig(os.path.join(graphs_dir, "movies_by_votes.png"))
  plt.close()

# grafica top 5 peliculas por ingresos
def plot_movies_by_gross(db):
  # obtener datos
  results = (
    db.query(Movie.title, Movie.gross)
    .order_by(Movie.gross.desc())
    .limit(5)
    .all()
  )

  # crear dataframe
  df = pd.DataFrame(results, columns=["title", "gross"])

  # crear gráfica
  plt.figure(figsize=(10, 6))
  plt.bar(df["title"], df["gross"], color="skyblue")
  plt.xlabel("Pelicula")
  plt.ylabel("Ingresos")
  plt.title("Top 5 peliculas por ingresos")
  plt.xticks(rotation=90)
  plt.ticklabel_format(style="plain", axis="y")
  plt.tight_layout()

  # guardar gráfica
  plt.savefig(os.path.join(graphs_dir, "movies_by_gross.png"))
  plt.close()

# grafica top 5 directores por ingresos
def plot_directors_by_gross(db):
  # obtener datos
  results = (
    db.query(Director.name, func.sum(Movie.gross).label("gross"))
    .join(Movie)
    .group_by(Director.name)
    .order_by(func.sum(Movie.gross).desc())
    .limit(5)
    .all()
  )

  # crear dataframe
  df = pd.DataFrame(results, columns=["name", "gross"])

  # crear gráfica
  plt.figure(figsize=(10, 6))
  plt.bar(df["name"], df["gross"], color="skyblue")
  plt.xlabel("Director")
  plt.ylabel("Ingresos")
  plt.title("Top 5 directores por ingresos")
  plt.xticks(rotation=90)
  plt.ticklabel_format(style="plain", axis="y")
  plt.tight_layout()

  # guardar gráfica
  plt.savefig(os.path.join(graphs_dir, "directors_by_gross.png"))
  plt.close()

# crear gráficos
def generate_graphs(db):
  # crear directorio si no existe
  if not os.path.exists(graphs_dir):
    os.makedirs(graphs_dir)

  # crear gráficas
  plot_directors_by_rating(db)
  plot_movies_by_votes(db)
  plot_movies_by_gross(db)
  plot_directors_by_gross(db)

  print("Gráficas generadas en la carpeta 'graphs'")
