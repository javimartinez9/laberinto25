import unittest
from juego import Juego
from este import Este
from oeste import Oeste
from creator import Creator
from pinchos import Pinchos

class TestPinchosDecorator(unittest.TestCase):
    def test_paredes_con_pinchos_decorator(self):
        juego = Juego()
        fmb = Creator()
        juego.laberinto = juego.crearLaberinto2HabPinchos(fmb)

        hab1 = juego.obtenerHabitacion(1)
        hab2 = juego.obtenerHabitacion(2)

        pin1 = hab1.obtenerElementoEnOrientacion(Este())
        pin2 = hab2.obtenerElementoEnOrientacion(Oeste())

        # Comprobar que ambos elementos son instancias de Cohete (decorator)
        self.assertIsInstance(pin1, Pinchos)
        self.assertIsInstance(pin2, Pinchos)

        # Comprobar que el atributo cohete_listo está en False
        self.assertTrue(pin1.pincho_preparado)
        self.assertTrue(pin2.pincho_preparado)

        # Comprobar que internamente decoran algo (la pared original)
        self.assertIsNotNone(pin1.em)
        self.assertIsNotNone(pin2.em)

if __name__ == "__main__":
    unittest.main()
