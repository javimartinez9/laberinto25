from laberinto_builder import LaberintoBuilder
from fanstasma import Fantasma
from supporter import Supporter
from dormilon import Dormilon  # si está separado, si no, ignora esto

class LaberintoBuilderConFantasmas(LaberintoBuilder):
    def fabricarFantasmaSupporter(self):
        fantasma=Fantasma()
        fantasma.caracter=Supporter()
        fantasma.iniSupporter()
        return fantasma
    def fabricarFantasmaDormilon(self):
        fantasma=Fantasma()
        fantasma.caracter=Dormilon()
        fantasma.iniDormilon
        return fantasma
    def fabricarFantasma(self, caracter, posicion):
        fantasma = Fantasma()
        
        if caracter == 'supporter':
            fantasma.caracter = Supporter()
            fantasma.iniSupporter()
        elif caracter == 'dormilon':
            fantasma.caracter = Dormilon()
            fantasma.iniDormilon()
        else:
            raise ValueError(f"Tipo de fantasma desconocido: {caracter}")
        
        hab = self.laberinto.obtenerHabitacion(posicion)
        hab.entrar(fantasma)
        self.juego.agregar_fantasma(fantasma)
        
   
        
   
