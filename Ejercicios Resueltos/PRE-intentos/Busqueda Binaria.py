"""
Created on Wed Feb 26 09:27:33 2020

@author: Gualteros
"""
# se muestra el comentario de introduccion al usuario
print ("Ingrese el numero a buscar dentro de la lista =")
print ("Lista = [-50, -45, -23, -21, -14, -9, -2, 0, 1, 3, 5, 16, 17, 24, 29, 30, 40, 52, 53, 92] ")
# El usuario ingresa el numero a evaluar 
""" numero en el ejemplo es [ 57 ] """
n = int (input ("------> "))
# Variables a emplear
L = [-50, -45, -23, -21, -14, -9, -2, 0, 1, 3, 5, 16, 17, 24, 29, 30, 40, 52, 53, 92]
iteraciones = 0 # Contador de iteraciones
''' 
Variable que indica si se encontró la clave en la lista tal que:
- Ban = False, la clave no esta en la lista
- Ban = True, la clave esta en la lista
'''
ban = False 
""" en el ejemplo es el 57 """
num = n  # Valor de prueba para buscar en la lista
# Imprima un mensaje donde se muestre la clave
print ("")
print ("La clave a buscar es : ",num)
print ("")
def resol (a,b):
    ''' Imprima el mensaje en el cual se informe la posición
    en la que se encontró el número, o un mensaje indicando que no se encontró'''
    print ("")
    print ("Numero encontrado en la posicion [índice] = ",a)
    print ("")
    print ("Y en la ubicacion  = ",a + 1)
    print ("")
    # Imprima la cantidad de iteraciones que hizo el ciclo
    print ("Cantidad de iteraciones ",b) 
"""Defino una funcion para imprimir a futuro la infromacion por iteracion"""
def impre (a,b,c,d):
    print ("Iteración: ",a,"central = ",b,"L[",b,"] = ",c,", Intervalo: ",d)
bajo = 0  # Índice inferior
alto = len (L) # Índice superior
if num > L[alto - 1] or num < L[bajo]:
    print ("")
    print ("El valor NO se encontro en la lista")
    print ("")
    print ("Cantidad de iteraciones 1") 
else :
    # Ciclo que recorre la lista para buscar
    while ban == False:
        # Calcule el valor del índice central (Use una variable llamada central para esto)
        use = alto + bajo
        central = use // 2
        # Compare el valor del elemento central con la clave (recuerde los 3 casos)
        if L[central] == num:
            ban = True
            resol (central,iteraciones)
        elif L[central] > num :
            # Actualice el numeto de iteraciones
            iteraciones += 1
            alto = central
            intervalo = L[bajo:alto]
            #uso la funcion para imprimir informacion de la iteracion
            impre(iteraciones,central,L[central],intervalo)
            if L[central] < num and L[central + 1] > num:
                ban = True
                print ("")
                print ("El numero de iteracines fues de ",iteraciones)
                print ("")
                print ("El valor NO se encontro en la lista")
        elif L[central] < num :
            # Actualice el numeto de iteraciones
            iteraciones += 1
            bajo = central
            intervalo = L[central:alto]
            #uso la funcion para imprimir informacion de la iteracion
            impre(iteraciones,central,L[central],intervalo)
            if L[central] < num and L[central + 1] > num:
                ban = True
                print ("")
                print ("El numero de iteracines fues de ",iteraciones)
                print ("")
                print ("El valor NO se encontro en la lista")
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
