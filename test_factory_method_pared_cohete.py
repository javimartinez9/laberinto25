import unittest
from juego import Juego
from creator import CreatorC
from este import Este
from oeste import Oeste
from pared_cohete import ParedCohete

class TestFactoryMethodParedCohete(unittest.TestCase):
    def test_crear_laberinto_con_paredes_cohete(self):
        juego = Juego()
        fmc = CreatorC()
        laberinto = juego.crearLaberinto2HabCoheteFM(fmc)

        hab1 = laberinto.obtenerHabitacion(1)
        hab2 = laberinto.obtenerHabitacion(2)

        # Obtener los elementos en las orientaciones Este y Oeste
        pared_este = hab1.obtenerElementoEnOrientacion(Este())
        pared_oeste = hab2.obtenerElementoEnOrientacion(Oeste())

        # Verificar que ambas paredes son instancias de ParedCohete
        
        self.assertIsInstance(pared_este, ParedCohete)
        self.assertIsInstance(pared_oeste, ParedCohete)

        # Verificar que el cohete está listo en ambas paredes
        self.assertTrue(pared_este.cohete_listo)
        self.assertTrue(pared_oeste.cohete_listo)

if __name__ == '__main__':
    unittest.main()
