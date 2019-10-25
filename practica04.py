"""
	@vysery98

	Laboratorio 04:

	En función del archivo .txt, hacer:
	
	- Encontrar todos los que han hecho mas de 3 goles
	- Encontrar los que son del país Nigeria
	- El valor mínimo de la caracteristica Height
	- El valor máximo de la caracteristica Height
"""

# codecs: libreria para manejar archivos 'r'/read
import codecs
# json: libreria para hacer parsing de datos
import json

# proceso para lectura del archivo datos.txt
archivo = codecs.open("datos.txt", "r")
info = archivo.readlines()

# transformar las cadenas del archivo .txt en diccionarios
dic_lin = [json.loads(l) for l in info]

# items - diccionarios en tuplas
# funcion anónima para mostrar aquellos con más de 3 goles
goles = lambda x: list(x.items())[1][1] > 3

# funcion anónima para mostrar aquellos de Nigeria
pais = lambda x: list(x.items())[0][1] == "Nigeria"

# Crea únicamente la lista con los valores de Height
height = list(map(lambda x: x["Height"], dic_lin))

# funcion anónima para mostrar al jugador más pequeño
minim = lambda x: list(x.items())[2][1] == min(height)

# funcion anónima para mostrar al jugador más alto
maxim = lambda x: list(x.items())[2][1] == max(height)

# Salida de Datos
print("Han hecho mas de 3 goles: ")
print(list(filter(goles, dic_lin)))

print("\nSon del país Nigeria: ")
print(list(filter(pais, dic_lin)))

print("\nJugador más pequeño: ")
print(list(filter(minim, dic_lin)))

print("\nJugador más alto: ")
print(list(filter(maxim, dic_lin)))
