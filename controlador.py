from pintadores import pintador
from tools import herramientas
import operator

def inicio():
    error = 0
    aciertos = 0
    body = pintador.cuerpoInicial()
    palabra = 'HOLA'
    letras = definirletras(palabra)
    print(herramientas.aleatoria(3))
    
    print('Bienvenido a Hangman')
    while(error <7 and operator.not_(termino(aciertos, palabra))):
        pintador.figura(body)
        print ("           " +"".join(letras))
        letra = input("Ingrese una leta: ")
        letra = herramientas.validarLetra(letra)
        if adivino(letra, palabra, letras):
            print("adivinaste")
            aciertos+=1
        else:
            error+=1
        
        body = pintador.cambairCuerpo(error,body)
    
    pintador.figura(body)
    print ("           " +"".join(letras))

    if(error == 7):
        print("perdiste")
    elif(adivino(letra, palabra, letras)):
        print("adivinaste")


def adivino(letra, palabra, letras):
    for caracter in palabra:
        if caracter == letra:
            mostraLetra(palabra,letra, letras)
            return True
    return False

def termino(aciertos, palabra):
    if aciertos < len(palabra):
        return False
    elif aciertos == len(palabra):
        return True
    
def mostraLetra(palabra,letra, letras):
    contador = 0
    for caracter in palabra:
        if caracter == letra:
            letras[contador] =caracter + " "
        contador +=1 

def definirletras(palabra):
    letras=[]
    for i in range(0,len(palabra)):
        letras.append("_ ") 
    return letras


