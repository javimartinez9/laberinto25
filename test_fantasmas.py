import unittest
from unittest.mock import patch, MagicMock
from juego import Juego
from creator import Creator

class TestCrearLaberintoConFantasmasYBichos(unittest.TestCase):
    def test_fantasmas_y_bichos_en_laberinto(self):
        juego = Juego()
        creador = Creator()
        laberinto = juego.crearLaberinto4HabFantasmas(creador)

        # Verificar habitaciones
        self.assertEqual(len(laberinto.hijos), 4)

        # ----------- Fantasmas -----------
        self.assertEqual(len(juego.fantasmas), 4)

        tipos_fantasmas = []
        posiciones_fantasmas = []
        for fantasma in juego.fantasmas:
            self.assertIsNotNone(fantasma.posicion)
            self.assertIn(fantasma.caracter.__str__(), ['-supporter', '-dormilon'])
            self.assertGreaterEqual(fantasma.vidas, 0)
            self.assertGreaterEqual(fantasma.poderMagico, 0)
            tipos_fantasmas.append(fantasma.caracter.__str__())
            posiciones_fantasmas.append(fantasma.posicion.num)

        self.assertEqual(tipos_fantasmas.count('-supporter'), 2)
        self.assertEqual(tipos_fantasmas.count('-dormilon'), 2)
        self.assertSetEqual(set(posiciones_fantasmas), {1, 2, 3, 4})

        # ----------- Bichos -----------
        self.assertEqual(len(juego.bichos), 4)

        posiciones_bichos = []
        for bicho in juego.bichos:
            self.assertIsNotNone(bicho.posicion)
            self.assertIsNotNone(bicho.modo)
            self.assertGreaterEqual(bicho.vidas, 0)
            self.assertGreaterEqual(bicho.poder, 0)
            posiciones_bichos.append(bicho.posicion.num)

        self.assertSetEqual(set(posiciones_bichos), {1, 2, 3, 4})

    @patch('time.sleep', return_value=None)
    def test_lanzar_fantasmas_actuan(self, _):
        juego = Juego()
        creador = Creator()
        juego.crearLaberinto4HabFantasmas(creador)

        for fantasma in juego.fantasmas:
            caracter_mock = MagicMock()
            fantasma.caracter = caracter_mock
            fantasma.vidas = 1
            fantasma.estaVivo = MagicMock(return_value=True)

        juego.lanzarFantasmas()
        # Ahora comprobamos que para cada fantasma, el método actuar fue llamado
        for fantasma in juego.fantasmas:
            fantasma.caracter.actuar.assert_called_with(fantasma)