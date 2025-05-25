
import copy
from laberinto import Laberinto
from bicho import Bicho
from habitacion import Habitacion
from puerta import Puerta
from norte import Norte
from sur import Sur
from este import Este
from oeste import Oeste
from orientacion import Orientacion
from agresivo import Agresivo
from perezoso import Perezoso
from pared import Pared
from bomba import Bomba
from pared_bomba import ParedBomba
from ente import Personaje
from pared_cohete import ParedCohete
from cohete import Cohete
from fantasma import Fantasma
from supporter import Supporter
from dormilon import Dormilon
import threading
import sys

class Juego:
    def __init__(self):
        self.habitaciones = {}
        self.bichos = []
        self.fantasmas=[]
        self.prototipo = None
        self.personaje=None
        self.bicho_threads = {}
        self.fantasma_threads={}
        self.running = True 
   
    def clonarLaberinto(self):
        return copy.deepcopy(self.prototipo)

    def agregar_bicho(self, bicho):
        bicho.juego = self
        self.bichos.append(bicho)
        
    def eliminarBicho(self, bicho):
        if bicho in self.bichos:
            self.bichos.remove(bicho)

    def hayBichosVivos(self):
        return any(b.estaVivo() for b in self.bichos)
    '''
    def terminarJuego(self):
        print("Juego terminado. ¡Has ganado!")
        sys.exit(0)  # Cierra el programa con código 0 (éxito)
    '''
    
    def agregar_fantasma(self,fantasma):
        fantasma.juego = self
        self.fantasmas.append(fantasma)

    def lanzarBicho(self, bicho):
        import threading
        if bicho not in self.bicho_threads:
            thread = threading.Thread(target=bicho.actua)
            self.bicho_threads[bicho] = []
        self.bicho_threads[bicho].append(thread)
        thread.start()
        
    def lanzarFantasma(self, fantasma):
        import threading
        if fantasma not in self.fantasma_threads:
            thread1 = threading.Thread(target=fantasma.actua)
            self.fantasma_threads[fantasma] = []
        self.fantasma_threads[fantasma].append(thread1)
        thread1.start()
        
    def lanzarFantasmas(self):
        #if self.personaje and self.personaje.posicion:
        for fantasma in self.fantasmas:
            self.lanzarFantasma(fantasma)
                    
        #else:
        #    print("Esperando a que el personaje esté posicionado antes de lanzar fantasmas.")
        #    print("posicion del fantasma",fantasma.posicion.num)
            
                    
    def terminarFantasma(self, fantasma):
        if fantasma in self.fantasma_threads:
            for thread in self.fantasma_threads[fantasma]:
                fantasma.vidas = 0
                fantasma.running = False 
                if thread is not threading.current_thread():
                    thread.join()
                
    def terminarFantasmas(self):
        for fantasma in self.fantasmas:
            self.terminarFantasma(fantasma)
    
    def terminarBichos(self):
        for bicho in self.bichos:
            self.terminarBicho(bicho)

    def terminarBicho(self, bicho):
        if bicho in self.bicho_threads:
            for thread in self.bicho_threads[bicho]:
                bicho.vidas = 0
                bicho.running = False 
                if thread is not threading.current_thread():
                    thread.join()
                try:
                    self.bicho_threads.pop(bicho)
                    self.bichos.remove(bicho)
                except Exception:
                    print("Bicho ya eliminado")
                
                

    def lanzarBichos(self):
        for bicho in self.bichos:
            self.lanzarBicho(bicho)

    def terminarBichos(self):
        for bicho in self.bichos:
            self.terminarBicho(bicho)

    def agregar_personaje(self, nombre):
        self.personaje = Personaje(100, 1000,self,nombre,None)
        self.laberinto.entrar(self.personaje)

    def buscarPersonaje(self,bicho):
        if bicho.posicion.num == self.personaje.posicion.num:
            print(f"El bicho {bicho} ataca al personaje {self.personaje}")
            self.personaje.esAtacadoPor(bicho)
        # Priorizamos ataque a personajes antes que a personajes de apoyo
        else:
            haAtacado = False
            i = 0
            # Solo ataca a 1 mago, no a todos los de la sala
            while haAtacado == False:
                mago = self.magos[i]
                if bicho.posicion.num == mago.posicion.num:
                    print(f"El mago {mago} es atacado por el bicho {bicho}")
                    mago.esAtacadoPor(bicho)
                    haAtacado = True
            
    def buscarPersonajeParaSupportear(self,fantasma):
        if fantasma.posicion.num == self.personaje.posicion.num:
            if self.personaje.vidas > 0:
                print(f"El personaje {fantasma} supportea con poder al personaje {self.personaje}")
                self.personaje.esSupporteadoPor(fantasma)
    
    def buscarBicho(self):
        for bicho in self.bichos:
            if bicho.posicion.num == self.personaje.posicion.num:
                print(f"El bicho {bicho} es atacado por el personaje {self.personaje}")
                bicho.esAtacadoPor(self.personaje)
                
    def abrir_puertas(self):
        def abrirPuertas(obj: Habitacion):
                objeto = obj.forma.este
                if objeto.esPuerta():
                    print(f"Abriendo puerta", obj)
                    objeto.abrir()
                objeto = obj.forma.oeste
                if objeto.esPuerta():
                    print(f"Abriendo puerta", obj)
                    objeto.abrir()
                objeto = obj.forma.norte
                if objeto.esPuerta():
                    print(f"Abriendo puerta", obj)
                    objeto.abrir()
                objeto = obj.forma.sur
                if objeto.esPuerta():
                    print(f"Abriendo puerta", obj)
                    objeto.abrir()
        self.laberinto.recorrer(abrirPuertas)

    def cerrar_puertas(self):
        def cerrarPuertas(obj):
            if obj.esPuerta():
                print(f"Cerrando puerta", obj)
                obj.cerrar()
        self.laberinto.recorrer(cerrarPuertas)

    def iniciar_juego(self):
        # Lógica para iniciar el juego
        pass

    def crearLaberinto2HabFM(self, creator):
        laberinto = creator.crear_laberinto()
        habitacion1 = creator.crear_habitacion(1)
        habitacion2 = creator.crear_habitacion(2)
        puerta = creator.crear_puerta(habitacion1, habitacion2)
        habitacion1.ponerElementoEnOrientacion(puerta, Norte())
        habitacion2.ponerElementoEnOrientacion(puerta, Sur())
        laberinto.agregarHabitacion(habitacion1)
        laberinto.agregarHabitacion(habitacion2)
        return laberinto
    
    def crearLaberinto2HabBomba(self, creator):
        laberinto = creator.crear_laberinto()
        habitacion1 = creator.crear_habitacion(1)
        habitacion2 = creator.crear_habitacion(2)
        puerta = creator.crear_puerta(habitacion1, habitacion2)

        habitacion1.ponerElementoEnOrientacion(puerta, Norte())
        habitacion2.ponerElementoEnOrientacion(puerta, Sur())

        pared1 = creator.crear_pared()
        bomba1 = creator.crear_bomba(pared1)
        habitacion1.ponerElementoEnOrientacion(bomba1, Este())

        pared2 = creator.crear_pared()
        bomba2 = creator.crear_bomba(pared2)
        habitacion2.ponerElementoEnOrientacion(bomba2, Oeste())

        laberinto.agregarHabitacion(habitacion1)
        laberinto.agregarHabitacion(habitacion2)
        return laberinto
    
    def crearLaberinto2HabCoheteFM(self, creator):
        laberinto = creator.crear_laberinto()
        habitacion1 = creator.crear_habitacion(1)
        habitacion2 = creator.crear_habitacion(2)
        puerta = creator.crear_puerta(habitacion1, habitacion2)

        habitacion1.ponerElementoEnOrientacion(puerta, Norte())
        habitacion2.ponerElementoEnOrientacion(puerta, Sur())

        pared1 = creator.crear_pared()  # Aquí se espera que sea ParedCohete()
        habitacion1.ponerElementoEnOrientacion(pared1, Este())

        pared2 = creator.crear_pared()
        habitacion2.ponerElementoEnOrientacion(pared2, Oeste())

        laberinto.agregarHabitacion(habitacion1)
        laberinto.agregarHabitacion(habitacion2)
        return laberinto
    
    def crearLaberinto2HabCohete(self, creator):
        laberinto = creator.crear_laberinto()
        habitacion1 = creator.crear_habitacion(1)
        habitacion2 = creator.crear_habitacion(2)
        puerta = creator.crear_puerta(habitacion1, habitacion2)

        habitacion1.ponerElementoEnOrientacion(puerta, Norte())
        habitacion2.ponerElementoEnOrientacion(puerta, Sur())

        pared1 = creator.crear_pared()
        cohete1 = creator.crear_cohete(pared1)
        habitacion1.ponerElementoEnOrientacion(cohete1, Este())

        pared2 = creator.crear_pared()
        cohete2 = creator.crear_cohete(pared2)
        habitacion2.ponerElementoEnOrientacion(cohete2, Oeste())

        laberinto.agregarHabitacion(habitacion1)
        laberinto.agregarHabitacion(habitacion2)
        return laberinto

    def obtenerHabitacion(self, num):
        return self.laberinto.obtenerHabitacion(num)

    def crearLaberinto4Hab(self, creator):
        laberinto = creator.crear_laberinto()

        habitacion1 = creator.crear_habitacion(1)
        habitacion2 = creator.crear_habitacion(2)
        habitacion3 = creator.crear_habitacion(3)
        habitacion4 = creator.crear_habitacion(4)

        puerta12 = creator.crear_puerta(habitacion1, habitacion2)
        puerta13 = creator.crear_puerta(habitacion1, habitacion3)
        puerta24 = creator.crear_puerta(habitacion2, habitacion4)
        puerta34 = creator.crear_puerta(habitacion3, habitacion4)

        habitacion1.ponerElementoEnOrientacion(puerta12, Sur())
        habitacion1.ponerElementoEnOrientacion(puerta13, Este())
        habitacion3.ponerElementoEnOrientacion(puerta13, Oeste())
        habitacion3.ponerElementoEnOrientacion(puerta34, Sur())
        habitacion2.ponerElementoEnOrientacion(puerta12, Norte())
        habitacion2.ponerElementoEnOrientacion(puerta24, Este())
        habitacion4.ponerElementoEnOrientacion(puerta34, Norte())
        habitacion4.ponerElementoEnOrientacion(puerta24, Oeste())

        bicho1 = creator.crear_bicho(5, 10, habitacion1, creator.crear_modo_agresivo())
        self.agregar_bicho(bicho1)
        bicho3 = creator.crear_bicho(5, 10, habitacion3, creator.crear_modo_agresivo())
        self.agregar_bicho(bicho3)
        bicho2 = creator.crear_bicho(5, 1, habitacion2, creator.crear_modo_perezoso())
        self.agregar_bicho(bicho2)
        bicho4 = creator.crear_bicho(5, 1, habitacion4, creator.crear_modo_perezoso())
        self.agregar_bicho(bicho4)

        habitacion1.bicho = bicho1
        habitacion2.bicho = bicho2
        habitacion3.bicho = bicho3
        habitacion4.bicho = bicho4

        laberinto.agregarHabitacion(habitacion1)
        laberinto.agregarHabitacion(habitacion2)
        laberinto.agregarHabitacion(habitacion3)
        laberinto.agregarHabitacion(habitacion4)

        return laberinto
    
    def crearLaberinto4HabFantasmas(self, creator):
        laberinto = creator.crear_laberinto()

        habitacion1 = creator.crear_habitacion(1)
        habitacion2 = creator.crear_habitacion(2)
        habitacion3 = creator.crear_habitacion(3)
        habitacion4 = creator.crear_habitacion(4)

        puerta12 = creator.crear_puerta(habitacion1, habitacion2)
        puerta13 = creator.crear_puerta(habitacion1, habitacion3)
        puerta24 = creator.crear_puerta(habitacion2, habitacion4)
        puerta34 = creator.crear_puerta(habitacion3, habitacion4)

        habitacion1.ponerElementoEnOrientacion(puerta12, Sur())
        habitacion1.ponerElementoEnOrientacion(puerta13, Este())
        habitacion3.ponerElementoEnOrientacion(puerta13, Oeste())
        habitacion3.ponerElementoEnOrientacion(puerta34, Sur())
        habitacion2.ponerElementoEnOrientacion(puerta12, Norte())
        habitacion2.ponerElementoEnOrientacion(puerta24, Este())
        habitacion4.ponerElementoEnOrientacion(puerta34, Norte())
        habitacion4.ponerElementoEnOrientacion(puerta24, Oeste())
        
        bicho1 = creator.crear_bicho(5, 10, habitacion1, creator.crear_modo_agresivo())
        self.agregar_bicho(bicho1)
        bicho3 = creator.crear_bicho(5, 10, habitacion3, creator.crear_modo_agresivo())
        self.agregar_bicho(bicho3)
        bicho2 = creator.crear_bicho(5, 1, habitacion2, creator.crear_modo_perezoso())
        self.agregar_bicho(bicho2)
        bicho4 = creator.crear_bicho(5, 1, habitacion4, creator.crear_modo_perezoso())
        self.agregar_bicho(bicho4)

        habitacion1.bicho = bicho1
        habitacion2.bicho = bicho2
        habitacion3.bicho = bicho3
        habitacion4.bicho = bicho4

        # Crear y configurar los fantasmas
        fantasma1 = Fantasma()
        fantasma1.iniSupporter()  # Inicializar como Supporter
        fantasma1.posicion = habitacion1
        self.agregar_fantasma(fantasma1)

        fantasma2 = Fantasma()
        fantasma2.iniDormilon()  # Inicializar como Dormilon
        fantasma2.posicion = habitacion2
        self.agregar_fantasma(fantasma2)

        fantasma3 = Fantasma()
        fantasma3.iniSupporter()  # Inicializar como Supporter
        fantasma3.posicion = habitacion3
        self.agregar_fantasma(fantasma3)

        fantasma4 = Fantasma()
        fantasma4.iniDormilon()  # Inicializar como Dormilon
        fantasma4.posicion = habitacion4
        self.agregar_fantasma(fantasma4)

        # Asignar los fantasmas a las habitaciones
        habitacion1.fantasma = fantasma1
        habitacion2.fantasma = fantasma2
        habitacion3.fantasma = fantasma3
        habitacion4.fantasma = fantasma4

        laberinto.agregarHabitacion(habitacion1)
        laberinto.agregarHabitacion(habitacion2)
        laberinto.agregarHabitacion(habitacion3)
        laberinto.agregarHabitacion(habitacion4)

        return laberinto


    def terminarJuego(self):
        self.terminarBichos()
        self.terminarFantasmas()
        if self.personaje.vidas==0:
            print(" los bichos han ganado el juego")
            
        
