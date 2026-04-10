nombres=[]

def agregar_nombres():
    nombre=input("Nombres:")
    nombres.append(nombre)

def mostrar_nombres():
    for nombre in nombres:
        print(nombre)

while True:
 
 print("\n1. Agregar")
 print("\n2. Mostrar")
 print("\n3. Salir")

 opcion=input("opcion:")
 
 if opcion == "1":
    agregar_nombres()

 elif opcion== "2":
    mostrar_nombres()
     
 elif opcion=="3":
    break
    