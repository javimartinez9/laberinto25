import unittest
from laberintobuilderconfantasmas import LaberintoBuilderConFantasmas
from director import Director
from fantasma import Fantasma
from supporter import Supporter
from dormilon import Dormilon

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
            ]
        }

    def test_fabricar_fantasmas(self):
        director = Director()
        director.dict = self.json_mock
        director.iniBuilder()
        director.fabricarLaberinto()
        director.fabricarJuego()
        director.fabricarFantasmas()
        
        juego = director.obtenerJuego()

        self.assertEqual(len(juego.fantasmas), 2)

        f1 = juego.fantasmas[0]
        f2 = juego.fantasmas[1]

        self.assertIsInstance(f1, Fantasma)
        self.assertIsInstance(f2, Fantasma)

        # Verificar que tienen los caracteres correctos
        self.assertIsInstance(f1.caracter, Supporter)
        self.assertIsInstance(f2.caracter, Dormilon)

        # Verificar que ambos están en la habitación 1
        self.assertEqual(f1.posicion.num, 1)
        self.assertEqual(f2.posicion.num, 1)

if __name__ == '__main__':
    unittest.main()

