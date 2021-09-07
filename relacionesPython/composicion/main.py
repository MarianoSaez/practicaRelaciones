from persona import Persona
from domicilio import Domicilio

if __name__ == "__main__":
    per = Persona("Mariano", "Saez", 21, "Dr. Mazza", 1233)

    print("Nombre: " + per.getNombre())
    print("Apellido: " + per.getApellido())
    print("Edad: " + str(per.getEdad()))
    print("Calle: " + per.getDomicilio().getCalle())
    print("Numero: " + str(per.getDomicilio().getNumero()))

