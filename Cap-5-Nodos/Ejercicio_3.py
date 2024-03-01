#Eliminar de una pila todos los elementos impares, es decir que en la misma solo queden números pares
import random

class Nuevo_nodo():
	def __init__(self):
		info, sig = None, None


class Pila():
	def __init__(self):
		self.cima = None
		self.tamanio = 0


def apilar(pila, informacion):
	nodo = Nuevo_nodo()
	nodo.sig = pila.cima
	nodo.info = informacion
	pila.cima = nodo
	pila.tamanio +=1

def desapilar(pila):
	info = pila.cima.info
	pila.cima = pila.cima.sig
	pila.tamanio -= 1
	return info


def pila_vacia(pila):
	return pila.cima is None


def en_cima(pila):
	if not pila_vacia:
		return pila.cima.info
	else:
		return None

def tamanio(pila):
    return pila.tamanio


def barrido(pila):
    pila_aux= Pila()
    while not pila_vacia(pila):
        ultimo = desapilar(pila)
        apilar(pila_aux, ultimo)
    while not pila_vacia(pila_aux):
        apilar(pila, desapilar(pila_aux))


def eliminar_impares(pila):
    pila_aux = Pila()
    while not pila_vacia(pila):
        elemento = desapilar(pila)
        if elemento%2==0:
            apilar(pila_aux, elemento)
    while not pila_vacia(pila_aux):
        print(pila_aux.cima.info, end=' ')
        apilar(pila, desapilar(pila_aux))
    return pila

 
nuevaPila= Pila()

datos = []

for i in range(220):
    numero = random.randint(0, 100)
    datos.append(numero)

datos.sort()

for dato in datos:
    apilar(nuevaPila, dato)

print('\nDatos de entrada \n\n', datos, '\n\nDatos de salida\n')
eliminar_impares(nuevaPila) 