import util.generador as generador
import matplotlib.pyplot as plt
import math

class GeneradorDistribucionBernoulli:
  def __init__(self, p):
    if p < float(0.0) or p > float(1.0):
      raise ValueError('probability must be between 0 and 1.')

    self.generador = generador.GeneradorLinealCongruente()
    self.probability = p

  def generar(self):
    u = self.generador.generar()

    if u >= float(0.0) and u < float(self.probability):
      return 1
    elif u >= float(self.probability) and u < float(1.0):
      return 0
    else:
      raise ValueError('u must be between 0 and 1.')

  def generar_lista(self, cantidad):
    lista = []

    for i in range(cantidad):
      lista.append(self.generar())

    return lista

class GeneradorDistribucionGeometrica:
  def __init__(self, p):
    if p < float(0.0) or p > float(1.0):
      raise ValueError('probability must be between 0 and 1.')

    self.generador = GeneradorDistribucionBernoulli(p)
    self.probability = p

  def generar(self):
    if self.probability == float(0.0):
      return math.inf

    cantidad = 0
    b = 0

    while b != 1:
      b = self.generador.generar()
      cantidad += 1

    return (cantidad - 1)

  def generar_lista(self, cantidad):
    lista = []

    for i in range(cantidad):
      lista.append(self.generar())

    return lista

g = GeneradorDistribucionGeometrica(0.5)

print("GENERAR HISTOGRAMA")
lista = g.generar_lista(10000)
plt.hist(lista)
plt.title("HISTOGRAMA DE 10000 NUMEROS GENERADOS")
plt.savefig('./graficos/ejercicio6-histograma.png')
plt.show()
print("FIN GENERAR HISTOGRAMA")
print("\n")
