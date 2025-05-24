import unittest
from unittest.mock import patch, MagicMock
from juego import Juego
from creator import Creator

class TestCrearLaberintoConFantasmasYBichos(unittest.TestCase):
    def test_fantasmas_y_bichos_en_laberinto(self):
        print("\n[Test] Verificando creación del laberinto con fantasmas y bichos")
        juego = Juego()
        creador = Creator()
        laberinto = juego.crearLaberinto4HabFantasmas(creador)

        # Verificar habitaciones
        print(f"[Info] Habitaciones creadas: {len(laberinto.hijos)}")
        self.assertEqual(len(laberinto.hijos), 4)

        # ----------- Fantasmas -----------
        print(f"[Info] Fantasmas creados: {len(juego.fantasmas)}")
        self.assertEqual(len(juego.fantasmas), 4)

        tipos_fantasmas = []
        posiciones_fantasmas = []
        for i, fantasma in enumerate(juego.fantasmas, start=1):
            print(f"[Fantasma {i}] Posición: {fantasma.posicion.num}, Tipo: {fantasma.caracter}")
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
        print(f"[Info] Bichos creados: {len(juego.bichos)}")
        self.assertEqual(len(juego.bichos), 4)

        posiciones_bichos = []
        for i, bicho in enumerate(juego.bichos, start=1):
            print(f"[Bicho {i}] Posición: {bicho.posicion.num}, Modo: {bicho.modo}")
            self.assertIsNotNone(bicho.posicion)
            self.assertIsNotNone(bicho.modo)
            self.assertGreaterEqual(bicho.vidas, 0)
            self.assertGreaterEqual(bicho.poder, 0)
            posiciones_bichos.append(bicho.posicion.num)

        self.assertSetEqual(set(posiciones_bichos), {1, 2, 3, 4})

    @patch('time.sleep', return_value=None)  # Evita ralentizar la prueba
    def test_lanzar_fantasmas_actuan(self, _):
        print("\n[Test] Verificando que los fantasmas actúan")
        juego = Juego()
        creador = Creator()
        juego.crearLaberinto4HabFantasmas(creador)

        for i, fantasma in enumerate(juego.fantasmas, start=1):
            print(f"[Mock] Preparando fantasma {i}")
            caracter_mock = MagicMock()
            fantasma.caracter = caracter_mock
            fantasma.vidas = 1
            fantasma.estaVivo = MagicMock(side_effect=[True, False])  # Simula vida activa y luego termina

            # Simular acción
            fantasma.actua()
            caracter_mock.actuar.assert_called_once_with(fantasma)
            print(f"[OK] Fantasma {i} actuó correctamente")

if __name__ == '__main__':
    unittest.main()
