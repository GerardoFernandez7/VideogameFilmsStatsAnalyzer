# Importar modulos
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('video_game_films.csv')
df.dropna(subset=['Rotten Tomatoes', 'Metacritic'])

#Funciones
def lineas_5():
    df_5 = df.head(5)
    print("")
    print(df_5)
    print("")

def estadisticas_boxoffice():
    worldwide_box_office = df['Worldwide box office']
    print("")
    print("Las estadisticas resumen del Worldwide box office son: ")
    print(worldwide_box_office)
    print("")

def promedio_rotten_metacritic():
    rotten = int(df['Rotten Tomatoes'].mean())
    meta = int(df['Metacritic'].mean())
    print(f"\n El promedio de las metricas de Rotten Tomatoes es: \n {rotten}")
    print(f"\n El promedio de las metricas de Metacritic es: \n {meta} \n ")

def top10_boxoffice():
    top10_box_office = df.sort_values('Worldwide box office', ascending=False).head(10)
    movies = top10_box_office['Title']
    box_office = top10_box_office['Worldwide box office']
    plt.figure(figsize=(10, 6))
    plt.bar(movies, box_office)
    plt.title('Top 10 Películas - Taquilla Mundial')
    plt.xlabel('Película')
    plt.ylabel('Rango')
    plt.xticks(rotation=45)
    plt.show()

def relacion_rotten_metacritic():
    rotten = df['Rotten Tomatoes']
    meta = df['Metacritic']
    plt.figure(figsize=(20, 10))
    plt.scatter(rotten, meta)
    plt.title('Relacion entre las metricas de Rotten Tomatoes y Metacritic')
    plt.xlabel('')
    plt.ylabel('')
    plt.xticks(rotation=45)
    plt.show()

def distribuidor():
    c_pelis = df['Distributor'].value_counts()
    print(f"\nLa cantidad de peliculas creadas por distribuidor es:\n\n{c_pelis}\n")

def pelis_10anos():
    df['Year'] = pd.to_datetime(df['Release date']).dt.year
    movies_by_year = df[(df['Year'] >= 2010) & (df['Year'] <= 2020)]
    movies_by_year_counts = movies_by_year['Year'].value_counts().sort_index()
    plt.figure(figsize=(15, 8))
    plt.bar(movies_by_year_counts.index, movies_by_year_counts.values)
    plt.title('Cantidad de peliculas en 10 años')
    plt.xlabel('Años')
    plt.xticks(rotation=45)
    plt.ylabel('Cantidad')
    plt.show()