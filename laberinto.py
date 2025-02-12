class ElementoMapa:
    def __init__(self):
        pass

class Habitacion(ElementoMapa):
    def __init__(self, num):
        super().__init__()
        self.num = num
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None

class Pared(ElementoMapa):
    def __init__(self):
        super().__init__()

class Puerta(ElementoMapa):
    def __init__(self, lado1, lado2):
        super().__init__()
        self.abierta = False
        self.lado1 = lado1
        self.lado2 = lado2

    def abrir(self):
        self.abierta = True
        print(f"Puerta entre habitación {self.lado1.num} y {self.lado2.num} abierta.")

    def cerrar(self):
        self.abierta = False
        print(f"Puerta entre habitación {self.lado1.num} y {self.lado2.num} cerrada.")
        
   


class Laberinto(ElementoMapa):
    def __init__(self):
        super().__init__()
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)
        print(f"Habitación {habitacion.num} agregada al laberinto.")


    def conectar_habitaciones(self, hab1, hab2, direccion):
        if direccion == 'norte':
            hab1.norte = hab2
            hab2.sur = hab1
        elif direccion == 'sur':
            hab1.sur = hab2
            hab2.norte = hab1
        elif direccion == 'este':
            hab1.este = hab2
            hab2.oeste = hab1
        elif direccion == 'oeste':
            hab1.oeste = hab2
            hab2.este = hab1
            
        print(f"Habitación {hab1.num} conectada con la habitación {hab2.num} al {direccion}.")
        
    def mostrar_laberinto(self):
        for hab in self.habitaciones:
            print(f"Habitación {hab.num}:")
            print(f"  Norte -> {hab.norte.num if hab.norte else 'Nada'}")
            print(f"  Sur -> {hab.sur.num if hab.sur else 'Nada'}")
            print(f"  Este -> {hab.este.num if hab.este else 'Nada'}")
            print(f"  Oeste -> {hab.oeste.num if hab.oeste else 'Nada'}")

class Juego:
    def __init__(self, laberinto):
        self.laberinto = laberinto

    def jugar(self):
        # Lógica del juego
        pass

# Ejemplo de uso
laberinto = Laberinto()

# Crear habitaciones
hab1 = Habitacion(1)
hab2 = Habitacion(2)
hab3 = Habitacion(3)

# Agregar habitaciones al laberinto
laberinto.agregar_habitacion(hab1)
laberinto.agregar_habitacion(hab2)
laberinto.agregar_habitacion(hab3)

# Conectar habitaciones
laberinto.conectar_habitaciones(hab1, hab2, 'norte')
laberinto.conectar_habitaciones(hab2, hab3, 'este')

# Crear puertas
puerta1 = Puerta(hab1, hab2)
puerta2 = Puerta(hab2, hab3)

# Abrir puertas
puerta1.abrir()
puerta2.abrir()

# Crear el juego
juego = Juego(laberinto)

# Jugar
juego.jugar()
laberinto.mostrar_laberinto()