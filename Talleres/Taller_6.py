# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 11:56:09 2021

@author: Arnold
"""

import numpy as np
import pandas as pd


#%%
# Ejercicio 1

def importar_e_indexar ():
    df_data_public = pd.read_stata('.\Archivos\pooled_data_public.dta')
    df_data_public.head()
    df_data_public.set_index("id",drop = True, inplace = True)

    return df_data_public

c = importar_e_indexar()

#%%
# Ejercicio 2

def indice_sencillo_a_multiple ():
    df_data_public = importar_e_indexar()
    df_data_public.set_index("country_code", append=True, drop=True, inplace =True)
    return df_data_public

p = indice_sencillo_a_multiple()

#%%
# Ejercicio 3

def sin_columnas ():
    df_data_public = importar_e_indexar()
    df_data_public.drop(columns=["country_name", "grado", "coima"], axis=1, inplace = True)
    return df_data_public

k = sin_columnas()

#%%
# Ejercicio 4

def indexar_columnas_numericamente():
    df_data_public = importar_e_indexar()
    df_data_public.drop(columns = df_data_public.iloc[:,80:100], axis=1, inplace = True)
    return df_data_public  

n = indexar_columnas_numericamente()

#%%
# Ejercicio 5

def trabajo_afuera_y_mayores():
    df_data_public = importar_e_indexar()
    df_data_public = df_data_public[(df_data_public["trabajocasa"] == "Fuera de su casa") & (df_data_public["haymayores"] == "si")]
    return df_data_public  

r = trabajo_afuera_y_mayores()

 #%%
# Ejercicio 6

def hogares_decrecen():
    df_data_public = importar_e_indexar()
    df_data_public = df_data_public.loc[:,["nrhogar", "nrhogar_antes"]]
    df_data_public["hogar_decrecio"] = np.where ((df_data_public ["nrhogar"] < df_data_public["nrhogar_antes"]), 1, 0)
    return df_data_public

s = hogares_decrecen()