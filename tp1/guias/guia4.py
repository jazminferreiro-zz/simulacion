# -*- coding: utf-8 -*-


def imprimir(l):
    lstr = ','.join(str(e) for e in l)
    print "["+lstr+"]\n"

"""
Dado el sistema de crecimiento exponencial definido por
x t = ax t−1
realice simulaciones en Octave/Matlab o Python generando series temporales para distintos valores del parámetro
a y con condición inicial x 0 = 1. Describa el comportamiento y cómo influye el valor del parámetro en el resultado.
"""

class Sist_exp:
	def __init__(self, x0, a):
		self.current=x0
		self.a=a

	def next(self):
		self.current = self.a*self.current;
		return self.current


def ejercicio6():
    print("                         EJERCICIO6 ")
    x = 1
    parameters = [1,3,6,12,30]
    for a in parameters:
    	serie = Sist_exp(x,a)
    	res = []

    	for i in range(0,100):
    		res.append(serie.next())

    	imprimir(res)

    print "todos tienden a infinito, y el valor del parametro a hace que vaya mas rapido"
    print("__________________________________________________________________________________________")



"""
Dado el sistema de dos variables definido por
x t = ax t−1 + by t−1 ,
y t = cx t−1 + dy t−1 ,
realice simulaciones en Octave/Matlab o Python generando series temporales para distintos valores de los
parámetros a, b, c, d y con condición inicial (x 0 , y 0 ) = (1,1). Muestre los resultados en forma de trayectorias en el
espacio de fases (x, y) . Describa los distintos comportamientos que pueden ser obtenidos y justifique
teóricamente.

"""

class Sist_doble:
	def __init__(self, a,b, c, d, x0, y0):
		self.a = a
		self.b = b
		self.c = c
		self.d = d
		self.currentX = x0
		self.currentY = y0

	def next(self):
		X = self.a*self.currentX + self.b* self.currentY
		Y = self.c *self.currentX + self.d* self.currentY
		self.currentX = X
		self.currentY = Y
		return (self.currentX, self.currentY)

def ejercicio7():
	print("                         EJERCICIO 7 ")
	x = 1
	y = 1
	parameters = [(1,2,3,4),(2,0,11,0),(0,1,0,2),(1,2,0,0),(0,0,1,1), (-1,2,-4,2),(-2,-3,-3,-4)]
	
	for a,b,c,d in parameters:
		print "a: %d" %(a)
		print "b: %d" %(b)
		print "c: %d" %(c)
		print "d: %d" %(d)
		serie = Sist_doble(a,b,c,d,x,y)
		res =[]
   		for i in range(0,100):
   			res.append(serie.next())
   		imprimir(res)

   	print "Oscila si son todos negativos. Se mantiene constante si a=b=0 o si c=d=0. Aumenta para todos los demás"
   	print("__________________________________________________________________________________________")

"""
Simule en Octave/Matlab o Python el comportamiento de la siguiente serie de Fibonacci:
x t = x t−1 + x t−2 , con x 0 = 1, x 1 = 1.
Nota: Convertir primero a un sistema de ecuaciones de diferencias de primer orden con dos variables.
"""

class Fibonacci:
	def __init__(self, x0, x1):
		self.current = x1
		self.prev = x0
	def next(self):
		x = self.current + self.prev
		self.prev = self.current
		self.current = x
		return self.current
		

def ejercicio8():
	print("                         EJERCICIO 8 ")
	x0 = 1
	x1 = 1
	fibonacci = Fibonacci(x0, x1);
	res =[]
   	for i in range(0,100):
   		res.append(fibonacci.next())
   	imprimir(res)
   	print("__________________________________________________________________________________________")

"""
Simule en Octave/Matlab o Python el comportamiento del modelo logístico definido por la siguiente ecuación:

Utilice diferentes valores de los parámetros (a, K) y condiciones iniciales x 0 . Discuta los resultados en el contexto
crecimiento de poblaciones. ¿Hay alguna limitación al crecimiento máximo de la población?
"""
class comportamiento_logistico:
	def __init__(self, a, k, x0):
		self.a = a
		self.k = k
		self.current = x0

	def next(self):
		self.current = self.current * (self.current*((self.a -1) / self.k) +self.a)
		return self.current


def ejercicio8():
	print("                         EJERCICIO 8 ")
	parameters = [(1,1,0), (1,1,1),(2,1,4), (2,3,4)]
	for a,k,x in parameters:
		print "a: %d" %(a)
		print "K: %d" %(k)
		print "x: %d" %(x)

		serie = comportamiento_logistico(a,k,x)
		res =[]
   		for i in range(0,100):
   			res.append(serie.next())
   		imprimir(res)
   	print("__________________________________________________________________________________________")


ejercicio6()
ejercicio7()
ejercicio8()



