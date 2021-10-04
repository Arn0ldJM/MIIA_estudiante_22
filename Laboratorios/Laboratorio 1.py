# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 16:33:56 2021

@author: Arnold
"""

import numpy as np
import math as mt
import matplotlib.pyplot as plt

#Mision 1

def archivo_a_lista(ruta):

    archivo = open(ruta, 'r', encoding='UTF-8')
    data = archivo.read().splitlines()
    archivo.close()

    return data


datos = []

informacion = ["./Archivos/edad.txt", "./Archivos/escolaridad.txt",
               "./Archivos/estado_civil.txt", "./Archivos/estrato.txt",
               "./Archivos/genero.txt", "./Archivos/promedio.txt", "./Archivos/region.txt"]

for inf in informacion:
    datos.append(archivo_a_lista(inf))

id_estudiantes = list(range(0, len(datos[0])))
datos.insert(0, id_estudiantes)

datos[1] = list(map(int, datos[1]))
datos[6] = list(map(float, datos[6]))

#Mision 2


def summary(columna):
    resultados_descriptivos = {}
    resultados_descriptivos["Media"] = np.mean(columna)
    resultados_descriptivos["Mediana"] = np.median(columna)
    resultados_descriptivos["Desviacion"] = np.std(columna)
    resultados_descriptivos["Varianza"] = np.var(columna)

    return resultados_descriptivos


def graficas(datos_graficar):
    etiquetas = ['Edad', 'Escolaridad',
                 'Estado Civil', 'Estrato', 'Genero', 'Region']

    for i in range(len(etiquetas)):
        plt.hist(datos_graficar[i+1], bins=10)
        plt.xlabel(etiquetas[i])
        plt.ylabel('Cantidad')
        plt.show()

    plt.boxplot(datos_graficar[1])
    plt.xlabel('Edad')
    plt.ylabel('Cantidad')
    plt.show()

    plt.boxplot(datos_graficar[6])
    plt.xlabel('Promedio')
    plt.ylabel('Cantidad')
    plt.show()


graficas(datos)

#Mision 4


def metodo_asignacion1(data, becas):
    # Identificacion subgrupos por estrato
    grupos = list(np.unique(datos[4]))
    listado_grupos = []
    for g in grupos:
        lista_grupo = []
        for indice in range(len(data[4])):
            if g == data[4][indice]:
                candidato = data[0][indice]
                prom_notas = data[6][indice]
                lista_grupo.append([candidato, data[4][indice], prom_notas])
        lista_grupo.sort(key=lambda x: x[2], reverse=True)
        listado_grupos.append(lista_grupo)

    # Listado de candidatos seleccionados
    seleccionados = []

    # Contador de becas asignadas
    contador = 0

    while contador < becas:
        # Asignar becas a cada subgrupo

        for lg in listado_grupos:
            # Determinar el numero de becas que son el 2% del tamano del grupo
            becas_restantes = becas - contador

            becas_grupo = len(lg) * 0.02
            becas_grupo = round(becas_grupo)

            if becas_restantes <= becas_grupo:
                becas_grupo = becas_restantes

            # Tomar del listado de candidatos las primeras posiciones hasta completar el cupo de becas
            asignados = lg[0:becas_grupo]
            # Agregar al gran listado de estudiantes seleccionados
            seleccionados.extend(asignados)
            # Remover los candidatos que ya fueron asignados
            for i in asignados:
                lg.remove(i)
            # Actualiza la cantidad de becas asignadas
            contador = len(seleccionados)

    return seleccionados

becas = int(input("Ingresa el numero de becas disponible: "))

print(metodo_asignacion1(datos, becas))

#Mision 5


def metodo_asignacion2(data, becas):
    import numpy as np
    # Identificacion subgrupos por region y asignacion becas por region equitativamente
    grupos_regiones = list(np.unique(data[7]))
    listado_regiones = []
    dicc_becas_region = {}
    for r in grupos_regiones:
        lista_regiones = []
        for indice in range(len(data[7])):
            if r == data[7][indice]:
                candidato = data[0][indice]
                genero = data[5][indice]
                prom_notas = data[6][indice]
                lista_regiones.append(
                    [candidato, genero, data[7][indice], prom_notas])
        lista_regiones.sort(key=lambda x: x[3], reverse=True)
        listado_regiones.append(lista_regiones)
        prop_region = 1/len(grupos_regiones)
        becas_region = round(prop_region * becas)
        dicc_becas_region[r] = becas_region

    # Identificacion subgrupos por genero en cada region y su asignacion de becas
    grupos_generos = list(np.unique(data[5]))
    listado_regiones_generos = []
    dicc_becas_region_genero = {}

    for r in listado_regiones:
        for g in grupos_generos:
            lista_regiones_generos = []
            for lr in range(len(r)):
                if g == r[lr][1]:
                    lista_regiones_generos.append(r[lr])
            lista_regiones_generos.sort(key=lambda x: x[3], reverse=True)
            listado_regiones_generos.append(lista_regiones_generos)
            prop_region_genero = 1/len(grupos_generos)
            becas_region_genero = np.floor(
                prop_region_genero * dicc_becas_region[r[lr][2]])
            dicc_becas_region_genero[(r[lr][2], g)] = becas_region_genero

    # Listado de candidatos seleccionados
    seleccionados = []

    # Asignar becas a cada subgrupo
    for lrg in listado_regiones_generos:
        if len(lrg) > 0:
            # Obtener las becas a asignar
            reg = lrg[0][2]
            gen = lrg[0][1]
            becas_rg = int(dicc_becas_region_genero[(reg, gen)])
            # Tomar del listado de candidatos las primeras posiciones hasta completar el cupo de becas
            asignados = lrg[0:becas_rg]
            # Agregar al gran listado de estudiantes seleccionados
            seleccionados.extend(asignados)

    return seleccionados

becas = int(input("Ingresa el numero de becas disponible: "))

print(metodo_asignacion2(datos, becas))

# Mision 6


def volver_estructuradatos(data_trans, datos):
    iden = []
    edad = []
    esco = []
    estc = []
    estr = []
    gene = []
    prom = []
    regi = []

    # Reconstruir todos los datos del estudiante
    for item in data_trans:
        idest = item[0]
        iden.append(idest)
        edad.append(datos[1][idest])
        esco.append(datos[2][idest])
        estc.append(datos[3][idest])
        estr.append(datos[4][idest])
        gene.append(datos[5][idest])
        prom.append(datos[6][idest])
        regi.append(datos[7][idest])

    return [iden, edad, esco, estc, estr, gene, prom, regi]


becas = int(input("Ingresa el numero de becas disponible: "))

metodo1 = metodo_asignacion1(datos, becas)
metodo2 = metodo_asignacion2(datos, becas)

data_metodo1 = volver_estructuradatos(metodo1, datos)
data_metodo2 = volver_estructuradatos(metodo2, datos)


print("Metodo 1 Edad")
print(summary(data_metodo1[1]))

print("Metodo 2 Edad")
print(summary(data_metodo2[1]))

print("Metodo 1 Promedio")
print(summary(data_metodo1[6]))

print("Metodo 2 Promedio")
print(summary(data_metodo2[6]))

graficas(data_metodo1)
graficas(data_metodo2)


# Mision 7


def metodo_asignacion3(data, becas, politica, rango_i_edad, rango_f_edad):

    iden = []
    edad = []
    esco = []
    estc = []
    estr = []
    gene = []
    prom = []
    regi = []

    for ind in data[0]:
        if data[1][ind] >= rango_i_edad and data[1][ind] <= rango_f_edad:
            iden.append(ind)
            edad.append(data[1][ind])
            esco.append(data[2][ind])
            estc.append(data[3][ind])
            estr.append(data[4][ind])
            gene.append(data[5][ind])
            prom.append(data[6][ind])
            regi.append(data[7][ind])

    data = [iden, edad, esco, estc, estr, gene, prom, regi]

    if politica == 1:
        #Sub grupos unicos
        grupos_genero = list(np.unique(data[5]))
        listado_genero = []
        dicc_becas_genero = {}
        for g in grupos_genero:
            #proporciones por sub grupo
            proporcion = int(input("Indique la proporcion de "+str(g)+" en numero: "))
            lista_genero = []
            for e in range(len(data[0])):
                candidato = data[0][e]
                prom_notas = data[6][e]
                lista_genero.append([candidato, data[5][e], prom_notas])
            lista_genero.sort(key=lambda x: x[2], reverse=True)
            listado_genero.append(lista_genero)
            dicc_becas_genero[g] = np.floor(proporcion/100 * becas)
        
        # Listado de candidatos seleccionados
        seleccionados = []

        # Asignar becas a cada subgrupo
        for lg in listado_genero:
            if len(lg) > 0:
                # Obtener las becas a asignar
                becas_g = int(dicc_becas_genero[lg[0][1]])
                # Tomar del listado de candidatos las primeras posiciones hasta completar el cupo de becas
                asignados = lg[0:becas_g]
                # Agregar al gran listado de estudiantes seleccionados
                seleccionados.extend(asignados)
    elif politica == 2:
        grupos_estrato = list(np.unique(data[4]))
        listado_estrato = []
        dicc_becas_estrato = {}
        for g in grupos_estrato:
            proporcion = int(input("Indique la proporcion de Estrato "+str(g)+" en numero: "))
            lista_estrato = []
            for e in range(len(data[0])):
                candidato = data[0][e]
                prom_notas = data[6][e]
                lista_estrato.append([candidato, data[4][e], prom_notas])
            lista_estrato.sort(key=lambda x: x[2], reverse=True)
            listado_estrato.append(lista_estrato)
            dicc_becas_estrato[g] = np.floor(proporcion/100 * becas)
        
        # Listado de candidatos seleccionados
        seleccionados = []

        # Asignar becas a cada subgrupo
        for le in listado_estrato:
            if len(le) > 0:
                # Obtener las becas a asignar
                becas_e = int(dicc_becas_estrato[le[0][1]])
                # Tomar del listado de candidatos las primeras posiciones hasta completar el cupo de becas
                asignados = le[0:becas_e]
                # Agregar al gran listado de estudiantes seleccionados
                seleccionados.extend(asignados)            
    elif politica == 3:
        grupos_region = list(np.unique(data[7]))
        listado_region = []
        dicc_becas_region = {}
        for g in grupos_region:
            proporcion = int(input("Indique la proporcion de region "+str(g)+" en numero: "))
            lista_region = []
            for e in range(len(data[0])):
                candidato = data[0][e]
                prom_notas = data[6][e]
                lista_region.append([candidato, data[7][e], prom_notas])
            lista_region.sort(key=lambda x: x[2], reverse=True)
            listado_region.append(lista_region)
            dicc_becas_region[g] = np.floor(proporcion/100 * becas)
        
        # Listado de candidatos seleccionados
        seleccionados = []

        # Asignar becas a cada subgrupo
        for lr in listado_region:
            if len(lr) > 0:
                # Obtener las becas a asignar
                becas_r = int(dicc_becas_region[lr[0][1]])
                # Tomar del listado de candidatos las primeras posiciones hasta completar el cupo de becas
                asignados = lr[0:becas_r]
                # Agregar al gran listado de estudiantes seleccionados
                seleccionados.extend(asignados)            
    else:
        print("No selecciono una opcion valida")
        return ""

    return seleccionados


becas = int(input("Indique el numero de becas: "))
edad1 = int(input("Indique el rango inferior de edad: "))
edad2 = int(input("Indique el rango superior de edad "))
politica = int(input("Indique el # de politica a calcular. Genero = 1, Estrato = 2, Region = 3: "))

print(metodo_asignacion3(datos, becas, politica, edad1, edad2))

