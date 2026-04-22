usuarios = []

def registrar_usuario():
    nombre = input("Nombre: ")

    try:
        edad = int(input("Edad: "))
    except:
        print("Edad invalidad")
        return
    
    usuario ={
        "nombre":nombre,
        "edad":edad
    }

    usuarios.append(usuario)
     
def mostrar_usuarios():
    for usuario in usuarios:
        print("Nombre:",
         usuario["nombre"], "| Edad: ",
        usuario["edad"])
        