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
datos

