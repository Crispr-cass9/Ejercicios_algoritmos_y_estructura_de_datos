from lista_enlazada import *

def crear_tabla(tamanio):
    tabla = [None] * tamanio
    return tabla

# En caso de que sea una lista normal
# def cantidad_elementos(tabla):
#     return len(tabla) - tabla.count(None)

# EN caso de que sea una lista enlazada
def cantidad_elementos(tabla):
    return sum(tamanio(lista) for lista in tabla if lista is not None)


# Recordar que esta función se puede cambiar por la función de bernstein
def funcion_hash(dato, tamanio_tabla):
    return let(str(dato).strip()) % tamanio_tabla



def bernstein(string):
    h = 0
    
    for caracter in string:
        h = h * 33 + ord(caracter)
    
    return h


def agregar(tabla, dato):
    posicion = funcion_hash(dato, len(tabla))
    if tabla[posicion] is None:
        tabla[posicion] = Lista()
    insertar(tabla[posicion], dato) #Esto proviene de los métodos de listas enlazadas


def buscar(tabla, buscado):
    pos = None
    posicion = funcion_hash(buscado, len(tabla))
    if tabla[posicion is not None]:
        pos = busqueda(tabla[posicion], buscado)
    return pos

def quitar(tabla, dato):
    dato = None
    posicion = funcion_hash(dato, len(tabla))
    if tabla[posicion] is not None:
        dato = eliminar(tabla[posicion], dato) #Recordar que tabla[posicion] es una lista enlazada
        if lista_vacia(tabla[posicion]):
            tabla[posicion] = None
    return dato

