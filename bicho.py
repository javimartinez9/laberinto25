from modo import Modo
from agresivo import Agresivo
from ente import Ente
from estado_ente import Vivo,Muerto

class Bicho(Ente):
    def __init__(self):
        super().__init__()
        self.modo = None
        self.running = True
        self.poder = None
        self.vidas = None
        self.posicion = None
        

    def actua(self):
        while self.estaVivo():
            self.modo.actuar(self)

    def iniAgresivo(self):
        self.modo = Agresivo()
        self.poder = 10
        self.vidas = 5

    def iniPerezoso(self):
        self.poder = 1
        self.vidas = 5

    def atacar(self):
        self.juego.buscarPersonaje(self)
    def caminar(self):
        self.posicion.caminarAleatorio(self)

    def estaVivo(self):
        return self.vidas > 0

    def __str__(self):
        return "Soy un bicho"+self.modo.__str__()

    