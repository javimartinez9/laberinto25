import time
from personalidad import Personalidad
class Activo(Personalidad):
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return "-activo"
    
    def dormir(self,mago):
        print("Activo: Durmiendo un poco...")
        time.sleep(1)

    def caminar(self,mago):
        print("Mago: Caminando con determinación...")
        mago.caminar()

    def ayudar(self,mago):
        mago.ayudar()  # Llama al ataque real