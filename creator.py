from juego import Habitacion, Laberinto, Pared, Puerta, ParedBomba, Bomba, Bicho, Agresivo, Perezoso,ParedCohete,Cohete,Fantasma,Supporter,Dormilon,ParedPinchos,Pinchos,ParedPoder
from norte import Norte
from sur import Sur
from este import Este
from oeste import Oeste
from orientacion import Orientacion
from cuadrado import Cuadrado


class Creator:
    def crear_habitacion(self, num):
        habitacion = Habitacion(num)
        habitacion.forma = self.crear_forma()
        pared_norte = self.crear_pared()
        habitacion.ponerElementoEnOrientacion(pared_norte, Norte())
        pared_sur = self.crear_pared()
        habitacion.ponerElementoEnOrientacion(pared_sur, Sur())
        pared_este = self.crear_pared()
        habitacion.ponerElementoEnOrientacion(pared_este, Este())
        pared_oeste = self.crear_pared()
        habitacion.ponerElementoEnOrientacion(pared_oeste, Oeste())
        return habitacion

    def crear_forma(self):
        forma=Cuadrado()
        forma.agregarOrientacion(self.fabricarNorte())
        forma.agregarOrientacion(self.fabricarSur())
        forma.agregarOrientacion(self.fabricarEste())
        forma.agregarOrientacion(self.fabricarOeste())
        return forma
    
    def crear_laberinto(self):
        return Laberinto()

    def fabricarNorte(self):
        return Norte()

    def fabricarSur(self):
        return Sur()

    def fabricarEste(self):
        return Este()

    def fabricarOeste(self):
        return Oeste()

    def crear_pared(self):
        return Pared()

    def crear_puerta(self, lado1, lado2):
        return Puerta(lado1, lado2)

    def crear_bomba(self, em):
        return Bomba(em)
    
    def crear_cohete(self, em):
        return Cohete(em)
    
    def crear_pinchos(self, em):
        return Pinchos(em)
    
    def crear_bicho(self,vidas,poder,posicion,modo):
        bicho=Bicho()
        bicho.vidas=vidas
        bicho.poder=poder
        bicho.posicion=posicion
        bicho.modo=modo
        return bicho
    
    def crear_fantasma(self, vidas, poderMagico, posicion, caracter):
        return Fantasma(vidas, poderMagico, posicion, caracter)
    
    def crear_caracter_supporter(self):
        return Supporter()
    
    def crear_caracter_dormilon(self):
        return Dormilon()

    def crear_modo_agresivo(self):
        return Agresivo()

    def crear_modo_perezoso(self):
        return Perezoso()

class CreatorB(Creator):
    def crear_pared(self):
        return ParedBomba()
    
class CreatorC(Creator):
    def crear_pared(self):
        print("🛠 CreatorC ha creado una ParedCohete")
        return ParedCohete()
    
class CreatorD(Creator):
    def crear_pared(self):
        print("🛠 CreatorD ha creado una ParedPinchos")
        return ParedPinchos()
    
class CreatorE(Creator):
    def crear_pared(self):
        print("🛠 CreatorE ha creado una ParedPoder")
        return ParedPoder()

       