from abuelo import Abuelo


class Padre(Abuelo):
    def __init__(self):
        super().__init__()
        print("Instanciando padre...")
