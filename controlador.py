from pintadores import pintador
from tools import herramientas
import operator

palabra="" 
letra= ""
body = ""
letras = []

def inicio(): 
    global letra
    error = 0
    body = pintador.cuerpoInicial()
    palabrasRandom()
    definirletras()
    print(herramientas.aleatoria(3))
    
    print('Bienvenido a Hangman')
    while(error < 6 and operator.not_( termino())):
        pintador.figura(body, letras)
        letra = input("Ingrese una letra: ")
        letra = herramientas.validarLetra(letra)
        if yaHaAdivinado():
            print("ya has adivinado esta Letra")
        else:
            if adivino():
                print("adivinaste")
            else:
                print("Xx__FALLASTE__xX")
                error+=1
        body = pintador.cambairCuerpo(error,body)
    pintador.figura(body, letras)

    if(error == 6):
        print("PERDISTE. La palabra era " + palabra)
    elif(adivino()):
        print("adivinaste")

def yaHaAdivinado():
    i=0
    for caracter in letras:
        if caracter== letra:
            return True
        i+=1
    return False

def adivino():
    for caracter in palabra:
        if caracter == letra:
            mostraLetra()
            return True
    return False

def termino():
    if "".join(letras)==palabra:
        return True
    else:
        return False

def mostraLetra():
    contador = 0
    for caracter in palabra:
        if caracter == letra:
            letras[contador] =caracter
        contador +=1 

def definirletras():
    global letras
    for i in range(0,len(palabra)):
       letras.append("_")

def palabrasRandom():
    global palabra
    palabras = ['HOLA',"QUIEN","GATO","GALGO","PAPA"]
    palabra = palabras[herramientas.aleatoria(len(palabras))]
    print("la palabra es " + palabra)
    return palabra


