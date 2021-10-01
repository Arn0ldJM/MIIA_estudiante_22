# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 22:30:28 2021

@author: Arnold
"""

#%%

# Ejercicio 1

cadena = "Archivos de texto"

def sustituir(cadena):
    lst_cadena = list(cadena)
    segundo_caracter = lst_cadena[1]
    penultimo_caracter = lst_cadena[-2]
    
    lst_cadena[1] = penultimo_caracter
    lst_cadena[-2] = segundo_caracter
    
    cadena = ''.join(lst_cadena)
    
    return cadena 

print(sustituir(cadena))

#%%

# Ejercicio 2

directorio = "./Archivos/tesoro.txt"

def archivo_a_lista(ruta):
       
    archivo = open(ruta,'r', encoding ='UTF-8')
    data = archivo.readlines()
    archivo.close()
    
    return data
    
print(archivo_a_lista(directorio))

#%%

lista_paises = ['Japón', 'Francia']
lineas = archivo_a_lista(directorio)

def filtrar_paises(paises):
    lineas_paises = []
    
    for value in paises:
        for i in lineas:
            if value in i:
                lineas_paises.append(i)
                break

    return lineas_paises  

print(filtrar_paises(lista_paises))     

#%%

pronostico_jorge = ["Brasil", "Argentina", "Uruguay", "Colombia", "Chile", "Ecuador", "Perú", "Paraguay", "Venezuela", "Bolivia"]
pronostico_juan = ["Brasil", "Uruguay", "Colombia", "Argentina", "Ecuador", "Chile", "Paraguay", "Perú", "Venezuela", "Bolivia"]       

def ECM(pronostico1, pronostico2):
    
    eliminatorias = archivo_a_lista("./Archivos/Eliminatorias.txt")
    del eliminatorias[0]
    posiciones = {}
    pos = 0
    for i in eliminatorias:
        pais = i.split('\t')[1]
        ECM1 = 
        posiciones[pais] = pronostico1[pos], pronostico2[pos]
        pos += 1
    
    print(posiciones)
    
        
    
    return(0,0)

print(ECM(pronostico_jorge,pronostico_juan))