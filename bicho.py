from modo import Modo
from agresivo import Agresivo
from perezoso import Perezoso 

class Bicho:
    def __init__(self, vidas, poder, posicion, modo):
        self.vidas = vidas
        self.poder = poder
        self.posicion = posicion
        self.modo = modo

    def actua(self):
        self.modo.actuar(self)

    def iniAgresivo(self):
        self.modo = Agresivo()
        self.poder = 10
        self.vidas = 5

    def iniPerezoso(self):
        self.modo=Perezoso()
        self.poder = 1
        self.vidas = 5

    def __str__(self):
        return "Soy un bicho"