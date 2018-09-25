import util.generador as generador
import matplotlib.pyplot as plt

class GeneradorDistribucionBernoulli:
  def __init__(self):
    self.generador = generador.GeneradorLinealCongruente()

  def generar(self):
    u = self.generador.generar()

    if u >= float(0.0) and u < float(0.5):
      return 0
    elif u >= float(0.5) and u < float(1.0):
      return 1
    else:
      raise ValueError('u must be between 0 and 1.')

  def generar_lista(self, cantidad):
    lista = []

    for i in range(cantidad):
      lista.append(self.generar())

    return lista

class GeneradorDistribucionGeometrica:
  def __init__(self):
    self.generador = GeneradorDistribucionBernoulli()

  def generar(self):
    cantidad = 0
    b = 0

    while b != 1:
      cantidad += 1
      b = self.generador.generar()

    return cantidad

  def generar_lista(self, cantidad):
    lista = []

    for i in range(cantidad):
      lista.append(self.generar())

    return lista

g = GeneradorDistribucionGeometrica()

print("GENERAR HISTOGRAMA")
lista = g.generar_lista(10000)
plt.hist(lista)
plt.title("HISTOGRAMA DE 10000 NUMEROS GENERADOS")
plt.savefig('./graficos/ejercicio6-histograma.png')
plt.show()
print("FIN GENERAR HISTOGRAMA")
print("\n")
