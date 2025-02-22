# Elementos base del mapa
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
            print(f"  Norte -> {hab.norte.num if isinstance(hab.norte, Habitacion) else 'Puerta'}")
            print(f"  Sur -> {hab.sur.num if isinstance(hab.sur, Habitacion) else 'Puerta'}")
            print(f"  Este -> {hab.este.num if isinstance(hab.este, Habitacion) else 'Puerta'}")
            print(f"  Oeste -> {hab.oeste.num if isinstance(hab.oeste, Habitacion) else 'Puerta'}")
# Interfaz de Creador para el patrón Factory Method
class CreadorLaberinto:
    def fabricarHabitacion(self, num):
        return Habitacion(num)

    def fabricarPuerta(self, lado1, lado2):
        return Puerta(lado1, lado2)

    def fabricarLaberinto(self):
        return Laberinto()

    def fabricarPared(self):
        return Pared()

    def fabricarJuego(self):
        return Juego(self.fabricarLaberinto())

# Clase Juego que usa el CreadorLaberinto
class Juego:
    def __init__(self, creador_laberinto=None):
        self.creador_laberinto = creador_laberinto
        self.laberinto = None
        self.usa_factory = True if creador_laberinto else False

    def crear_laberinto_con_factory(self):
        # Lógica con Factory Method
        hab1 = self.creador_laberinto.fabricarHabitacion(1)
        hab2 = self.creador_laberinto.fabricarHabitacion(2)
        hab3 = self.creador_laberinto.fabricarHabitacion(3)
        puerta1 = self.creador_laberinto.fabricarPuerta(hab1, hab2)
        puerta2 = self.creador_laberinto.fabricarPuerta(hab2, hab3)
        pared = self.creador_laberinto.fabricarPared()
        hab1.sur = puerta1
        hab2.norte = puerta1
        hab2.sur = puerta2
        hab3.norte = puerta2
        self.laberinto = self.creador_laberinto.fabricarLaberinto()
        self.laberinto.agregar_habitacion(hab1)
        self.laberinto.agregar_habitacion(hab2)
        self.laberinto.agregar_habitacion(hab3)

        # Mostrar el laberinto
        self.laberinto.mostrar_laberinto()

    def crear_laberinto_sin_factory(self):
        # Crear laberinto directamente (sin Factory Method)
        hab1 = Habitacion(1)
        hab1.este = Pared()
        hab1.oeste = Pared()
        hab1.norte = Pared()

        hab2 = Habitacion(2)
        hab2.este = Pared()
        hab2.oeste = Pared()
        hab2.sur = Pared()

        # Crear puerta
        puerta = Puerta(hab1, hab2)

        # Conectar las habitaciones con la puerta
        hab1.sur = puerta
        hab2.norte = puerta

        # Crear el laberinto y agregar las habitaciones
        self.laberinto = Laberinto()
        self.laberinto.agregar_habitacion(hab1)
        self.laberinto.agregar_habitacion(hab2)

        # Mostrar el laberinto
        self.laberinto.mostrar_laberinto()

    def jugar_con_factory(self):
        # Lógica del juego con Factory Method
        print("El juego ha comenzado con Factory Method.")
        self.crear_laberinto_con_factory()

    def jugar_sin_factory(self):
        # Lógica del juego sin Factory Method
        print("El juego ha comenzado sin Factory Method.")
        self.crear_laberinto_sin_factory()


# Si usas Factory Method
creador = CreadorLaberinto()  # Creador para Factory Method
juego_con_factory = Juego(creador_laberinto=creador)
juego_con_factory.jugar_con_factory()

# Si no usas Factory Method
juego_sin_factory = Juego(creador_laberinto=None)
juego_sin_factory.jugar_sin_factory()

