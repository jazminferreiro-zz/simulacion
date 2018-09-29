from general import *

class Exponential_distribution:
	def __init__(self, lamda):
		self.lamda = lamda

	def generate(self,u):
		if(u > 1):
			raise ValueError('u must be less than 1.')
		x = -math.log(1-u)/self.lamda
		return x

	def generate_list(self, n):
		generator = Generator()
		l = generator.generate_list(n)
		for i in range(n):
			l[i] = self.generate(l[i])
		return l
	def get_media(self):
		return 1.0/self.lamda
	def get_variance(self):
		return 1.0/(self.lamda**2)


print("######################################################")
print("EJERCICIO 2")
print("######################################################")
print("\n")
exp = Exponential_distribution(15)
l = exp.generate_list(10000)
generate_histogram(l, "HISTOGRAMA DE 100000 NUMEROS GENERADOS",'./graficos/ejercicio2-histograma.png');

print("La media teorica de una v.A exponencial es: %f" %(exp.get_media()))
print("La media es: %f" %(get_media(l)) )
print("La varianza teorica de una v.A exponencial es: %f" %(exp.get_variance()))
print("La varianza experimental es: %f" %(get_variance(l)))
print("La moda es: %f" %(get_modas(l)))








