class Domicilio:
    def __init__(self, calle=None, numero=None):
        self.calle = calle
        self.numero = numero

    def setCalle(self, calle):
        self.calle = calle

    def getCalle(self):
        return self.calle

    def setNumero(self, numero):
        self.numero = numero

    def getNumero(self):
        return self.numero

    def __repr__(self):
        dicc = self.__dict__
        string = ""
        for i in dicc:
            string += f"{i} : {dicc[i]}\n"
        return string
