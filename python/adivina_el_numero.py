def pedir_numero():
    return int(input(" Adivina el numero:"))

def verificar(numero,secreto):
    return numero== secreto

numero_secreto=7 
intentos=3

while intentos>0:
    numero=pedir_numero()

    if verificar(numero,numero_secreto):
        print(" Ganaste!!")
        break

    else:
        intentos-=1
        print("ncorrecto, te quedan",intentos)

    if intentos==0:
        Print("Perdiste...")
        

    
