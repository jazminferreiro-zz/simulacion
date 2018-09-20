import util.generador as generador
import matplotlib.pyplot as plt
import math

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
		x = math.log(1-u)/self.lamda
		return x
	def generate_list(self, n):
		generator = Generator()
		l = generator.generate_list(n)
		for i in range(n):
			l[i] = self.generate(l[i])
		return l

print("######################################################")
print("EJERCICIO 2")
print("######################################################")
print("\n")
exp = Exponential_distribution(-15)
l = exp.generate_list(100000)
generate_histogram(l, "HISTOGRAMA DE 100000 NUMEROS GENERADOS",'./graficos/ejercicio2-histograma.png');
