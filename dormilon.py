import time
from caracter import Caracter

class Dormilon(Caracter):
    def __init__(self):
        super().__init__()
        
    def dormir(self,fantasma):
        print("Dormilon: Descansando...")
        time.sleep(3)

    def caminar(self, fantasma):
        print("Dormilon: Caminando sin ganas...")
        fantasma.caminar()

    def supportear(self, fantasma):
        fantasma.supportear()
        #print("Dormilon: Intentando supportear sin efecto...")
        
    def __str__(self):
        return "-dormilon"