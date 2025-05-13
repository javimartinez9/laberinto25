from pared import Pared

class ParedCohete(Pared):
    def __init__(self):
        super().__init__()
        self.cohete_listo = True
        print("🔧 Se ha creado una ParedCohete con cohete listo:", self.cohete_listo)

    def entrar(self):
        print("Entrando en una pared cohete")