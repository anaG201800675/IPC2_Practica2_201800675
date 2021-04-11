from graphviz import Digraph
from self import self

class contacto:
    def __init__(self, nombre, apellido, tel):
        self.nombre = nombre
        self.m = tel
        self.n = apellido

class nodo:
    def __init__(self, nombre, apellido, tel):
        self.nombre = nombre
        self.n = apellido
        self.next = None

    def getElemento(self):
        return print("nombre: ", self.nombre, "apellido: ", self.apellido, 'tel: ', self.tel)

    def getNodo(self):
        return self.dato

class listaCircular(object):
    def __init__(self):
        self.head = None #nodo primero
        self.last = None #nodo último

    def isEmpty(self):
        if self.head == None:
            return True

    def insertar(self, nombre, apellido, tel):
        nuevo = nodo(nombre, apellido, tel)
        if self.isEmpty() == True:
            self.head = self.last = nuevo
            self.last.next = self.head
        else:
            self.last.next = nuevo
            self.last = nuevo
            self.last.next = self.head

    def imprimir(self):
        if self.isEmpty() == True:
            print("lista vacía")
        else:
            validar = True
            temp = self.head
            while(validar):
                print(temp.getElemento())
                if temp == self.last:
                    validar = False
                else:
                    temp = temp.next


    def buscar(self, tel):
        temp = self.head
        i = 1
        flag = False
        if self.isEmpty() == True:
            print("Lista vacía")
        else:
            while True:
                if temp.tel == tel:
                    flag = True
                    break
                temp = temp.next
                i = i + 1
                if temp == self.head:
                    break
            if flag:
                print("Posición: " + str(i))
            else:
                print("Ingrese un elemento que si exista")

    def getDatos(self):
        nodo = self.head
        while nodo.next != None:
            return nodo.getNodo(), print("se obtuvieron los datos")

    def graph(self, nombre):
        pass