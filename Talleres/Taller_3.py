# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 01:23:26 2021

@author: Arnold
"""

#%%

# Ejercicio 1

lista = [23.7, 15.1, 22.2, 21, 16.1, 24, 15.9]

def suma_lista(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma

#%%

# Ejercicio 2

lista = [23.7, "15", "22.2", 21, 24, 15.9]

def primera_letra(lista):
    letra = ""
    for i in lista:
        if type(i) == str:
            if i.isalpha():
               letra = i
               break
    return letra

print(primera_letra(lista))

#%%

# Ejercicio 3

lista = [4, 3, 8, 5, 6, 2, 7, 5]

def separar_pares_impares(lista):
    pares = []
    impares = []
    for i in lista:
        if i%2 == 0:
           pares.append(i)
        else:
            impares.append(i)
    pares.sort()
    impares.sort()
    
    return (pares, impares)

a = separar_pares_impares(lista)
print(a)

#%%

# Ejercicio 4

treinta = 30
cuarenta_y_cinco = 45
cincuenta = 50
sesenta_y_tres = 63

def mayor50(trinta):
    if trinta > 50:
        return True
    else:
        return False

mayor_a_cincuenta = lambda trinta:True if trinta > 50 else False
print(mayor_a_cincuenta(treinta))

#%%

# Ejercicio 5

lista = [3, 4, 2, 5, 5, 6, 3]

def modulo_del_minimo(lista):
    repit =[]
    for i in lista:
        if lista.count(i) > 1:
            repit.append(i)
        
    num_min = min(repit)
    return lambda entero: num_min%entero

min_val_rep = modulo_del_minimo(lista)  
print(min_val_rep(5))
            
        
#%%