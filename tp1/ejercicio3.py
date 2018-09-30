from util.general import *

class Uniform_distribution:
	def __init__(self, a, b):
		if(a > b):
			raise ValueError('[a,b] must be an interval.')
		self.a = a
		self.b = b

	def generate(self,u):
		x = u*(self.b-self.a)+self.a
		return x

	def generate_list(self, n):
		generator = generador.GeneradorLinealCongruente()
		l = generator.generar_lista(n)
		for i in range(n):
			l[i] = self.generate(l[i])

		return l
	def get_media(self):
		return (self.b+self.a)/2.0
	def get_variance(self):
		return ((self.b+self.a)**2)/12.0
 

class Normal_standar:
	def __init__(self):
		self.media = 0
		self.desvio= 1
		self.uniform = Uniform_distribution(0,1.0/math.sqrt(2.0*math.pi))

	def density_function(self, x):
		return (1.0/(math.sqrt(2.0*math.pi)))*math.exp(-(x**2)/2)


	def generate_list(self, n):
		l = self.uniform.generate_list(n)
		g = generador.GeneradorLinealCongruente()
		for i in range(n):
			x = self.generate(l[i])
			u2 = g.generar()
			if(u2>0.5):
				l[i] = x
			else:
				l[i] = -x
		return l

	def generate(self,u):
		limit = 1.0/math.sqrt(2.0*math.pi)
		if( u < 0 or u > limit):
			raise ValueError(' u =%d must be smaller than %f.' %(u, limit))

		x = math.sqrt(-2.0*math.log(u*math.sqrt(2.0*math.pi)))
		return x


	def get_media(self):
		return self.media

	def get_moda(self):
		return self.media

	def get_variance(self):
		return self.desvio

if __name__ == '__main__':
	print("######################################################")
	print("EJERCICIO 3")
	print("######################################################")
	print("\n")

	cant = 10000
	normal = Normal_standar()
	l = normal.generate_list(cant)
	generate_histogram(l, "HISTOGRAMA %d NUMEROS GENERADOS" %(cant),'./graficos/ejercicio3-histograma.png');

	print("La media teorica de una V.A uniforme es: %f" %(normal.get_media()))
	print("La media es: %f" %(get_media(l)) )
	print("La varianza teorica de una v.A uniforme es: %f" %(normal.get_variance()))
	print("La varianza experimental es: %f" %(get_variance(l)))
	print("La moda es: %f" %(get_modas(l)))
