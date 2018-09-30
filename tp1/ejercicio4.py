from util.general import *
from ejercicio2 import Exponential_distribution


class Normal:
	def __init__(self, media, desvio):
		if(desvio == 0):
			raise ValueError('descio must be positive.')
		self.media = media
		self.desvio= desvio
		self.c = math.sqrt(math.exp(1)/2.0*math.pi)
		self.exponencial = Exponential_distribution(1)
		self.uniform = generador.GeneradorLinealCongruente()

	def density_function(self, x):
		return (1.0/(math.sqrt(2.0*math.pi)))*math.exp(-(x**2)/2)

	def exponencial_function(self, x):
		return self.exponencial.distribution(x)

	def X(self, t):
		return self.density_function(t)

	def Y(self, t):
		return self.exponencial_function(t)

	def accept(self, u):
		u2 =  self.uniform.generar()
		t  = self.exponencial.generate(u2)
		return (u < (self.X(t)/(self.Y(t)*self.c)))

	def generate_list(self, n):
		l = []
		u =  self.uniform.generar()
		for i in range(n):
			while(not self.accept(u)):
				u =  self.uniform.generar()
				print("no se acepto %f" %(u*self.desvio+self.media))	
			u3 = self.uniform.generar()
			if(u3 >0.5):
				l.append(u*self.desvio+self.media)
			else:
				l.append(-u*self.desvio+self.media)
			u =  self.uniform.generar()
		return l

		return l
	def get_media(self):
		return self.media

	def get_moda(self):
		return self.media

	def get_variance(self):
		return self.desvio

if __name__ == '__main__':
	print("######################################################")
	print("EJERCICIO 4")
	print("######################################################")
	print("\n")

	cant = 100000
	uni = Normal(35,5)
	l = uni.generate_list(cant)
	generate_histogram(l, "HISTOGRAMA %d NUMEROS GENERADOS" %(cant),'./graficos/ejercicio4-histograma.png');

	print("La media teorica de una V.A normal es: %f" %(uni.get_media()))
	print("La media es: %f" %(get_media(l)) )
	print("La varianza teorica de una v.A normal es: %f" %(uni.get_variance()))
	print("La varianza experimental es: %f" %(get_variance(l)))
	print("La moda teorica de una v.A normal es: %f" %(uni.get_variance()))
	print("La moda es: %f" %(get_modas(l)))
