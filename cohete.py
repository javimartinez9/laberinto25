from decorator import Decorator

class Cohete(Decorator):
    def __init__(self, em):
        super().__init__(em)
        self.cohete_listo=True

    def esCohete(self):
        return True
    
    def entrar(self, ente):
        # Primero se ejecuta la lógica original del elemento decorado
        self.em.entrar(ente)

        # Ahora la lógica del cohete
        if self.cohete_listo:
            print("🚀 Te ha dado un cohete (decorador)")
            ente.vidas -= 1
            print(f"⚠️  {ente} pierde una vida. Vidas restantes: {ente.vidas}")
            if ente.vidas <= 0:
                ente.vidas = 0
                ente.estadoEnte.morir(ente)
            self.cohete_listo = False
        else:
            print("El cohete del decorador ya se usó")

    def __str__(self):
        return "Soy un cohete"