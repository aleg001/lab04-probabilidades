""" *****************************************
    Universidad del Valle de Guatemala
    Teoría de Probabilidades sección 10
    03/03/2022

    Miembros:
    Alejandro Gómez - 20347
    Diego Córdova - 20212
    Cristian Aguirre - 20231
    Paola de León - 20361
    Paola Contreras - 20213
    Marco Jurado - 20308
    ***************************************** """ 

# Se definen imports
from sympy import Symbol, exp, Interval
from sympy.stats import P, density, cdf, FiniteRV, ContinuousRV
import sympy as sy

# Imports para el título
import time
import sys

x = Symbol('X')
pdf = exp(-x)
#X1
X1 = ContinuousRV()

#X2

X2 = ContinuousRV(x,pdf, set=Interval(8,10))


# ----- Inciso k -----
#3/4*Fx1 + 1/4Fx2

# --------------- Main -------------------

Bienvenida = '\n----- Bienvenido al programa ----\n'

# Se imprime el titulo de forma ¡chilerisima!
for i in Bienvenida:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.02)

menu = 0

dict_menu = {
    #'1': EminemXD,
    #'2': Ejercicio2,
    #'3': bye,
}

while menu != '3':

    menu = input(
        '\nIngrese una opcion\n1. Ejercicio 1\n2. Ejercicio 2\n3. Salir\n-> ')
    accion = dict_menu[menu]
    accion()
