import unittest
from juego import Juego
from este import Este
from oeste import Oeste
from creator import CreatorC
from cohete import Cohete

class TestCoheteDecorator(unittest.TestCase):
    def test_paredes_con_cohete_decorator(self):
        juego = Juego()
        fmb = CreatorC()
        juego.laberinto = juego.crearLaberinto2HabCohete(fmb)

        hab1 = juego.obtenerHabitacion(1)
        hab2 = juego.obtenerHabitacion(2)

        coh1 = hab1.obtenerElementoEnOrientacion(Este())
        coh2 = hab2.obtenerElementoEnOrientacion(Oeste())

        # Comprobar que ambos elementos son instancias de Cohete (decorator)
        self.assertIsInstance(coh1, Cohete)
        self.assertIsInstance(coh2, Cohete)

        # Comprobar que el atributo cohete_listo está en False
        self.assertFalse(coh1.cohete_listo)
        self.assertFalse(coh2.cohete_listo)

        # Comprobar que internamente decoran algo (la pared original)
        self.assertIsNotNone(coh1.em)
        self.assertIsNotNone(coh2.em)

if __name__ == "__main__":
    unittest.main()
