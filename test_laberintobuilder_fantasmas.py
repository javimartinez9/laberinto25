import unittest
from laberintobuilderconfantasmas import LaberintoBuilderConFantasmas
from director import Director
from fantasma import Fantasma
from supporter import Supporter
from dormilon import Dormilon
from mago import Mago
from activo import Activo
from vago import Vago
import time

class TestLaberintoBuilderConFantasmas(unittest.TestCase):

    def setUp(self):
        # Prepara un JSON mínimo en memoria que simula el archivo con un fantasma
        self.json_mock = {
            "forma": "cuadrado_con_fantasmas",
            "laberinto": [
                {"tipo": "habitacion", "num": 1}
            ],
            "puertas": [],
            "bichos": [],
            "fantasmas": [
                {"caracter": "Supporter", "posicion": 1},
                {"caracter": "Dormilon", "posicion": 1}
            ],
            "magos":[
                {"personalidad":"Activo","posicion":1},
                {"personalidad":"Vago","posicion":1},
            ]
        }

    def test_fabricar_fantasmas(self):
        director = Director()
        director.dict = self.json_mock
        director.iniBuilder()
        director.fabricarLaberinto()
        director.fabricarJuego()
        director.fabricarFantasmas()
        director.fabricarMagos()
        
        juego = director.obtenerJuego()

        self.assertEqual(len(juego.fantasmas), 2)
        self.assertEqual(len(juego.magos),2)

        f1 = juego.fantasmas[0]
        f2 = juego.fantasmas[1]
        
        m1=juego.magos[0]
        m2=juego.magos[1]

        self.assertIsInstance(f1, Fantasma)
        self.assertIsInstance(f2, Fantasma)
        
        self.assertIsInstance(m1,Mago)
        self.assertIsInstance(m2,Mago)

        # Verificar que tienen los caracteres correctos
        self.assertIsInstance(f1.caracter, Supporter)
        self.assertIsInstance(f2.caracter, Dormilon)
        
        self.assertIsInstance(m1.personalidad,Activo)
        self.assertIsInstance(m2.personalidad,Vago)

        # Verificar que ambos están en la habitación 1
        self.assertEqual(f1.posicion.num, 1)
        self.assertEqual(f2.posicion.num, 1)
        
        self.assertEqual(m1.posicion.num,1)
        self.assertEqual(m2.posicion.num,1)
        
        juego.agregar_personaje("pepe")
        juego.lanzarFantasmas()
        juego.lanzarMagos()
        time.sleep(3)
        juego.terminarFantasmas()
        juego.terminarMagos()
        

if __name__ == '__main__':
    unittest.main()

