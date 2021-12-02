# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 14:18:23 2021

@author: Arnold
"""
import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import plotly.io as pio
import plotly.express as px
import plotly
import seaborn as sns 
import missingno as msno
from sklearn.impute import KNNImputer
import scipy.stats as estadísticas
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#%%

#Funciones

def exploracion_data (df):
    s=df.shape
    t=df.dtypes
    i=df.info()
    l=list(data.columns)
    d=df.describe(include='O')
    d_o=df.describe(include='object')
    return s, t, d, i, l, d_o    

def valores_vacios(df):
    vacios_data = df.isnull().sum()
    mx = msno.matrix(df)
    dendrogram = msno.dendrogram(df)
    return vacios_data, mx, dendrogram

def visualizar_datos(df):
    print(data.head())
    print(data.tail())
    print(data.sample(5))

def imput_faltantes(df):
    df_imput = df.copy()
    for i in df:
        if df_imput[i].dtypes == object:
            df_imput[i].fillna(df_imput[i].mode()[0], inplace = True)
        else:
            df_imput[i].fillna(df_imput[i].mean(), inplace = True)
    return df_imput

def factorize_variables(df):
    class_type = df.columns.to_series().groupby(df.dtypes).groups
    ctext = class_type[np.dtype('object')]
    for c in ctext:
        df[c], _ = pd.factorize(df[c])
    return df

def dummies(df):
    df_dummies = df.copy()
    for i in df:
        if df[i].dtypes == object:
            df_dummies = pd.get_dummies(df_dumies["i"])
                   
    return df_dummies
#%%
#Mision 1

# Importar archivos txt.

SB11_20191_txt = pd.read_csv('Archivos/SB11_20191.txt', delimiter='¬', header=0, keep_default_na=True)
SB11_20201_txt = pd.read_csv('Archivos/SB11_20201.txt', delimiter='¬', header=0, keep_default_na=True)
SB11_20211_txt = pd.read_csv('Archivos/SB11_20211.txt', delimiter='¬', header=0, keep_default_na=True)

# Unir bases de datos

a = pd.concat([SB11_20211_txt, SB11_20201_txt], axis=0, ignore_index=True)
data = pd.concat([a, SB11_20191_txt], axis=0, ignore_index=True)

#definir indice

data.set_index("ESTU_CONSECUTIVO", append=False, drop=True, inplace =True)

#visualizar datos
visualizar_datos(data)

# Exploracion de los datos.
exploracion_data(data)
msno.heatmap(data)

#valores vacios
valores_vacios(data)

#primera depuración de datos

data = data.drop(['ESTU_ETNIA','ESTU_GENERACION-E','ESTU_NSE_ESTABLECIMIENTO','ESTU_NSE_INDIVIDUAL','ESTU_INSE_INDIVIDUAL',
           'PERCENTIL_ESPECIAL_GLOBAL','ESTU_ESTADOINVESTIGACION','PERCENTIL_GLOBAL','COLE_CARACTER','COLE_BILINGUE',
           'DESEMP_INGLES','PERCENTIL_INGLES','PUNT_INGLES','DESEMP_SOCIALES_CIUDADANAS','PERCENTIL_SOCIALES_CIUDADANAS',
           'PUNT_SOCIALES_CIUDADANAS','DESEMP_C_NATURALES','PERCENTIL_C_NATURALES','PUNT_C_NATURALES','DESEMP_MATEMATICAS',
           'PERCENTIL_MATEMATICAS','PUNT_MATEMATICAS','DESEMP_LECTURA_CRITICA','PERCENTIL_LECTURA_CRITICA','PUNT_LECTURA_CRITICA',
           'ESTU_COD_DEPTO_PRESENTACION','ESTU_DEPTO_PRESENTACION','ESTU_MCPIO_PRESENTACION','ESTU_COD_MCPIO_PRESENTACION',
           'ESTU_PRIVADO_LIBERTAD','COLE_DEPTO_UBICACION','COLE_COD_DEPTO_UBICACION','COLE_MCPIO_UBICACION','COLE_COD_MCPIO_UBICACION',
           'COLE_JORNADA','COLE_AREA_UBICACION','COLE_SEDE_PRINCIPAL','COLE_NOMBRE_SEDE','COLE_COD_DANE_SEDE','COLE_CALENDARIO',
           'ESTU_PAIS_RESIDE','ESTU_ESTUDIANTE','PERIODO','ESTU_FECHANACIMIENTO','ESTU_NACIONALIDAD','ESTU_TIPODOCUMENTO',
           'COLE_NATURALEZA','COLE_GENERO','COLE_NOMBRE_ESTABLECIMIENTO','COLE_COD_DANE_ESTABLECIMIENTO','COLE_CODIGO_ICFES'], axis=1)


# Eliminar filas que tiene 5 variables o menos con datos.
data = data.dropna(axis= 0, thresh= 15)

#valores vacios
valores_vacios(data)

msno.heatmap(data)
mx = msno.matrix(data)

data = data.drop(['ESTU_DEPTO_RESIDE','ESTU_COD_RESIDE_DEPTO','ESTU_MCPIO_RESIDE','ESTU_COD_RESIDE_MCPIO','FAMI_PERSONASHOGAR',
           'FAMI_CUARTOSHOGAR','FAMI_EDUCACIONPADRE','FAMI_EDUCACIONMADRE','FAMI_TRABAJOLABORPADRE','FAMI_TRABAJOLABORMADRE',
           'ESTU_HORASSEMANATRABAJA','ESTU_TIPOREMUNERACION','FAMI_TIENEHORNOMICROOGAS','FAMI_NUMLIBROS',
           'FAMI_SITUACIONECONOMICA', 'FAMI_TIENELAVADORA'], axis=1)

valores_vacios(data)

# imputacion
data = imput_faltantes(data)

#%%
#Mision 2

#Puntaje Global
sns.displot(data)
plt.title('Puntaje Global')
plt.xlabel('Puntaje')
plt.ylabel('Densidad');


sns.set(rc={"figure.figsize":(15, 8)})
ax = sns.boxplot(x="FAMI_ESTRATOVIVIENDA", y="PUNT_GLOBAL", data=data)
data["FAMI_ESTRATOVIVIENDA"].value_counts()

ax = sns.boxplot(x="ESTU_TIENEETNIA", y="PUNT_GLOBAL", data=data)
data["ESTU_TIENEETNIA"].value_counts()


ax = sns.boxplot(x="ESTU_GENERO", y="PUNT_GLOBAL", data=data)
data["ESTU_GENERO"].value_counts()


ax = sns.boxplot(x="FAMI_TIENEINTERNET", y="PUNT_GLOBAL", data=data)
data["FAMI_TIENEINTERNET"].value_counts()


ax = sns.boxplot(x="FAMI_TIENECOMPUTADOR", y="PUNT_GLOBAL", data=data)
data["FAMI_TIENECOMPUTADOR"].value_counts()


ax = sns.boxplot(x="FAMI_COMELECHEDERIVADOS", y="PUNT_GLOBAL", data=data)
data["FAMI_COMELECHEDERIVADOS"].value_counts()


ax = sns.boxplot(x="FAMI_COMECARNEPESCADOHUEVO", y="PUNT_GLOBAL", data=data)
data["FAMI_COMECARNEPESCADOHUEVO"].value_counts()


ax = sns.boxplot(x="FAMI_COMECEREALFRUTOSLEGUMBRE", y="PUNT_GLOBAL", data=data)
data["FAMI_COMECEREALFRUTOSLEGUMBRE"].value_counts()

#Función para factorizar las variables categoricas
data_fat = factorize_variables(data)
sns.heatmap(data_fat.corr(), square=True, annot=True)


cor = data_fat.corr()
sns.heatmap(cor, annot=True)
cor_pt_global = cor['PUNT_GLOBAL']

#%%
      

#Mision 3

y = pd.Series(data['PUNT_GLOBAL'])
X = data.iloc[:,0:14]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

lr = linear_model.LinearRegression()
lr.fit(X_train, y_train)

y_pred = lr.predict(X_test,)

r2 = lr.score(X_test, y_test)
r2

#modelo2

y = pd.Series(data_fat['PUNT_GLOBAL'])
X = data_fat['FAMI_COMELECHEDERIVADOS','FAMI_COMECARNEPESCADOHUEVO','FAMI_COMECEREALFRUTOSLEGUMBRE','FAMI_ESTRATOVIVIENDA']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

lr = linear_model.LinearRegression()
lr.fit(X_train, y_train)

y_pred = lr.predict(X_test,)

r2 = lr.score(X_test, y_test)
r2
