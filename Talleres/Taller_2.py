# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 18:43:29 2021

@author: Arnold
"""

#%%

# Ejercicio 1

num_1 = 6
num_2 = 6

if num_1 > num_2:
    mayor = num_1
elif num_2 > num_1:
    mayor = num_2
else:
    num_2 == num_1
    mayor = num_1
    
print(mayor)



#%%

# Ejercicio 2

elemento = "k"
lista = ["b", "c", "a", "d"]

if elemento in lista:
    lista
else:
    lista.extend(elemento)
print(lista)

#%%

# Ejercicio 3

num = 7
divisor = 4

cociente = num / divisor
resto = num % divisor

if resto == 0 :
    division_o_residuo = cociente
else:
    division_o_residuo = resto
    
print(cociente)
print(resto)

#%%
# Ejericicio 4


vel_Camilo = 10.5
vel_Esteban = 9.3
vel_Alejandro = 9.8
vel_David = 10.2

velocidad_rapida = 0
mas_rapido = ""

diccionario ={"Camilo" : vel_Camilo,
               "Esteban" : vel_Esteban,
               "Alejandro" : vel_Alejandro,
               "David" : vel_David,
               }

for competidor in diccionario:
    if diccionario[competidor] > velocidad_rapida:
        velocidad_rapida = diccionario[competidor]
        mas_rapido = competidor


#%%

# Ejercicio 5

num_actual = 20
cap_maxima = 40

porcentaje = (num_actual / cap_maxima)

if porcentaje <= 0.4:
    nivel_ocupacion = "Bajo"
    indicador_interes = num_actual

elif porcentaje > 0.4 and porcentaje <=0.8:
    nivel_ocupacion = "Medio"
    indicador_interes = porcentaje
else:
    nivel_ocupacion = "Alto"
    indicador_interes = cap_maxima - num_actual

info = [nivel_ocupacion, indicador_interes]

#%%

# Ejercicio 6

vegetarianos = ['Tomate', 'Champiñones', 'Cebolla']
no_vegetarianos = ['Pepperoni', 'Pollo', 'Jamón']

ingrediente_1 = 'Jamón'
ingrediente_2 = 'Pollo'
ingrediente_3 = 'Pepperoni'

if ingrediente_1 in vegetarianos:
        if ingrediente_2 in vegetarianos:
            if ingrediente_3 in vegetarianos:
                tipo = "Vegetariana"
            else:
                tipo = "Semi vegetariana"
        else:
            if ingrediente_3 in vegetarianos:
                tipo = "Semi vegetariana"
            else:
                tipo = "Semi vegetariana"
else:
    if ingrediente_2 in vegetarianos:
            if ingrediente_3 in vegetarianos:
                tipo = "Semi vegetariana"
            else:
                tipo ="Semi vegetariana"
    else:
        if ingrediente_3 in vegetarianos:
            tipo = "Semi vegetariana"
        else:
            tipo = "No vegetariana"
    

#%%

# Ejercicio 7

n = 100

pares = []

for i in range(1,n+1):
    if i%2 == 0:
        pares.append(i)
    
#%%

# Ejercicio 8

inicio = 10

cuenta_regresiva = []

if inicio > 1:
    for i in range(inicio,0,-1):
        cuenta_regresiva.append(i)


#%%

# Ejercicio 9

numeros = [1,2,8,4,6,7,10,45,67,89,100,12,34,2,1,5,34,36,28,27,43,182,13,124,122,158,835,38,46,38,28,38,34,67,89,58]
a_buscar = 3

indice = -1

for i in range(len(numeros)):
    if a_buscar == numeros[i]:
        indice = i
        break


#%%

# Ejercicio 10

cadena = "Me encanta programar, Python es mi pasión."

vocales = ["a","e","i","o","u"]

num_vocales = {}

               
for i in vocales:
    contar_si = 0
    
    for j in cadena:
        if i == j:
            contar_si = contar_si + 1
    
    num_vocales[i] = contar_si
            
        
    
#%%

# Ejercicio 11

lb = 2
ub = 5

perros_refugio = {
                  "Bruno": 5,
                  "Alex": 2,
                  "Fiona": 3,
                  "Salvador": 7,
                  "Max": 1,
                  "Copito": 5,
                  "Joe": 1,
                  "Maya": 2
                  }

perros_evento = []

for i in perros_refugio:
    if perros_refugio[i] >= lb and perros_refugio[i] <= ub:
        perros_evento.append(i)


#%%

# Ejercicio 12

cifrada = "Aqxzxobjmp nmo bi kmoqb x ixp 5 ab ix qxoab"
corr = 3

descifrada = ""

alfabeto = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

for i in cifrada:
    if i in alfabeto:
        x = alfabeto.index(i)
        if x+corr >= len(alfabeto):
           y = alfabeto[(x+corr)-len(alfabeto)]
        else:
           y = alfabeto[x+corr]
        descifrada += y
    else:
        descifrada += i
        
 #%%

# Ejercicio 13


catalogo = {
            "Oso de peluche" : 50000,
            "Perfume" : 9800,
            "Aretes" : 5000,
            "Dulces" : 5000,
            "Blusa" : 15000,
            "Bono de peluqueria" : 10000,
            "Libros" : 60000
            }   

valor_minimo = min(catalogo.values())

regalos = []

for mas_barato in catalogo:
    if catalogo[mas_barato] == valor_minimo:
        regalos.append(mas_barato)
regalos.sort()

regalo = regalos[0]

if catalogo[regalo] > 10000:
    regalo = "Carta"

#%%    
        
        
        
              
