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