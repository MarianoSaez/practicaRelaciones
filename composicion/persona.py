from domicilio import Domicilio


class Persona:
    def __init__(self, nombre=None, apellido=None, edad=None, calle=None, numero=None):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        print("Componiendo domicilio desde persona...")
        self.domicilio = Domicilio(calle, numero)

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def getApellido(self):
        return self.apellido

    def setEdad(self, edad):
        self.edad = edad

    def getEdad(self):
        return self.edad

    def setDomicilio(self, dom):
        self.domicilio = dom

    def getDomicilio(self):
        return self.domicilio

    def __repr__(self):
        dicc = self.__dict__
        string = ""
        for i in dicc:
            string += f"{i} : {dicc[i]}\n"
        return string
