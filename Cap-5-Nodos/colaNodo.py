import random

class Nodo():
	info, sig =  None, None


class Cola():
	def __init__(self):
		self.frente, self.final = None, None
		self.tamanio = 0


def arribo(cola, info):
	nodo = Nodo()
	nodo.info = dato
	if cola.frente is None:
		cola.frente = nodo
	else:
		cola.final.sig = nodo
	cola.final = nodo
	cola.tamanio += 1


def atencion(cola):
	dato = cola.frente.info
	cola.frente = cola.frente.sig
	if cola.frente is None:
		cola.final = None
	cola.tamanio -= 1
	return dato


def es_vacia(cola):
	return cola.frente is None


def en_frente(cola):
	return cola.frente.info


def tamanio(cola):
	return cola.tamanio


def mover_al_final(cola):
	dato = atencion(cola)
	arribo(cola, dato)
	return dato

def barrido(cola):
	cola_aux = Cola()
	while (not es_vacia(cola)):
		dato = atencion(cola)
		print(dato, end=" ")
		arribo(cola_aux, dato)
	while (not es_vacia(cola_aux)):
		arribo(cola, atencion(cola_aux))


def barrido_mejorado(cola):
	i = 0
	while i < tamanio(cola):
		dato = mover_al_final(cola)
		print(dato, end=' ')
		i+=1

def entrada_prioridad(cola, info):
	if es_vacia(cola):
		arribo(cola, info)
	else:
		nodo = Nodo()
		nodo.info = info
		nodo.sig = cola.frente
		cola.frente = nodo

datos = []
nuevaCola = Cola()

for i in range(40):
	dato = random.randint(0, 20)
	datos.append(dato)
	arribo(nuevaCola, dato)

entrada_prioridad(nuevaCola, 'Funcionó')

print(datos, '\n\n')

barrido(nuevaCola)
