from pintadores import pintador
from tools import herramientas
import operator
def inicio():
    error = 0
    body = pintador.cuerpoInicial()
    palabra = 'HOLA'
    print(herramientas.aleatoria(3))

    print('Bienvenido a Hangman')
    while(error <7 and operator.not_(adivino())):
        pintador.figura(body)
        error+=1
        body = pintador.cambairCuerpo(error,body)
    
    if(error == 7):
        print("perdiste")
    elif(adivino()):
        print("adivinaste")


def adivino():

    return False