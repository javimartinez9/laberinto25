from pared import Pared

class ParedCohete(Pared):
    def __init__(self):
        super().__init__()
        self.cohete_listo = True
        print("🔧 Se ha creado una ParedCohete con cohete listo:", self.cohete_listo)

    def entrar(self, ente):
        if self.cohete_listo:
            print("💥 Te ha lanzado un cohete la pared")
            ente.vidas -= 1
            print(f"⚠️  {ente} pierde una vida. Vidas restantes: {ente.vidas}")
            if ente.vidas <= 0:
                ente.vidas = 0
                ente.estadoEnte.morir(ente)
            self.activa = False  # La bomba solo se activa una vez
        else:
            print("La pared cohete ya ha lanzado")
