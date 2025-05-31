import time
from modo import Modo

class Agresivo(Modo):
    def __init__(self):
        super().__init__()

    def dormir(self, bicho):
        print("Agresivo: Durmiendo un poco...")
        time.sleep(1)

    def caminar(self, bicho):
        print("Agresivo: Caminando con determinación...")
        bicho.caminar()

    def atacar(self, bicho):
        #print("Agresivo: ¡Atacando con furia!")
        bicho.atacar()  # Llama al ataque real

    def __str__(self):
        return "-agresivo"