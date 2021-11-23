# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 23:45:44 2021

@author: Arnold
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#%%
# Ejercicio 1

archivo = pd.read_excel("./Archivos/datosTaller.xlsx")
archivo

def dividir_datos(df):
    X = df.iloc[:,1:]
    y = df.iloc[:,0]
    return (X,y)

print(dividir_datos(archivo))

#%%
# Ejercicio 2

datos = (pd.DataFrame({"x1":[6,  8,  6,  4, 5,  7,  8],
                       "x2":[3,  1,  2,  2, 1,  4,  5],
                       "x3":[22, 35, 41, 3, 18, 18, 9]}),
         pd.Series([9, 1, 5, 3, 9, 9, 6]))

def crear_train_test(tupla):
    X = tupla[0]
    y = tupla[1]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 0)
    
    return X_train, X_test, y_train, y_test

crear_train_test(datos)

#%%
# Ejercicio 3

datos = (pd.DataFrame({"x1":[6,  8,  6,  4,  5,  7,  8],
                       "x2":[3,  1,  2,  2,  1,  4,  5],
                       "x3":[22, 35, 41, 3,  18, 18, 9]}),
         pd.DataFrame({"x1":[7,  6,  5,  3,  5],
                       "x2":[5,  4,  4,  4,  4],
                       "x3":[47, 50, 11, 42, 1]}),
         pd.Series([9,  1, 5, 3, 9, 9, 6]),
         pd.Series([10, 3, 7, 6, 8]))
datos

from sklearn import linear_model

def crear_modelo(tupla):
    rl = linear_model.LinearRegression()
    rl.fit(tupla[0], tupla[2])
    return rl
  

#%%
# Ejercicio 4

import pickle

modelo = pickle.load(open("Archivos/modeloTaller", 'rb'))

datos = (pd.DataFrame({"x1":[6,  8,  6,  4,  5,  7,  8],
                       "x2":[3,  1,  2,  2,  1,  4,  5],
                       "x3":[22, 35, 41, 3,  18, 18, 9]}),
         pd.DataFrame({"x1":[7,  6,  5,  3,  5],
                       "x2":[5,  4,  4,  4,  4],
                       "x3":[47, 50, 11, 42, 1]}),
         pd.Series([9,  1, 5, 3, 9, 9, 6]),
         pd.Series([10, 3, 7, 6, 8]))

def predecir(mod_entrenado,tupla):
        return mod_entrenado.predict(tupla[1])

predecir(modelo, datos)  

#%%
# Ejercicio 5

import pickle

modelo = pickle.load(open("Archivos/modeloTaller", 'rb'))

X_test = pd.DataFrame({"x1":[7,  6,  5,  3,  5],
                       "x2":[5,  4,  4,  4,  4],
                       "x3":[47, 50, 11, 42, 1]})

y_test = pd.Series([10, 3, 7, 6, 8])

def calcular_precision(modelo_entrenado,X_test,y_test):
    return modelo_entrenado.score(X_test, y_test)

calcular_precision(modelo,X_test,y_test)
