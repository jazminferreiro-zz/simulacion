from general import *

g = generador.GeneradorLinealCongruente()

class Normal_distribution:
	def __init__(self, media, desvio):
		self.media = media
		self.desvio= desvio
		self.c = (1.0/(self.desvio*math.sqrt(2.0*math.pi)))*math.exp(self.desvio + self.media-0.5)

	def density_function(self, x):
		return (1.0/(self.desvio*math.sqrt(2.0*math.pi)))*math.exp(-(((x-self.media)**2)/(2*(self.desvio)**2)))

	def exponencial_function(self, x):
		return math.exp(-x)

	def X(self, t):
		return self.density_function(t)

	def Y(self, t):
		return self.exponencial_function(t)

	def accept(self, u):
		u2 =  g.generar()
		t  = -math.log(1-u2);
		return (u > (self.X(t)/self.Y(t)*self.c))

	def generate_list(self, n):
		l = []
		u =  g.generar()
		for i in range(n):
			while(not self.accept(u)):
				u =  g.generar()
				print("no se acepto %f" %(u))	
			u3 = g.generar()
			if(u3 >0.5):
				l.append(u)
			else:
				l.append(u)
			u =  g.generar()
		return l

		return l
	def get_media(self):
		return self.media

	def get_moda(self):
		return self.media

	def get_variance(self):
		return self.desvio


print("######################################################")
print("EJERCICIO 4")
print("######################################################")
print("\n")

cant = 100000
uni = Normal_distribution(0,1)
l = uni.generate_list(cant)
generate_histogram(l, "HISTOGRAMA %d NUMEROS GENERADOS" %(cant),'./graficos/ejercicio4-histograma.png');

print("La media teorica de una V.A normal es: %f" %(uni.get_media()))
print("La media es: %f" %(get_media(l)) )
print("La varianza teorica de una v.A normal es: %f" %(uni.get_variance()))
print("La varianza experimental es: %f" %(get_variance(l)))
print("La moda teorica de una v.A normal es: %f" %(uni.get_variance()))
print("La moda es: %f" %(get_modas(l)))
