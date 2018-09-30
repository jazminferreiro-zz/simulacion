from general import *
 

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


if __name__ == '__main__':
	print("######################################################")
	print("EJERCICIO 3")
	print("######################################################")
	print("\n")

	cant = 10000
	uni = Uniform_distribution(0,1)
	l = uni.generate_list(cant)
	generate_histogram(l, "HISTOGRAMA %d NUMEROS GENERADOS" %(cant),'./graficos/ejercicio3-histograma.png');

	print("La media teorica de una V.A uniforme es: %f" %(uni.get_media()))
	print("La media es: %f" %(get_media(l)) )
	print("La varianza teorica de una v.A uniforme es: %f" %(uni.get_variance()))
	print("La varianza experimental es: %f" %(get_variance(l)))
	print("La moda es: %f" %(get_modas(l)))
