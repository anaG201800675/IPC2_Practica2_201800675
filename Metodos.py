import Lista
from self import self
lista = Lista.listaCircular

def contacto():
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    tel = input("Ingrese teléfono: ")
    lista.insertar(nombre, apellido, tel)

def buscar():
    num = input("Número que desea ingresar")
    lista.buscar(num)

def graficar():
    pass