#test de Kolmogorov-Smirnov chi cuadrado
from util.general import *
from ejercicio4 import Normal


if __name__ == '__main__':
	print("######################################################")
	print("EJERCICIO 4")
	print("######################################################")
	print("\n")
	cant = 100000
	uni = Normal(35,5)
	l = uni.generate_list(cant)