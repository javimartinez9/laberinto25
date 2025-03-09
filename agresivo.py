from modo import Modo

class Agresivo(Modo):
    def __init__(self):
        super().__init__()

    def dormir(self, bicho):
        print("Agresivo->Dormitando un rato....")

    def caminar(self, bicho):
        print("Agresivo->Caminando....")

    def atacar(self, bicho):
        print("Agresivo->Atacando ferozmente....")

    def __str__(self):
        return "Soy un bicho modo agresivo"