# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 13:58:09 2021

@author: Arnold
"""

import numpy as np
import pandas as pd

arreglo = np.array([1,2,3,4])

print(arreglo)

elemento1 = arreglo[0]

print("El primer elemento del arreglo es " + str(elemento1) + ".")

porcion_arreglo = arreglo[-2:]

print(porcion_arreglo)

arreglo = np.append(arreglo, 5)

print(arreglo)

arreglo = np.delete(arreglo, 1)

print(arreglo)

arreglo = np.array([1,2,3,4])

suma = arreglo.sum()

print("La suma de todos los elementos es " + str(suma) + ".")

promedio = arreglo.mean()

print("El promedio de todos los elementos es " + str(promedio) + ".")

maximo = arreglo.max()

print("El máximo elemento es " + str(maximo) + ".")

minimo = arreglo.min()

print("El minimo elemento es " + str(minimo) + ".")

arreglo_1 = np.array([1,2,3,4])
arreglo_2 = np.array([5,6,7,8])

arreglo_concat = np.concatenate((arreglo_1, arreglo_2))

print(arreglo_concat)

matriz = np.array( [ [1,2,3], [4,5,6] ] )
matriz

mat_1 = np.array([[1,2], [3,4]])
mat_1

mat_2 = np.array([[1,1], [4,4]])
mat_2

suma_matrices = mat_1 + mat_2
suma_matrices

producto_matrices = mat_1 * mat_2
producto_matrices

mat_1_por_mat_2 = mat_1.dot(mat_2)
mat_1_por_mat_2

mat_2_por_mat_1 = mat_2.dot(mat_1)
mat_2_por_mat_1

trans_matriz = mat_1.transpose()
trans_matriz

arreglo_booleano = np.array([True, False, False]) | np.array([True, True, False])
arreglo_booleano

serie = pd.Series(['A','B','C','D','E'])

serie

serie = pd.Series({"Colombia":"Bogotá", "Argentina": "Buenos Aires", "Peru": "Lima", "Mexico": "Ciudad de Mexico"})

serie

serie = pd.Series(['A','B','C','D','E'], index = [10,20,30,40,50], name = "Mi_serie")

serie

elem_2 = serie.iloc[1]
elem_2

elem_2 = serie.loc[20]
elem_2

parte_serie = serie.iloc[0:2]

parte_serie

l1 = ["Jorge", 28, "Bogotá"]
l2 = ["Laura", 37, "Lima"]

df = pd.DataFrame([l1,l2], index = ["Persona 1", "Persona 2"], columns = ["Nombre", "Edad", "Ciudad Residencia"])

df

s1 = pd.Series({"Pais":"Colombia", "Capital": "Bogotá"})
s2 = pd.Series({"Pais": "Argentina", "Capital": "Buenos Aires"})
s3 = pd.Series({"Pais": "Peru", "Capital": "Lima"})

df = pd.DataFrame([s1,s2, s3], index = ["Pais 1", "Pais 2", "Pais 3"])

df

mercadeo = np.array([2000, 1500, 1300, 1600])
logistica = np.array([1800, 1600, 1200, 1100])


def suma(arreglo1, arreglo2):
    
    concatenado = np.concatenate((arreglo1,arreglo2))
    respuesta = concatenado.sum()
    
    return respuesta

suma(mercadeo, logistica)

#%%
# Ejercicio 1


mercadeo = np.array([2000, 1500, 1300, 1600])
logistica = np.array([1800, 1600, 1200, 1600])

def promedio(arreglo1, arreglo2):
    
    concatenado = np.concatenate((arreglo1,arreglo2))
    respuesta = concatenado.mean()
    
    return respuesta

promedio(mercadeo, logistica)

#%%
# Ejercicio 2

hermanos = pd.Series({"Sonia": 40, "Patricia": 42, "Jorge": 37, 
                      "Alejandro": 45, "Aura": 47, "Carlos": 40, 
                      "Claudia": 41, "Victor": 43})
def mayores (hermanos):
    mayor_valor1 = hermanos.max()
    ind = hermanos[hermanos == mayor_valor1].index[0]
    result = hermanos.drop(labels = ind)
    mayor_valor2 = result.max()
    return (mayor_valor1,mayor_valor2)
print (mayores(hermanos))


#%%
# Ejercicio 3    

e1 = [ 28,"Bogotá", 2000]
e2 = [ 37, "Lima", 3200 ]
e3 = [ 23,"Bogotá", 1700]
e4 = [ 25, "Buenos Aires", 1100 ]
e5 = [ 43,"Buenos Aires", 3300]
e6 = [ 58, "Lima", 5500 ]
e7 = [ 32,"Bogotá", 2700]
e8 = [ 35, "Quito", 2500 ]

empleados = pd.DataFrame([e1,e2, e3, e4, e5, e6, e7, e8], 
                         index = ["Carlos", "David", "Ana", "Maria", "Felipe", "Luisa", "Juan", "Camila"], 
                         columns = ["Edad", "Ciudad Residencia", "Salario (en USD)"])
empleados

def ciudades (empleados):
    resultado = empleados.groupby("Ciudad Residencia")
    return len(resultado)

print(ciudades(empleados))


#%%
# Ejercicio 4
   
e1 = [ 28,"Bogotá", 2000]
e2 = [ 37, "Lima", 3200 ]
e3 = [ 23,"Bogotá", 1700]
e4 = [ 25, "Buenos Aires", 1100 ]
e5 = [ 43,"Buenos Aires", 3300]
e6 = [ 58, "Lima", 5500 ]
e7 = [ 32,"Bogotá", 2700]
e8 = [ 35, "Quito", 2500 ]

empleados = pd.DataFrame([e1,e2, e3, e4, e5, e6, e7, e8], 
                         index = ["Carlos", "David", "Ana", "Maria", "Felipe", "Luisa", "Juan", "Camila"], 
                         columns = ["Edad", "Ciudad Residencia", "Salario (en USD)"])
empleados


def mayor_al_promedio (empleados, index):
    promedio = empleados["Salario (en USD)"].mean()
    salario = empleados.loc[index][2]
    if salario > promedio:
        return True
    return False

print(mayor_al_promedio(empleados, "Luisa"))

#%%
# Ejercicio 5

e1 = [ 28,"Bogotá", 2000]
e2 = [ 37, "Lima", 3200 ]
e3 = [ 23,"Bogotá", 1700]
e4 = [ 25, "Buenos Aires", 1100 ]
e5 = [ 43,"Buenos Aires", 3300]
e6 = [ 58, "Lima", 5500 ]
e7 = [ 32,"Bogotá", 2700]
e8 = [ 35, "Quito", 2500 ]

empleados = pd.DataFrame([e1,e2, e3, e4, e5, e6, e7, e8], 
                         index = ["Carlos", "David", "Ana", "Maria", "Felipe", "Luisa", "Juan", "Camila"], 
                         columns = ["Edad", "Ciudad Residencia", "Salario (en USD)"])
empleados

def modificar (empleados):
    empleados = empleados.drop(empleados.index[1])
    empleados = empleados.rename(columns = {"Salario (en USD)": "Sueldo (en USD)"})
    return empleados

print(modificar(empleados))


#%%
# Ejercicio 6

paises = pd.read_csv("./Archivos/DiccionarioPaises.csv", encoding = "UTF-8", delimiter = ";")
paises.head()

def dif_longitud(paises):
    nuevo_df = []
    for index, row in paises.iterrows():
        if len(row[0]) == len(row[1]):
            nuevo_df.append(index)

    filter_df  = paises[paises.index.isin(nuevo_df)]

    return filter_df

dif_longitud(paises)
            

#%%
# Ejercicio 7

paises = pd.read_csv("./Archivos/DiccionarioPaises.csv", encoding = "UTF-8", delimiter = ";")
paises.head()

def paises_por_a(paises):
    paises = paises[paises["País en español"].str[0] == 'A']
    return paises

paises_por_a(paises)

#%%
# Ejercicio 8

paises = pd.read_csv("./Archivos/DiccionarioPaises.csv", encoding = "UTF-8", delimiter = ";")
paises.head()

alfabeto = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 
            'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 
            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

def inicia_con(paises):
    diccionario = {}
    for i in alfabeto:
        veces = 0
        for j in paises["País en inglés"]:
            if i == j[0]:
                veces += 1
        diccionario[i] = veces
    return diccionario
                
print(inicia_con(paises))
    
