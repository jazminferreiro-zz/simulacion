import util.generador as generador
import matplotlib.pyplot as plt

g = generador.GeneradorLinealCongruente()

print("######################################################")
print("EJERCICIO 1")
print("######################################################")
print("\n")

print("IMPRIMIR PRIMEROS 6 NUMEROS GENERADOS")
for i in range(6):
	print("EL NUMERO %d GENERADO ES: %f" %(i, g.generar()))
print("FIN IMPRIMIR PRIMEROS 6 NUMEROS GENERADOS")
print("\n")

print("GENERAR HISTOGRAMA")
lista = g.generar_lista(100000)
plt.hist(lista)
plt.title("HISTOGRAMA DE 100000 NUMEROS GENERADOS")
plt.savefig('./graficos/ejercicio1-histograma.png')
plt.show()
print("FIN GENERAR HISTOGRAMA")
print("\n")
