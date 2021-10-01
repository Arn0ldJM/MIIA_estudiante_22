# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 18:50:13 2021

@author: Arnold
"""

#%%
# Ejemplo
lista_meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
>>> lista_meses[9:12]
cuarto_trimestre = lista_meses[9:12]
print(cuarto_trimestre)

#%%
# Ejercicio 1

lista_ventas = [20, 21, 22, 20, 21, 27]
print (lista_ventas)

#%%
# Ejercicio 2

mes_a_actualizar = 4
ventas_mes_a_actualizar = 18
lista_ventas[mes_a_actualizar-1] = ventas_mes_a_actualizar

#%%
# Ejercicio 3

n = 3
lista_ventas = [20, 21, 22, 20, 21, 27]
mejores_ventas = sorted(lista_ventas, reverse=True)
mejores_ventas = mejores_ventas[:n]
print (mejores_ventas)


#%%
# Ejercicio 4

import math

nombres = ["Sara", "Juan", "Alberto", "Ana", "Enrique", "Lola"]

nombres_ordenados = sorted(nombres)
longitud_nombres = len(nombres)
mitad_nombres = math.ceil(longitud_nombres / 2)
primera_mitad = nombres_ordenados[:mitad_nombres]
segunda_mitad = nombres_ordenados[mitad_nombres:]
print(nombres)
print(longitud_nombres)
print(mitad_nombres)
print(primera_mitad)
print(segunda_mitad)


#%%
# Ejercicio 5

lista_abecedario = ["a", "b", "c", ["d", "e", ["f", "g"]]]
lista_abc = lista_abecedario [:3]

#%%
# Ejercicio 6

lista_abecedario = ["a", "b", "c", ["d", "e", ["f", "g"]]]
lista_de = lista_abecedario[3][:2]

#%%
# Ejercicio 7

lista_fgh = (lista_abecedario[3][2][0:2])
lista_fgh.append("h")

#%%
# Ejercicio 8

Lista_ij = ["i", "j"]
lista_a_j = (lista_abc + lista_de + lista_fgh + Lista_ij)

#%%
# Ejericio 9

tupla_primos =  (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
a_buscar = 73
indice = tupla_primos.index(a_buscar)



#%%
# Ejericico 10

tupla_primos =  (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
lim_inferior = 17
lim_superior = 47
index_inf = tuple.index(tupla_primos, lim_inferior)
index_sup = tuple.index(tupla_primos, lim_superior)
tupla_secuencia = tupla_primos[index_inf : index_sup+1 : 2]
print(tupla_secuencia)

#%%
# Ejercicio 11
pedidos_semana_1 = (3,2)
pedidos_semana_2 = (2,4)
pedidos_semana_3 = (1,1)

tupla_pedidos = (pedidos_semana_1, pedidos_semana_2, pedidos_semana_3)

#%%
#Ejeccicio 12
pedidos_semana_1 = (3,2)
pedidos_semana_2 = (2,4)
pedidos_semana_3 = (1,1)

tupla_pedidos = (pedidos_semana_1, pedidos_semana_2, pedidos_semana_3)
s = 2
semana_x = tupla_pedidos[s-1]
total_pedidos_semana_s = sum (semana_x)

#%%
# Ejecricio 13

dicc_meses = {"Enero":31,
              "Febrero":28,
              "Marzo": 31,
              "Abril": 30,
              "Mayo":31,
              "Julio":31,
              "Agosto":31,
              "Septiembre":30,
              "Noviembre":30}

dicc_meses ['Junio'] = 30
dicc_meses ['Octubre'] = 31
dicc_meses ['Diciembre'] = 31 

print(dicc_meses)

#%%
# Ejercicio 14

matriz = {}
matriz[(1,2)]=1
matriz[(1,4)]=1
matriz[(1,5)]=1
matriz[(2,5)]=1 
matriz[(3,1)]=1
matriz[(3,4)]=1
matriz[(4,1)]=1
matriz[(4,3)]=1
matriz[(4,5)]=1

print(matriz)

# Ejercicio 15

h = 5
t = 2


if (t,h) in matriz:
    prediccion_familia = matriz[(t,h)]
else:
    prediccion_familia = 0
print(prediccion_familia)