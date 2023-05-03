import random
def pedirDato(mensaje):
    dato = input(mensaje)
    return mensaje

def perdirnumero(mensaje):
    numero = input(mensaje)
    return numero

def aleatoria(cantidad):
    numero = random.randint(0,cantidad-1)
    return numero