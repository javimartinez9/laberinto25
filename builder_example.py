from director import Director
from laberinto_builder import LaberintoBuilder
from laberinto import Laberinto
from habitacion import Habitacion
from puerta import Puerta
import time

director = Director()

filename = "./lab4HabIzd4Bichos.json"

data = director.leerArchivo(filename)
if data:
    print("Data from JSON file:")
    print(data)
else:
    print("Failed to read data from JSON file.")

juego = director.procesar(filename)
juego = director.obtenerJuego()

# Ejemplo de uso de recorrer con print
print("\nRecorriendo el laberinto e imprimiendo:")
juego.laberinto.recorrer(print)

#mostrar los bichos del juego
for bicho in juego.bichos:
    print(bicho)
    print(f"Bicho con {bicho.vidas} vidas y {bicho.poder} de poder")
    print(f"Posición {bicho.posicion.num}")
    
for fantasma in juego.fantasmas:
    print(fantasma)
    print(f"Fantasma con {fantasma.vidas} vidas y {fantasma.poderMagico} de poderMagico")
    print(f"Posición {fantasma.posicion.num}")

juego.abrir_puertas()
juego.lanzarBichos()
time.sleep(3)
juego.terminarBichos()