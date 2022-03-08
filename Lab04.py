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

x = Symbol('X')

# ----- Diccionario para prints ----
incisos = {
    'a': '\na) P([X1 = 2])\n',
    'b': '\nb) P([X1 > 2])\n',
    'c': '\nc) P([X1 < 2])\n',
    'd': '\nd) Funcion de probabilidad P([x1 = i]) para i E 1 - 8\n',
    'e': '\ne) Funcion de distribucion acumulada F(x1)\n',
    'f': '\nf) P([X2 = 9])\n',
    'g': '\ng) P([X2 > 9])\n',
    'h': '\nh) P([X2 < 9])\n',
    'i': '\ni) Funcion densidad f(x2)\n',
    'j': '\nj) Funcion de distribucion acumulada F(x2)\n',
    'k': '\nk) Funcion de distribucion acumulada F(x3)\n',
    'l': '\nl) P([x3 = 8])\n',
    'm': '\nm) P([x3 > 8])\n',
    'n': '\nn) P([x3 < 8])\n'
}

# --------------- Main -------------------

Bienvenida = '\n----- Bienvenido al programa ----\n'

# Se imprime el titulo de forma ¡chilerisima!
for i in Bienvenida:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.02)


#PARTE DE GABY
# ----- Inciso D -----
X1 = DiscreteUniform('X',[1,2,3,4,5,6,7,8])
Fun_prob =density(X1).dict
print(incisos['d'], f'-> {Fun_prob}') 

# ----- Inciso E -----
'''
for i in Fun_prob.values():
    acum=0
    A_values=[]
    while acum != 1:
        ac= i + acum;
        acum +=i
        A_values.append(ac)
A_dic=dict(zip(x1,A_values))
'''
print(incisos['e'], f'-> {cdf(X1)}') 

#PARTE DE CHRIS
#-----------X2---------
X2 = Uniform("x", 8, 10)

#------ Inciso F ------
Pf= P(X2<=9)-P(X2<9)
print(incisos['f'], f'-> {Pf}')

#------ Inciso G ------
Pg= P(X2>9)
print(incisos['g'], f'-> {Pg}')

#------ Inciso H ------
Ph= P(X2<9)
print(incisos['h'], f'-> {Ph}')

#PARTE PAO
# ----- Inciso I -----
# Densidad
d2 = density(X2)(x)
print(incisos['i'], f'-> {d2}') 

# ----- Inciso J -----
a2 = cdf(X2)(x)
print(incisos['j'], f'-> {a2}') 

# Parte Diego 
# ----- Inciso k -----
fpdX3_1 = {
    1: 3/4 * 1/8,
    2: 3/4 * 1/8,
    3: 3/4 * 1/8,
    4: 3/4 * 1/8,
    5: 3/4 * 1/8,
    6: 3/4 * 1/8,
    7: 3/4 * 1/8,
    8: 3/4 * 1/8
}
X3_1 = FiniteRV('X3_1', density=fpdX3_1);

X3_2 = Piecewise((1/8*x - 1/4, (8 < x) & (x < 10)), (0, True))

cdf_x3 =  '(1 <= x <= 8)\n'
cdf_x3 += str(cdf(X3_1))
cdf_x3 +=  '\n(8 < x < 10)\n'
cdf_x3 += str(X3_2)
print(incisos['k'], cdf_x3)

# ----- Funcion para clcular probabilidad de x3 ----
def prob_x3(operador:str, valor):
    '''
    Regresa la probabilidad de x3 valuado en valor y operado con el operador
    Ejemplos: 
        - prob_x3(>, 5) = P(x3 > 5)
        - prob_x3(=, 3) = P(x3 = 3)
    '''
    
    if operador == '=':
        parte_x1 = P(X3_1 <= valor) - P(X3_1 < valor)
        parte_X2 = 1/4 * (P(X2 <= valor) - P(X2 < valor))
        return parte_x1 + parte_X2
        
    elif operador == '<':
        return P(X3_1 < 8) + (1/4 * P(X2 < valor))

    elif operador == '>':
        return P(X3_1 > valor) + (1/4 * P(X2 > valor))
