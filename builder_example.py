from director import Director
from laberinto_builder import LaberintoBuilder
from laberinto import Laberinto
from habitacion import Habitacion
from puerta import Puerta
import time


def update(juego):
    while len(juego.bichos) > 0:
        juego.personaje.caminar()
        juego.buscarBicho()
        time.sleep(3)
    print("GANÓ EL PERSONAJE")

director = Director()

filename = "./lab4HabFantasmas.json"

data = director.leerArchivo(filename)
if data:
    print("Data from JSON file:")
    print(data)
else:
    print("Failed to read data from JSON file.")

juego = director.procesar(filename)
juego = director.obtenerJuego()
juego.agregar_personaje("pepe")

# Ejemplo de uso de recorrer con print
# print("\nRecorriendo el laberinto e imprimiendo:")
# juego.laberinto.recorrer(r)

# print("Personaje", juego.personaje.nombre, juego.personaje.vidas,juego.personaje.posicion.num,juego.personaje.poder)

#juego.buscarBicho(self)

'''
# Mostrar los bichos del juego y atacar
for bicho in juego.bichos:
    print(bicho)
    print(f"Bicho con {bicho.vidas} vidas y {bicho.poder} de poder")
    print(f"Posición {bicho.posicion.num}")
    #juego.buscarPersonaje(bicho)  # Invoca el ataque si el bicho está en la misma posición que el personaje
    #juego.buscarBicho(bicho)
# Mostrar los fantasmas y sus atributos
'''

'''
for fantasma in juego.fantasmas:
    print(fantasma)
    print(f"Fantasma con {fantasma.vidas} vidas y {fantasma.poderMagico} de poderMagico")
    print(f"Posición {fantasma.posicion.num}")
    juego.buscarPersonajeParaSupportear(fantasma)
'''


# Mostrar el personaje y sus atributos
# print("Personaje", juego.personaje.nombre, juego.personaje.vidas,juego.personaje.posicion.num)
#juego.buscarBicho()

# Lógica de abrir puertas, lanzar bichos y terminar bichos
juego.abrir_puertas()
#juego.personaje.caminar()
print("posicion personaje despues de caminar",juego.personaje.posicion.num)
juego.lanzarFantasmas()
juego.lanzarBichos()
update(juego)
#juego.buscarBicho()
#juego.buscarBicho()
#juego.terminarBichos()
#time.sleep(3)
#juego.terminarFantasmas()



