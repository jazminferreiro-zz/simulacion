import util.generador as generador
import matplotlib.pyplot as plt
import math
import operator

class Generator:
	def __init__(self):
		self.g = generador.GeneradorLinealCongruente();

	def generate_list(self,n):
		return self.g.generar_lista(n)

def generate_histogram(num_list, title, path):
	plt.hist(num_list)
	plt.title(title)
	plt.savefig(path)
	plt.show()

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


def get_media(l):
	return (sum(l)/len(l))

def get_modas(l):
	frecuencias = {}
	for i in l:
		if(i in frecuencias.keys()):
			continue
		frecuencias[i] = l.count(i)
	return max(frecuencias.iteritems(), key=operator.itemgetter(1))[0]


def get_variance(l):
	average = get_media(l); 	
	variance = 0
	for i in l:
		variance += (average - i) ** 2
	return (variance/len(l))

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


