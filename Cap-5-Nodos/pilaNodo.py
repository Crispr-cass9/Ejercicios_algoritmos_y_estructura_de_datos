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
		print(ultimo)
		apilar(pila_aux, ultimo)
	while not pila_vacia(pila_aux):
		apilar(pila, desapilar(pila_aux))


# nuevaPila = Pila()
# apilar(nuevaPila, 'Hola')
# apilar(nuevaPila, 'Mundo')
# apilar(nuevaPila, 'dato random')

# barrido(nuevaPila)
