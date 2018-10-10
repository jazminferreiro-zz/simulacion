# -*- coding: utf-8 -*-
import datetime, time
class GeneradorLinealCongruente:
    def __init__(self,a,c,m, inicial):
        self.a = a
        self.c = c
        self.m= m
        self.actual = inicial

    def generar(self):
        self.actual =  (self.a*self.actual + self.c) % self.m
        return self.actual

    def generar_lista(self, cantidad):
        lista = []
        for i in range(cantidad):
            lista.append(self.generar())
        return lista

def imprimir(l):
    lstr = ','.join(str(e) for e in l)
    print "["+lstr+"]"


def ejercicio1():
    print("                         EJERCICIO 1")
    a = 1
    c = 7
    m = 10

    print("generamos una lista de numeros aleatorios con (1x+7) % 10")

    print("con x inicial = 7")
    g7 = GeneradorLinealCongruente(a, c, m, 7)
    l7 = g7.generar_lista(11)
    imprimir(l7)


    print("con x inicial = 1")
    g1 = GeneradorLinealCongruente(a,c,m, 1)
    l1 = g1.generar_lista(11)
    imprimir(l1)

    print("vemos que es un mal generador porque para distintintas semillas se repite el mismo ciclo de numeros")
    print("se podria predecir el valor siguiente")
    print("__________________________________________________________________________________________")

def ejercicio2():
    print("                         EJERCICIO 2")
    a = 9821
    c = 0.211327
    m = 1
    seconds = time.mktime(datetime.datetime.now().timetuple())
    Excel = GeneradorLinealCongruente(a,c,m,seconds)
    l1= Excel.generar_lista(11)
    imprimir(l1)
    
    seconds = time.mktime(datetime.datetime.now().timetuple())
    l2= Excel.generar_lista(11)
    imprimir(l2)
    print("__________________________________________________________________________________________")

"""Se desea utilizar una urna para simular una variable aleatoria con un espacio muestral S = {1,2,3,4,5} y
probabilidades p 1 = 1/3 , p 2 = 1/5 , p 3 = 1/4 , p 4 = 1/7 , p 5 = 1 − (p 1 + p 2 + p 3 + p 4 ) . ¿Cuántas
bolas debería contener la urna y cómo deberían estar marcadas? Generalice este resultado para demostrar
que una urna puede ser utilizada para simular cualquier experimento aleatorio con un espacio muestral
finito y probabilidades dadas por números racionales."""

from fractions import Fraction
class urna:
    def __init__(self, espacio_muestral, probabilidades):
        if(len(espacio_muestral) != len(probabilidades)):
            raise Exception("debe haber una probabilidad para cada elmento del espacio muestral")
        if(sum(probabilidades) - 1 > 0.3 ):
            raise Exception("las probabilidades deberian sumar 1")
        self.dic = {}
        for i in range(0, len(espacio_muestral)):
            self.dic[espacio_muestral[i]] =  Fraction(probabilidades[i])

    def get_total(self):
        total = 1
        for prob in self.dic.values():
            total = total*prob.denominator
        return total


    def print_urna(self):
        total = self.get_total()
        print("total de bolas: %d" %(total))
        for (tipo,prob) in self.dic.items():
            print("del tipo %s, hay %d bolas" %(tipo, prob*total)) 

def ejercicio7():
    print("                         EJERCICIO 7 ")

    espacio_muestral = ["a", "b", "c", "d", "e"]
    probabilidades = [Fraction(1,3), Fraction(1,5), Fraction(1,4),Fraction(1,7), Fraction(31,420)]
    u = urna(espacio_muestral, probabilidades)
    u.print_urna()


    print("__________________________________________________________________________________________")

def ejercicio():
    print("                         EJERCICIO ")
    print("__________________________________________________________________________________________")

ejercicio1()
ejercicio2()
ejercicio7()
