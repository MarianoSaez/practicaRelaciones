class Persona:
    def __init__(self, nombre=None, apellido=None, edad=None):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.domicilio = None

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

    def agregateDomicilio(self, domicilio):
        print("Agregando domicilio...")
        self.domicilio = domicilio

    def __repr__(self):
        dicc = self.__dict__
        string = ""
        for i in dicc:
            string += f"{i} : {dicc[i]}\n"
        return string
