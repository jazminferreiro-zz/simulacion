import util.generador as generador
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np


x=[0, 0.00003, 0.00135, 0.00621, 0.02275, 0.06681, 0.11507, 0.15866, 0.21186, 0.27425, 0.34458, 0.42074, 0.5, 0.57926, 0.65542, 0.72575, 0.78814, 0.84134, 0.88493, 0.93319, 0.97725, 0.99379, 0.99865, 0.99997, 1]
y=[-5, -4, -3, -2.5, -2, -1.5, -1.2, -1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.5, 2, 2.5, 3, 4, 5]

# Con estos valores de X e Y obtengo lo que aparenta ser la inversa de una CDF de normal
# Si intercambio X e Y obtengo la CDF de una normal
f = interp1d(x, y)
plt.plot(x, y)
plt.title("DEBERIA SER LA INVERSA DE LA CDF DE UNA NORMAL")
plt.show()

class GeneradorNormal:
  def __init__(self):
    self.generador = generador.GeneradorLinealCongruente()
    self.inverse = interp1d(x, y)

  def generar(self):
    u = self.generador.generar()

    return self.inverse(u)

  def generar_lista(self, cantidad):
    lista = []

    for i in range(cantidad):
      lista.append(self.generar())

    return lista


g = GeneradorNormal()

print("GENERAR HISTOGRAMA")
lista = g.generar_lista(100000)
plt.hist(lista)
plt.title("HISTOGRAMA DE 100000 NUMEROS GENERADOS")
plt.savefig('./graficos/ejercicio3-histograma.png')
plt.show()
print("FIN GENERAR HISTOGRAMA")
print("\n")


print("La media deberia de una normal estandar debreia ser 0")
print("La media es: %f" % (np.mean(lista)))
print("La varianza deberia ser 1")
print("La varianza es: %f" % (np.var(lista)))