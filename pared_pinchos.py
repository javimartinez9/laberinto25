from pared import Pared

class ParedPinchos(Pared):
    def __init__(self):
        super().__init__()
        self.pincho_preparado = True
        print("🔧 Se ha creado una ParedPinchos con :", self.pincho_preparado)

    def entrar(self, ente):
        if self.pincho_preparado:
            print("🗡️ Te has pinchado con la paredPincho")
            ente.vidas -= 2
            print(f"⚠️  {ente} pierde dos vida. Vidas restantes: {ente.vidas}")
            if ente.vidas <= 0:
                ente.vidas = 0
                ente.estadoEnte.morir(ente)
            self.pincho_preparado = False  # La bomba solo se activa una vez
        else:
            print("La pared pincho ya ha pinchado")
