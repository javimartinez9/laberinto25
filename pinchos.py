from decorator import Decorator

class Pinchos(Decorator):
    def __init__(self, em):
        super().__init__(em)
        self.pincho_preparado=True

    def esPinchos(self):
        return True
    
    def entrar(self, ente):
        # Primero se ejecuta la lógica original del elemento decorado
        self.em.entrar(ente)

        # Ahora la lógica del cohete
        if self.pincho_preparado:
            print("🗡️ Te ha dado un pincho(decorador)")
            ente.vidas -= 2
            print(f"⚠️  {ente} pierde una vida. Vidas restantes: {ente.vidas}")
            if ente.vidas <= 0:
                ente.vidas = 0
                ente.estadoEnte.morir(ente)
            self.pincho_preparado = False
        else:
            print("El pincho del decorador ya se usó")

    def __str__(self):
        return "Soy un pincho"