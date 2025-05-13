from caracter import Caracter
from supporter import Supporter
from dormilon import Dormilon
class Fantasma:
    def __init__(self):
        self.vidas = None
        self.poderMagico = None
        self.posicion = None
        self.caracter = None

    def iniSupporter(self):
        self.caracter = Supporter()
        self.poderMagico = 10
        self.vidas = 5

    def iniDormilon(self):
        self.caracter=Dormilon()
        self.poderMagico = 0
        self.vidas = 5
    
    def __str__(self):
        return "Soy un fantasma"+self.caracter.__str__()