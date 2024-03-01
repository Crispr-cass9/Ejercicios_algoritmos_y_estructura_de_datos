class nodoLista():
    info, sig, prioridad = None, None, 3

class Lista():
    self.inicio = None
    self.tamanio = 0

def insertar(lista, info, prioridad):
    nodo = nodoLista()
    nodo.info = info
    
    if lista.inicio is None or lista.inicio.prioridad > prioridad:
        nodo.sig = lista.inicio
        lista.inicio = nodo
    else:
        anterior = lista.inicio
        posterior = lista.inicio.sig
        while posterior is not none and posterior.prioridad < prioridad:
            anterior = anterior.sig
            posterior = posterior.sig
        nodo.sig = posterior
        anterior.sig = nodo
    lista.tamanio += 1

def es_vacia(lista):
    return lista.inicio is None

def eliminar(lista, elemento):
    