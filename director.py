import json
from laberinto_builder import LaberintoBuilder
from laberintobuilderconfantasmas import LaberintoBuilderConFantasmas


class Director:
    def __init__(self):
        self.builder = None
        self.dict=None

    def obtenerJuego(self):
        return self.builder.obtenerJuego()
    
    def procesar(self,unArchivo):
        self.leerArchivo(unArchivo)
        self.iniBuilder()
        self.fabricarLaberinto()
        self.fabricarJuego()
        self.fabricarBichos()
        self.fabricarFantasmas()

    def fabricarJuego(self):
        self.builder.fabricarJuego()

    def iniBuilder(self):
        if self.dict['forma']=='cuadrado':
            self.builder=LaberintoBuilder()
        elif self.dict['forma'] == 'cuadrado_con_fantasmas':
            self.builder = LaberintoBuilderConFantasmas()

    def fabricarLaberinto(self):
        self.builder.fabricarLaberinto()
        for each in self.dict['laberinto']:
            self.fabricarLaberintoRecursivo(each,'root')
        
        for each in self.dict['puertas']:
            self.builder.fabricarPuerta(each[0],each[1],each[2],each[3]) 
	
        #recorrer la colección de puertas para fabricarlas
        for each in self.dict['puertas']:
            self.builder.fabricarPuerta(each[0],each[1],each[2],each[3])    
         
    '''
    def fabricarLaberintoRecursivo(self,each,padre):
        bomba_activa=False
        print(each)
        if each['tipo']=='habitacion':
            #print("eaaaach habitacion",each['hijos']['tipo'])
            con=self.builder.fabricarHabitacion(each['num'])
        if each['tipo']=='tunel':
            self.builder.fabricarTunelEn(padre)
        if 'hijos'in each.keys():
            for cadaUno in each['hijos']:
                print("cadauno",cadaUno['tipo'])   
                self.fabricarLaberintoRecursivo(cadaUno,con)
    '''
    
    def fabricarLaberintoRecursivo(self, each, padre):
        if each['tipo'] == 'habitacion':
            tiene_bomba = False
            tiene_cohete=False
            if 'hijos' in each:
                for hijo in each['hijos']:
                    if hijo['tipo']== "cohete":
                        tiene_cohete=True
                    if hijo['tipo'] == "bomba":
                        tiene_bomba = True
                    
            
        # Pasamos el flag al construir la habitación
            hab = self.builder.fabricarHabitacion(each['num'], tiene_bomba,tiene_cohete)

        elif each['tipo'] == 'tunel':
            self.builder.fabricarTunelEn(padre)
            if 'hijos' in each:
                for hijo in each['hijos']:
                    self.fabricarLaberintoRecursivo(hijo, padre)


    def leerArchivo(self, filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            self.dict=data
            return data
        except FileNotFoundError:
            print(f"Error: File not found: {filename}")
            return None
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in file: {filename}")
            return None

    def fabricarBichos(self):
        for each in self.dict['bichos']:
            self.builder.fabricarBicho(each['modo'],each['posicion'])
            
    def fabricarFantasmas(self):
        for each in self.dict['fantasmas']:
            self.builder.fabricarFantasma(each['caracter'],each['posicion'])