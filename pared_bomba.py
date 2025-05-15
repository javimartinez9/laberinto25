from pared import Pared

class ParedBomba(Pared):
    def __init__(self):
        super().__init__()
        self.activa = False

    from pared import Pared

class ParedBomba(Pared):
    def __init__(self):
        super().__init__()
        self.activa = True

    def entrar(self, ente):
        if self.activa:
            print("💥 BOOM: Has chocado con una pared bomba")
            ente.vidas -= 1
            print(f"⚠️  {ente} pierde una vida. Vidas restantes: {ente.vidas}")
            if ente.vidas <= 0:
                ente.estadoEnte.morir(ente)
            self.activa = False  # La bomba solo se activa una vez
        else:
            print("La pared bomba ya ha explotado")
