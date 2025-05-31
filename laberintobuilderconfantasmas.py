from laberinto_builder import LaberintoBuilder
from fantasma import Fantasma
from supporter import Supporter
from dormilon import Dormilon  # si está separado, si no, ignora esto
from mago import Mago
from activo import Activo
from vago import Vago

class LaberintoBuilderConFantasmas(LaberintoBuilder):
    def fabricarFantasmaSupporter(self):
        fantasma=Fantasma()
        fantasma.caracter=Supporter()
        fantasma.iniSupporter()
        return fantasma
    def fabricarFantasmaDormilon(self):
        fantasma=Fantasma()
        fantasma.caracter=Dormilon()
        fantasma.iniDormilon()
        return fantasma
    def fabricarFantasma(self,caracter,posicion):
        if caracter=='Supporter':
            fantasma=self.fabricarFantasmaSupporter()
        if caracter=='Dormilon':
            fantasma=self.fabricarFantasmaDormilon()
            
        hab=self.laberinto.obtenerHabitacion(posicion)
        hab.entrar(fantasma)
        self.juego.agregar_fantasma(fantasma)
        
    def fabricarMagoActivo(self):
        mago=Mago()
        mago.personalidad=Activo()
        mago.iniActivo()
        return mago
    
    def fabricarMagoVago(self):
        mago=Mago()
        mago.personalidad=Vago()
        mago.iniVago()
        return mago
    
    def fabricarMago(self,personalidad,posicion):
        if personalidad=='Activo':
            mago=self.fabricarMagoActivo()
        if personalidad=='Vago':
            mago=self.fabricarMagoVago()
            
        hab=self.laberinto.obtenerHabitacion(posicion)
        hab.entrar(mago)
        self.juego.agregar_mago(mago)
        

        
   
        
   
