from decorator import Decorator

class Cohete(Decorator):
    def __init__(self, em):
        super().__init__(em)
        self.cohete_listo=False

    def esCohete(self):
        return True

    def __str__(self):
        return "Soy un cohete"