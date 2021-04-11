import Metodos

def menu():
    print("1. Ingresar nuevo contacto\n2. Buscar contacto\n3. Visualizar agenda")
    entrada = input("Ingrese una opción: ")
    if entrada == "1":
        Metodos.contacto()


menu()