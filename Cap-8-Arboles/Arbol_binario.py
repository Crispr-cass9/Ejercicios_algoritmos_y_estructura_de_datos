class nodoArborl():
    def __init__(self, info):
        self.izq = None
        self.der = None
        self.info = info
        self.altura = 0


def eliminar_nodo(raiz,clave):
    # Elimina un elemento de un arbol y lo devuelve
    x = None
    if raiz is not None:
        
        if clave < raiz.info:
            raiz, x = eliminar_nodo(raiz.izq)
        
        elif clave > raiz.info:
            raiz, x = eliminar_nodo(raiz.der)
        
        else:
            x = raiz.info
            if raiz.izq is None:
                raiz = raiz.der
            elif raiz.der is None:
                raiz = raiz.izq
            else:
                raiz.izq, aux = reemplazar(raiz.izq)
                raiz.info = aux.info
    raiz = balancear(raiz)
    actualizarAltura(raiz)
    return raiz, x

#Siempre que se inserta un nodo se agregará como una hoja, no como un nodo intermedio 

def insertar_nodo(raiz, dato):
    if raiz is None:
        raiz = nodoArborl(dato)
    elif dato < raiz.info:
        raiz.izq = insertar_nodo(raiz.izq, dato)
    else:
        raiz.der = insertar_nodo(raiz.der, dato)
    raiz = balancear(raiz)
    actualizarAltura(raiz)
    return raiz
    
def es_arbol_vacio(raiz):
    return raiz is None

def remplazar(raiz):
    #Determina el nodo que reemplazará al que se elimina
    aux = None
    if raiz.der is None:
        aux = raiz
        raiz = raiz.izq
    else:
        raiz.der, aux = remplazar(raiz.der)
    
    return raiz, aux


def buscar(raiz, clave):

    pos = None
    if raiz.info == clave:
        pos = raiz
    elif clave < raiz.info:
        pos = buscar(raiz.izq, clave)
    else:
        pos = buscar(raiz.der, clave)
    return pos


def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izq)
        print(raiz.info)
        inorden(raiz.der)


def preorden(raiz):
    if raiz is not None:
        print(raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)


def postorden(raiz):
    if raiz is not None:
        inorden(raiz.der)
        print(raiz.info)
        inorden(raiz.izq)

def altura(raiz):
    if raiz is None:
        return -1
    else:
        return raiz.altura

def actualizarAltura(raiz):
    if raiz is not None:
        alt_izq = altura(raiz.izq)
        alt_der = altura(raiz.der)
    raiz.altura = (alt_izq if alt_izq > alt_der else alt_der) +1 
    
def rotar_simple(raiz, control):
    if control:
        aux = raiz.izq
        raiz.izq = aux.der
        aux.der = raiz
    else:
        aux = raiz.der
        aux.der = aux.izq
        aux.izq = raiz
    actualizarAltura(raiz)
    actualizarAltura(aux)
    raiz = aux
    return raiz

def rotar_doble(raiz, control):
    if control:
        raiz.izq = rotar_simple(raiz.izq, False)
        raiz = rotar_simple(raiz, True)
    else:
        raiz.der = rotar_simple(raiz.der, True)
        raiz = rotar_simple(raiz, False)
    return raiz

def balancear(raiz):
    if raiz is not None:
        if altura(raiz.izq)-altura(raiz.der) == 2:
            if altura(raiz.izq.izq) >= altura(raiz.izq.der):
                raiz = rotar_simple(raiz, True)
            else:
                raiz = rotar_doble(raiz, True)
        
        elif altura(raiz.der)-altura(raiz.izq) == 2:
            if altura(raiz.der.der) >= altura(raiz.der.izq):
                raiz = rotar_simple(raiz, False)
            else:
                raiz = rotar_doble(raiz, False)
    return raiz 

    