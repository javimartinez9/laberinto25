from pared import Pared
from mago import Mago

class ParedPoder(Pared):
    def __init__(self):
        super().__init__()
        self.poder_preparado = True
        print("🔧 Se ha creado una ParedPoder con poder preparado:", self.poder_preparado)

    def entrar(self, ente):
        if self.poder_preparado:
            print("⚡ La pared otorga poder al ente que la toque")
            if hasattr(ente, 'poderMagico'):  # Mago o Fantasma
                print("poderMagico del", ente, "antes:", ente.poderMagico)
                ente.poderMagico += 1
                print("poderMagico del", ente, "después:", ente.poderMagico)
                self.poder_preparado = False
            elif hasattr(ente, 'poder'):  # Personaje o Bicho
                print("poder del", ente, "antes:", ente.poder)
                ente.poder += 1
                print("poder del", ente, "después:", ente.poder)
                self.poder_preparado = False
            else:
                print("⚠️ El ente no tiene atributos de poder conocidos.")
            self.poder_preparado = False
        else:
            print("La pared de poder ya ha dado fuerza a un ente")

