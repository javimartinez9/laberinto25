import copy
from laberinto import Laberinto
from habitacion import Habitacion
from puerta import Puerta
from norte import Norte
from sur import Sur
from este import Este
from oeste import Oeste 
from habitacion import Habitacion
from pared import Pared 
from pared_bomba import ParedBomba
from bicho import Bicho
from agresivo import Agresivo
from perezoso import Perezoso
from cuadrado import Cuadrado
from juego import Juego
from tunel import Tunel
from pared_cohete import ParedCohete
from ente import Personaje
from pared_pinchos import ParedPinchos
from pared_poder import ParedPoder
from cohete import Cohete
from pinchos import Pinchos

class LaberintoBuilder:
    def __init__(self):
        self.laberinto = None
        self.juego=None

    def fabricarJuego(self):
        self.juego=Juego()
        self.juego.prototipo = self.laberinto
        self.juego.laberinto = copy.deepcopy(self.juego.prototipo)

    def fabricarLaberinto(self):
        self.laberinto = Laberinto()
        
    ''''
    def fabricarHabitacion(self, num):
        hab=Habitacion(num)	
        hab.forma=self.fabricarForma()
        hab.forma.num=num
        # hab.agregarOrientacion(self.fabricarNorte())
        # hab.agregarOrientacion(self.fabricarSur())
        # hab.agregarOrientacion(self.fabricarEste())
        # hab.agregarOrientacion(self.fabricarOeste())
        for each in hab.forma.orientaciones:
            print("eaaaaach",each)
            
            hab.ponerElementoEnOrientacion(self.fabricarParedBomba(),each)
        self.laberinto.agregarHabitacion(hab)
        return hab
    '''
    
    def fabricarHabitacion(self, num, tiene_bomba=False,tiene_cohete=False,tiene_pinchos=False,tiene_poder=False): 
        hab = Habitacion(num)
        hab.forma = self.fabricarForma()
        hab.forma.num = num
        
        for each in hab.forma.orientaciones:
            if tiene_bomba:
                # Aquí pones pared bomba
                hab.ponerElementoEnOrientacion(self.fabricarParedBomba(), each)
                print("insertando paredBomba en ",hab.num,each)
            elif tiene_cohete:
                if isinstance(each, Este) or isinstance(each, Oeste):
                    hab.ponerElementoEnOrientacion(self.fabricarParedCohete(),each)
                    print("insertando paredCohete en ",hab.num,each)
                else:
                    pared=self.fabricarPared()
                    coh1=self.fabricarCohete(pared)
                    hab.ponerElementoEnOrientacion(coh1,each)
                    print("insertando cohete con decorator ")
                        
            elif tiene_pinchos:
                if isinstance(each, Este) or isinstance(each, Oeste):
                    hab.ponerElementoEnOrientacion(self.fabricarParedPinchos(),each)
                    print("insertando paredPinchos en ",hab.num,each) 
                else:
                    pared=self.fabricarPared()
                    pin1=self.fabricarPinchos(pared)
                    hab.ponerElementoEnOrientacion(pin1,each)
                    print("insertando pinchos con decorator ")
                        
            elif tiene_poder:
                hab.ponerElementoEnOrientacion(self.fabricarParedPoder(),each)
                print("insertando paredPoder en ",hab.num,each)
                '''
            elif tiene_cohete_decorator:
                pared=self.fabricarPared()
                coh1=self.fabricarCohete(pared)
                hab.ponerElementoEnOrientacion(coh1,each)
                print("insertando cohete con decorator ")
                '''
            else:
                # Pared normal
                hab.ponerElementoEnOrientacion(self.fabricarPared(), each)

        self.laberinto.agregarHabitacion(hab)
        return hab

    def fabricarCohete(self,pared):
        return Cohete(pared)
    
    def fabricarPinchos(self,pared):
        return Pinchos(pared)

    def fabricarPared(self):
        return Pared()
    
    def fabricarParedBomba(self):
        return ParedBomba()
    
    def fabricarParedCohete(self):
        return ParedCohete()
    
    def fabricarParedPinchos(self):
        return ParedPinchos()

    def fabricarParedPoder(self):
        return ParedPoder()

    def fabricarPuerta(self, lado1,o1,lado2,o2):
        hab1=self.laberinto.obtenerHabitacion(lado1)
        hab2=self.laberinto.obtenerHabitacion(lado2)
        puerta=Puerta(hab1,hab2)
        objOr1=self.obtenerObjeto(o1)
        objOr2=self.obtenerObjeto(o2)
        hab1.ponerElementoEnOrientacion(puerta,objOr1)
        hab2.ponerElementoEnOrientacion(puerta,objOr2)
    
    def obtenerObjeto(self,cadena):
        obj=None
        match cadena:
            case 'Norte':
                obj=self.fabricarNorte()
            case 'Sur':
                obj=self.fabricarSur()
            case 'Este':
                obj=self.fabricarEste()
            case 'Oeste':
                obj=self.fabricarOeste()
        return obj
     
    def fabricarForma(self):
        forma=Cuadrado()
        forma.agregarOrientacion(self.fabricarNorte())
        forma.agregarOrientacion(self.fabricarSur())
        forma.agregarOrientacion(self.fabricarEste())
        forma.agregarOrientacion(self.fabricarOeste())
        return forma

    def fabricarNorte(self):
        return Norte()
    def fabricarSur(self):
        return Sur()
    def fabricarEste(self):
        return Este()
    def fabricarOeste(self):
        return Oeste()
    def fabricarBichoAgresivo(self):
        bicho=Bicho()
        bicho.modo=Agresivo()
        bicho.iniAgresivo()
        return bicho
    def fabricarBichoPerezoso(self):
        bicho=Bicho()
        bicho.modo=Perezoso()
        bicho.iniPerezoso()
        return bicho

    def obtenerJuego(self):
        return self.juego
    
    def fabricarTunelEn(self,unCont):
        tunel=Tunel(None)
        unCont.agregar_hijo(tunel)
    
    def fabricarBicho(self,modo,posicion):
        if modo=='Agresivo':
            bicho=self.fabricarBichoAgresivo()
        if modo=='Perezoso':
            bicho=self.fabricarBichoPerezoso()
            
        hab=self.laberinto.obtenerHabitacion(posicion)
        
        hab.entrar(bicho)
        self.juego.agregar_bicho(bicho)