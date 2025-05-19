from caracter import Caracter
from supporter import Supporter
from dormilon import Dormilon
from ente import Ente
from estado_ente import Vivo,Muerto

class Fantasma(Ente):
    def __init__(self):
        super().__init__()
        self.vidas = None
        self.poderMagico = None
        self.posicion = None
        self.caracter = None
        self.running = True

    def iniSupporter(self):
        self.caracter = Supporter()
        self.poderMagico = 10
        self.vidas = 5

    def iniDormilon(self):
        self.caracter=Dormilon()
        self.poderMagico = 0
        self.vidas = 5
        
    def actua(self):
            while self.estaVivo():
                self.caracter.actuar(self)
            
    def supportear(self):
        #if self.juego is None:
            #print("Error: self.juego no está asignado en el fantasma.")
            #return
        print(self)
        self.juego.buscarPersonajeParaSupportear(self)
        
    def caminar(self):
        self.posicion.caminarAleatorio(self)
        
    def estaVivo(self):
        return self.vidas > 0

    def __str__(self):
        return "Soy un fantasma"+self.caracter.__str__()