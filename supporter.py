import time
from caracter import Caracter
class Supporter(Caracter):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return "-supporter"