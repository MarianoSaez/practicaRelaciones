from persona import Persona
from domicilio import Domicilio

if __name__ == "__main__":
    per = Persona("Mariano", "Saez", 21)
    dom = Domicilio("Besares", 853)

    per.useDomicilio(dom)
