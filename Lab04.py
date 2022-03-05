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
from sympy import*
from sympy.stats import *

# Imports para el título
import time
import sys

X1 = [1,2,3,4,5,6,7,8]
x = Symbol('X')
pdf = exp(-x)
#X1
#X1 = ContinuousRV()

# --------------- Main -------------------

Bienvenida = '\n----- Bienvenido al programa ----\n'

# Se imprime el titulo de forma ¡chilerisima!
for i in Bienvenida:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.02)


#PARTE DE GABY
# ----- Inciso D -----
X = DiscreteUniform('X',X1)
Fun_prob =density(X).dict
print("d)",Fun_prob) 

# ----- Inciso E -----
for i in Fun_prob.values():
    acum=0
    A_values=[]
    while acum != 1:
        ac= i + acum;
        acum +=i
        A_values.append(ac)
A_dic=dict(zip(X1,A_values))
print("e)",A_dic)


#PARTE PAO
# ----- Inciso I -----
# Densidad
x = Symbol("x")
X2 = Uniform("x", 8, 10)
d2 = density(X2)(x)
print("i)", d2)

# ----- Inciso J -----
a2 = cdf(X2)(x)
print("j)", a2)

# ----- Inciso k -----
#3/4*Fx1 + 1/4Fx2
