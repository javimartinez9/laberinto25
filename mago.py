from personalidad import Personalidad
from activo import Activo
from vago import Vago
from ente import Ente
from estado_ente import Vivo,Muerto

class Mago(Ente):
    def __init__(self):
        super().__init__()
        self.vidas = None
        self.poderMagico = None
        self.posicion = None
        self.personalidad = None
        self.running = True

    def iniActivo(self):
        self.personalidad = Activo()
        self.poderMagico = 2
        self.vidas = 5

    def iniVago(self):
        self.personalidad=Vago()
        self.poderMagico = 0
        self.vidas = 5
        
    def actua(self):
            while self.estaVivo() and self.running:
                self.personalidad.actuar(self)
            
    def ayudar(self):
        #if self.juego is None:
            #print("Error: self.juego no está asignado en el fantasma.")
            #return
        print(self)
        self.juego.buscarPersonajeParaSupportearMago(self)
        
    def caminar(self):
        self.posicion.caminarAleatorio(self)
        
    def estaVivo(self):
        return self.vidas > 0

    def __str__(self):
        return "Soy un mago"+self.personalidad.__str__()