from caracter import Caracter
from supporter import Supporter
class Fantasma:
    def __init__(self, vidas, poderMagico, posicion, caracter):
        self.vidas = vidas
        self.poderMagico = poderMagico
        self.posicion = posicion
        self.caracter = caracter

    def iniSupporter(self):
        self.caracter = Supporter()
        self.poderMagico = 10
        self.vidas = 5

    def iniDormilon(self):
        self.poderMagico = 0
        self.vidas = 5
    
    def __str__(self):
        return "Soy un fantasma"+self.caracter.__str__()