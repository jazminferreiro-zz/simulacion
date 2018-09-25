import util.generador as generador
import matplotlib.pyplot as plt

class GeneradorDistribucionEmpirica:
  def __init__(self):
    self.generador = generador.GeneradorLinealCongruente()

  def generar(self):
    u = self.generador.generar()
    if u >= float(0.0) and u < float(0.5):
      return 1
    elif u >= float(0.5) and u < float(0.7):
      return 2
    elif u >= float(0.7) and u < float(0.8):
      return 3
    elif u >= float(0.8) and u < float(1.0):
      return 4
    else:
      raise ValueError('u must be between 0 and 1.')

  def generar_lista(self, cantidad):
    lista = []

    for i in range(cantidad):
      lista.append(self.generar())

    return lista

g = GeneradorDistribucionEmpirica()

print("GENERAR HISTOGRAMA")
lista = g.generar_lista(100000)
plt.hist(lista)
plt.title("HISTOGRAMA DE 100000 NUMEROS GENERADOS")
plt.savefig('./graficos/ejercicio5-histograma.png')
plt.show()
print("FIN GENERAR HISTOGRAMA")
print("\n")
