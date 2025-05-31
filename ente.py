from estado_ente import Vivo, Muerto

class Ente:
    def __init__(self):
        self.vidas = None
        self.poder = None
        self.posicion = None
        self.juego = None
        self.estadoEnte = Vivo()

    def clonarLaberinto(self,tunel):
        pass

    def esAtacadoPor(self, atacante):
        print(f"Ataque: {self} es atacado")
        self.vidas -= atacante.poder
        if self.vidas < 0:
            self.vidas = 0  # 👈 evita valores negativos
        print(f"Vidas restantes: {self.vidas}")
        if self.vidas == 0:
            print(f"El ente ha muerto")
            self.estadoEnte.morir(self)
    

    def esSupporteadoPor(self, supporter):
        print(f"Support time: {self} es supporteado")
        self.poder+=supporter.poderMagico
        print("Poder del personaje despues del support :",self.poder)
        
    def esSupporteadoPorMago(self, supporter):
        print(f"Support time: {self} es supporteado")
        self.poder+=supporter.poderMagico
        print("Poder del personaje despues del support del mago :",self.poder)

class Personaje(Ente):
    def __init__(self, vidas, poder, juego, nombre, posicion):
        super().__init__()
        self.nombre = nombre
        self.vidas = vidas
        self.juego = juego
        self.poder=poder
        self.posicion=posicion

    def clonarLaberinto(self,tunel):
        tunel.puedeClonarLaberinto()

    def atacar(self):
        #while self.estaVivo:
            self.juego.buscarBicho()
        
    def caminar(self):
            print(self.posicion)
            self.posicion.caminarAleatorio(self)
            print("caminando personaje")
            
    def estaVivo(self):
        return self.vidas > 0
    
    def __str__(self):
        return str(self.nombre)