def figura(body, letras):
    print("""     __________
    |          |
    |          |
    |          """+ body[0] + """  
    |         """+ body[1] + """
    |         """+ body[2] + """
    |          
    |          
 ___|___     """  +  " ".join(letras))
    
def cuerpoInicial():
     body = ["","",""]
     return body


def cambairCuerpo(error,body):
    if error == 1:
        body[0]='O'
    elif error ==2:
        body[1]=' |'
    elif error ==3:
        body[1]='/|'
    elif error ==4:
        body[1]='/|\\'
    elif error ==5:
        body[2]='/'
    elif error ==6:
        body[2]='/ \\'
    return body


