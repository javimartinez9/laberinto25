import time
from caracter import Caracter

class Dormilon(Caracter):
    def __init__(self):
        super().__init__()
        
    def dormir(self, bicho):
        print("Dormilon: Descansando...")
        time.sleep(3)

    def caminar(self, bicho):
        print("Dormilon: Caminando sin ganas...")

    def atacar(self, bicho):
        print("Dormilon: Intentando supportear sin efecto...")
        
    def __str__(self):
        return "-dormilon"