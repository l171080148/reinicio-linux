from funciones import registrar_usuario, mostrar_usuarios

while True:
    print("\n1. Registrar")
    print("2. Mostrar")
    print("3. Salir")

    opcion = input("Opcion: ")

    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        mostrar_usuarios()
    elif opcion == "3":
        break
