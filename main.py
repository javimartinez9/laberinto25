from creator import Creator
from creator import CreatorB,CreatorC
from juego import Juego
from este import Este
from oeste import Oeste
import time

"""
#ejemplo de uso
fm = Creator()
juego = Juego()
juego.laberinto = juego.crearLaberinto2HabFM(fm)
hab1=juego.obtenerHabitacion(1)
hab2=juego.obtenerHabitacion(2)
print(hab1.num)
print(hab2.num)
"""
"""
#laberinto con paredes bomba
juego=Juego()
fmb = CreatorB()
juego.laberinto = juego.crearLaberinto2HabBomba(fmb)
hab1=juego.obtenerHabitacion(1)
hab2=juego.obtenerHabitacion(2)
bm1=hab1.obtenerElementoEnOrientacion(Este())
bm2=hab2.obtenerElementoEnOrientacion(Oeste())
print(bm1.activa)
print(bm2.activa)
"""

"""
juego = Juego()
#laberinto con paredes cohete
fmc = CreatorC()
juego.laberinto = juego.crearLaberinto2HabCoheteFM(fmc)
hab1 = juego.obtenerHabitacion(1)
hab2 = juego.obtenerHabitacion(2)
coh1=hab1.obtenerElementoEnOrientacion(Este())
coh2=hab2.obtenerElementoEnOrientacion(Oeste())
print(coh1.cohete_listo)
print(coh2.cohete_listo)
coh1.entrar()
"""
"""
juego=Juego()
#laberinto con paredes cohete(decorator)
fmb = CreatorC()
juego.laberinto = juego.crearLaberinto2HabCohete(fmb)
hab1=juego.obtenerHabitacion(1)
hab2=juego.obtenerHabitacion(2)
coh1=hab1.obtenerElementoEnOrientacion(Este())
coh2=hab2.obtenerElementoEnOrientacion(Oeste())
print(coh1.cohete_listo)
print(coh2.cohete_listo)
"""
'''
juego=Juego()
# Crear laberinto de 4 habitaciones
fm = Creator()
juego.laberinto = juego.crearLaberinto4HabFantasmas(fm)

# Mostrar el número de cada habitación
for habitacion in juego.laberinto.hijos:
    print(f"Habitación {habitacion.num}")

#mostrar los bichos del juego
for fantasma in juego.fantasmas:
    print(fantasma)
    print(f"Fantasma con {fantasma.vidas} vidas y {fantasma.poderMagico} de poder Magico")
    print(f"Posición {fantasma.posicion.num}")
    
for bicho in juego.bichos:
    print(bicho)
    print(f"bicho con {bicho.vidas} vidas y {bicho.poder} de poder")
    print(f"Posición {bicho.posicion.num}")
'''

"""
juego=Juego()
# Crear laberinto de 4 habitaciones
fm = Creator()
juego.laberinto = juego.crearLaberinto4Hab(fm)

# Mostrar el número de cada habitación
for habitacion in juego.laberinto.hijos:
    print(f"Habitación {habitacion.num}")

#mostrar los bichos del juego
for bicho in juego.bichos:
    print(bicho)
    print(f"bicho con {bicho.vidas} vidas y {bicho.poder} de poder")
    print(f"Posición {bicho.posicion.num}")
"""

"""
# Ejemplo de uso de recorrer con print
print("\nRecorriendo el laberinto e imprimiendo:")
juego.laberinto.recorrer(print)

#def abrirPuertas(obj):
#    if obj.esPuerta():
#        obj.abrir()
juego.abrir_puertas()

juego.cerrar_puertas()

bicho=juego.bichos[0]
juego.lanzarBicho(bicho)
time.sleep(3)
bicho.vidas=0
"""