# Importar modulos
import videogames_films_funciones as f
import pandas as pd

# Declarar variables
seguir_en_programa = True
df = pd.read_csv('video_game_films.csv')

# Eliminar las filas que esten vacias en estas columnas
df.dropna(subset=['Rotten Tomatoes'])
df.dropna(subset=['Metacritic'])

# Menú principal
while seguir_en_programa:
    print("")
    print("---> BIENVENIDO <---")
    print("   ¿Que desea hacer?")
    print("")
    print("1. Ver las primeras 5 lineas del conjunto de datos")
    print("2. Ver las estadisticas resumen del Worldwide box office")
    print("3. Ver el promedio de las metricas de Rotten Tomatoes y Metacritic")
    print("4. Ver grafica del top 10 de peliculas con mayor 'Worldwide box office'")
    print("5. Ver grafico de dispersion sobre relacion de metricas de Rotten Tomatoes y Metacritic")
    print("6. Ver la cantidad de peliculas creadas por distribuidor")
    print("7. Ver grafico de cantidad de peliculas en un rango de 10 años")
    print("8. Salir")
    print("")
    
    opcion = input("Seleccione una opción válida ")
    
    # Hacer que la opción elegida sea un dígito, y si no lo es, volver a ejecutar el menú
    if opcion.isdigit() == False:
        print("Seleccione un tipo de valor válido")
    else:
        opcion = int(opcion)

    if opcion == 1:
        f.lineas_5()
    
    if opcion == 2:
        f.estadisticas_boxoffice()
    
    if opcion == 3:
        f.promedio_rotten_metacritic()

    if opcion == 4:
        f.top10_boxoffice()
    
    if opcion == 5:
        f.relacion_rotten_metacritic()
    
    if opcion == 6:
        f.distribuidor()
    
    if opcion == 7:
        f.pelis_10anos()
    
    if opcion == 8:
        seguir_en_programa = False
        print("Eso ha sido todo, vuelva pronto!")        
    else:
        print("Seleccione una opción válida.")