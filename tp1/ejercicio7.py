import util.generador as generador
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

g = generador.GeneradorLinealCongruente()

print("######################################################")
print("EJERCICIO 7")
print("######################################################")
print("\n")

print("GENERAR ANALISIS ESPECTRAL EN 2 DIMENSIONES")
axisX = g.generar_lista(100000)
axisY = g.generar_lista(100000)

plt.scatter(axisX, axisY)
plt.title("ANALISIS ESPECTRAL EN 2 DIMENSIONES")
plt.savefig('./graficos/ejercicio7-analisis-espectral-2d.png')
plt.show()
print("GENERAR ANALISIS ESPECTRAL EN 2 DIMENSIONES")
print("\n")

print("GENERAR ANALISIS ESPECTRAL EN 3 DIMENSIONES")
axisX = g.generar_lista(100000)
axisY = g.generar_lista(100000)
axisZ = g.generar_lista(100000)

figure = plt.figure()
subplot = figure.add_subplot(111, projection='3d')
subplot.scatter(axisX, axisY, axisZ)
plt.title("ANALISIS ESPECTRAL EN 3 DIMENSIONES")
plt.savefig('./graficos/ejercicio7-analisis-espectral-3d.png')
plt.show()
print("GENERAR ANALISIS ESPECTRAL EN 3 DIMENSIONES")
print("\n")
