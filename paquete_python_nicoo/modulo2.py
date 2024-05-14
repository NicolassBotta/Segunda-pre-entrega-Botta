import json
def registrar_usuario(database):
    # Solicita al usuario el nombre de usuario y contraseña
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    # Almacena el nombre de usuario y contraseña en el diccionario
    database[nombre_usuario] = contraseña
    print("Usuario registrado exitosamente!")

def mostrar_usuarios(database):
    print("Usuarios registrados:")
    for nombre_usuario, contraseña in database.items():
        print("Nombre de usuario:", nombre_usuario, ", Contraseña:", contraseña)

def login(database):
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    # Comprueba si el nombre de usuario existe en la base de datos y si la contraseña coincide
    if nombre_usuario in database and database[nombre_usuario] == contraseña:
        print("¡Bienvenido,", nombre_usuario + "!")
    else:
        print("Nombre de usuario o contraseña incorrectos.")

# Base de datos que almacena usuarios y contraseñas
def main():
    
    base_de_datos = {}

    while True:
        print("\nBienvenido al sistema de registro y login de usuarios")
        print("1. Registrar nuevo usuario")
        print("2. Mostrar usuarios registrados")
        print("3. Login de usuario")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario(base_de_datos)
        elif opcion == "2":
            mostrar_usuarios(base_de_datos)
        elif opcion == "3":
            login(base_de_datos)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

main()