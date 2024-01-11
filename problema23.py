#Define una clase llamada "LinkedList" que represente una lista enlazada. Agrega métodos para insertar un elemento al principio 
#y al final de la lista, y para imprimir la lista.

class LinkedList:
    def __init__(self):
        self.head = None

    def insertar_al_principio(self, elemento):
        nuevo_nodo = Node(elemento)
        nuevo_nodo.next = self.head
        self.head = nuevo_nodo

    def insertar_al_final(self, elemento):
        nuevo_nodo = Node(elemento)
        if self.head is None:
            self.head = nuevo_nodo
        else:
            nodo_actual = self.head
            while nodo_actual.next is not None:
                nodo_actual = nodo_actual.next
            nodo_actual.next = nuevo_nodo

    def imprimir_lista(self):
        nodo_actual = self.head
        while nodo_actual is not None:
            print(nodo_actual.data)
            nodo_actual = nodo_actual.next

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

linked_list = LinkedList()

linked_list.insertar_al_principio(1)
linked_list.insertar_al_principio(2)
linked_list.insertar_al_final(3)

linked_list.imprimir_lista()