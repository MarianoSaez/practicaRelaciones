from padre import Padre


class Hijo(Padre):
    def __init__(self):
        super().__init__()
        print("Instanciando hijo...")
