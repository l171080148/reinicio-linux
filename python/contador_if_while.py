numero_secreto = 10
intentos= 3

while intentos > 0:
    numero = int(input("Adivina el numero el numero secreto:"))
    
    if numero == numero_secreto:
        print("Ganaste!!!")
        break

    else:
        intentos -= 1
        print("Incorrecto, te quedan", intentos, "intentos")

    if intentos == 0:
        print("Perdiste...")    