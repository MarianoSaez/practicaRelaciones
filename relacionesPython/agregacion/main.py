from persona import Persona
from domicilio import Domicilio

if __name__ == "__main__":
    per = Persona("Mariano", "Saez", 21)
    dom = Domicilio("Dr. Mazza", 1233)

    per.agregateDomicilio(dom)

    print("Nombre: " + per.getNombre())
    print("Apellido: " + per.getApellido())
    print("Edad: " + str(per.getEdad()))
    print("Calle: " + per.getDomicilio().getCalle())
    print("Numero: " + str(per.getDomicilio().getNumero()))

