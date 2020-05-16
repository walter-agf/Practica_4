# Busqueda binaria

# Variables a emplear
L = [2, 10, 20, 23, 41, 45, 57, 90] # Lista (cambiar por la de la guía)
iteraciones = 0 # Contador de iteraciones
''' 
Variable que indica si se encontró la clave en la lista tal que:
- Ban = False, la clave no esta en la lista
- Ban = True, la clave esta en la lista
'''
ban = False 

num = 57  # Valor de prueba para buscar en la lista
bajo = 0 # Índice inferior
alto = len(L) - 1 # Índice superior

# Imprima un mensaje donde se muestre la clave

# Ciclo que recorre la lista para buscar 

    # Actualice el numeto de iteraciones

    # Calcule el valor del índice central (Use una variable llamada central para esto)     
    
    # Imprima: La iteración, el valor de central, el valor de L[central] y el intervalo actual de busqueda (consulte cómo indicar un intervalo de una lista en Python)
        
    # Compare el valor del elemento central con la clave (recuerde los 3 casos)

''' Imprima el mensaje en el cual se informe la posición
en la que se encontró el número, o un mensaje indicando que no se encontró'''
    
# Imprima la cantidad de iteraciones que hizo el ciclo

#****************************** Salida esperada ***********************************#
#Número: 57
#
#Iteración: 1, central = 3, L[central] = 23, Intevalo: [2, 10, 20, 23, 41, 45, 57, 90]
#Iteración: 2, central = 5, L[central] = 45, Intevalo: [41, 45, 57, 90]
#Iteración: 3, central = 6, L[central] = 57, Intevalo: [57, 90]
#
#Numero encontrado en la posición 6
#
#Cantidad de iteraciones 3
#**********************************************************************************#
