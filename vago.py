import time
from personalidad import Personalidad

class Vago(Personalidad):
    def __init__(self):
        super().__init__()
        
    def dormir(self,mago):
        print("Vago: Descansando tranquilo...")
        time.sleep(3)

    def caminar(self, mago):
        print("Vago: Caminando sin ganas...")
        mago.caminar()

    def ayudar(self,mago):
        mago.ayudar()
        
        
    def __str__(self):
        return "-vago"