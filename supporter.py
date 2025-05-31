import time
from caracter import Caracter
class Supporter(Caracter):
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return "-supporter"
    
    def dormir(self,fantasma):
        print("Supporter: Durmiendo un poco...")
        time.sleep(1)

    def caminar(self,fantasma):
        print("Supporter: Flotando con determinación...")
        fantasma.caminar()

    def supportear(self,fantasma):
        fantasma.supportear()  # Llama al ataque real