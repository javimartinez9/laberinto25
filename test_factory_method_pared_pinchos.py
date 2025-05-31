import unittest
from juego import Juego
from creator import CreatorD
from este import Este
from oeste import Oeste
from pared_pinchos import ParedPinchos

class TestFactoryMethodParedPinchos(unittest.TestCase):
    def test_crear_laberinto_con_paredes_pinchos(self):
        juego = Juego()
        fmc = CreatorD()
        laberinto = juego.crearLaberinto2HabFM(fmc)

        hab1 = laberinto.obtenerHabitacion(1)
        hab2 = laberinto.obtenerHabitacion(2)

        # Obtener los elementos en las orientaciones Este y Oeste
        pared_este = hab1.obtenerElementoEnOrientacion(Este())
        pared_oeste = hab2.obtenerElementoEnOrientacion(Oeste())

        # Verificar que ambas paredes son instancias de ParedCohete
        
        self.assertIsInstance(pared_este, ParedPinchos)
        self.assertIsInstance(pared_oeste, ParedPinchos)

        # Verificar que el cohete está listo en ambas paredes
        self.assertTrue(pared_este.pincho_preparado)
        self.assertTrue(pared_oeste.pincho_preparado)

if __name__ == '__main__':
    unittest.main()
