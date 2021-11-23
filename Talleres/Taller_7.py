# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 17:47:39 2021

@author: Arnold
"""

import numpy as np
import pandas as pd
from datetime import datetime

#%%
# Ejercicio 1

orden_cliente = pd.DataFrame([[70001, 3002],
                              [70002, 3001],
                              [70003, 3001],
                              [70004, 3003],
                              [70005, 3003]],
                              columns = ['no_orden', 'id_cliente'])

cliente_categoria = pd.DataFrame([[3001, "Platino"],
                                  [3002, "Oro"    ],
                                  [3003, "Oro"    ],
                                  [3004, "Bronce" ]],
                                  columns = ['id_cliente', 'Categoría Cliente'])

def union_derecha(df1, df2):
    df_union = pd.merge(df1,df2, how = "right", on = "id_cliente")
    return df_union

print(union_derecha(cliente_categoria,orden_cliente))

#%%
# Ejercicio 2

cliente_categoria_orden = pd.DataFrame([[3002, "Platino", 70001],
                                        [3004, "Oro",     70002],
                                        [3003, "Oro",     70003]],
                                        columns = ['id_cliente', 'Categoría Cliente', 'no_orden'])
    
cliente_categoria = pd.DataFrame([[3006, "Oro"    ],
                                  [3001, "Oro"    ],
                                  [3005, "Platino"],
                                  [3007, "Platino"]],
                                  columns = ['id_cliente', 'Categoría Cliente'])

def concatenar_interno(df1, df2):
    df_union = pd.concat([df1,df2], join = "inner", axis = 0)
    return df_union

print(concatenar_interno(cliente_categoria_orden,cliente_categoria))

#%%
# Ejercicio 3

ventas = pd.DataFrame([[2600.0,  12200.0, 6000.0],
                       [11200.0, 9000.0,  600.0 ],
                       [np.nan,  8000.0,  3000.0],
                       [4000.0,  np.nan,  np.nan],
                       [np.nan,  10000.0, 2000.0]],
                      columns = ["Producto 1", "Producto 2", "Producto 3"])

def mediana_faltantes(df):
    df.fillna(df.median(), inplace = True)
    return df

print(mediana_faltantes(ventas))
    
#%%
# Ejercicio 4

clientes = pd.DataFrame([[3002, "Masculino", "No"],
                         [3001, "Femenino",  "No"],
                         [3003, "Femenino",  "Sí"]],
                        columns = ["id_cliente", "Sexo", "Cliente Premium"])

clientes_prueba = pd.DataFrame([[3002, "Masculino", "Sí"],
                         [3001, "Masculino",  "No"],
                         [3003, "Femenino",  "Sí"]],
                        columns = ["id_cliente", "Sexo", "Cliente Premium"])

def cliente_dummies (df):
    df["Sexo"] = np.where(df["Sexo"] == "Femenino", 1, 0)
    df["Cliente Premium"] = np.where(df["Cliente Premium"] == "No", 1, 0)                          
    return df

print(cliente_dummies(clientes))


#%%
# Ejercicio 5

fecha_string = "2020-10-December"

def cadena_a_fecha(fecha_string):
    fecha = datetime.strptime(fecha_string,"%Y-%d-%B")
    return fecha

print(cadena_a_fecha(fecha_string))


#%%
# Ejercicio 6

def union_izquierda():
    TIB_Serie = pd.read_excel("Archivos/1.1.TIB_Serie historica IQY.xlsx", header = 7, skipfooter= 6).rename(columns={"Fecha(dd/mm/aaaa)": "Fecha"})
    TIP_Serie = pd.read_excel("Archivos/1.2.TIP_Serie historica diaria IQY.xlsx", header = 7, skipfooter= 4).rename(columns={"Fecha (dd/mm/aaaa)": "Fecha"})
    df = pd.merge(TIB_Serie, TIP_Serie, on ="Fecha",  how = "left")
    return df

print(union_izquierda())

#%%
# Ejercicio 7

df = pd.DataFrame({'no_orden':    [70001,np.nan,70002,70004,np.nan,70005,np.nan,70010,70003,70012,np.nan,70013],
                   'monto US$':   [150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45, 75.29,3045.6],
                   'Fecha Orden': ['2012-10-05','2012-09-10',np.nan,'2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
                   'idCliente':   [3002,3001,3001,3003,3002,3001,3001,3004,3003,3002,3001,3001],
                   'idVendedor':  [5002,5003,5001,np.nan,5002,5001,5001,np.nan,5003,5002,5003,np.nan]})

def ejercicio7(df):
    df = df.columns[df.isnull().sum()>1]
    df = df.values.tolist()
    return df

ejercicio7(df)

#%%
# Ejercicio 8

lista_meses = ["Enero",      "Febrero", "Marzo",     "Abril",
               "Mayo",       "Junio",   "Julio",     "Agosto",
               "Septiembre", "Octubre", "Noviembre", "Diciembre"] 

def ejercicio8():
    df = pd.read_excel("Archivos/Festivos.xlsx")
    df = df.loc[:,"2020":"2012"]
    amd=[]
    for año in df:
        for pos_celda in range(len(df[año].tolist())):
            dia = df[año][pos_celda].split()[0].zfill(2)
            mes = df[año][pos_celda].split()[1]
            mes = str(lista_meses.index(mes) + 1)
            mes = mes.zfill(2)
            amd.append(str(año) + mes + dia)
            
    return pd.to_datetime(amd,format="%Y-%m-%d") 

print(ejercicio8())

        