"""
Created on Wed Feb 26 08:44:03 2020

@author: Gualteros
"""
# se muestra el comentario de introduccion al usuario
def resultante (iteracion,L,num,i,ubi):
    #Imprimir ultimo comentario
    if num == L[ubi]:
        #En caso de que ban == True
        print ("")
        print ("Numero encontrado en la posición ",iteracion)
        print ("")
        print ("Cantidad de iteraciones ",i)
    else :
        #En caso de que ban == False
        print ("")
        print ("la clave NO esta en la lista")
        print ("Cantidad de iteraciones ",i)
print ("Ingrese el numero a buscar dentro de la lista =")
print ("Lista = [ -1001, -1000, -1000, -1000, -100, -100, -50, -45, -23, -21, -14, -9,-5, -2, 0, 0, 0, 0, 0, 1, 3, 3, 5, 7, 11, 16, 17, 24, 29, 30, 40, 52, 53, 85, 92, 500, 1575, 10001] ")
# El usuario ingresa el numero a evaluar 
""" numero en el ejemplo es [ 57 ] """
n = int (input ("------> "))
# Variables a emplear
L = [ -1001, -1000, -1000, -1000, -100, -100, -50, -45, -23, -21, -14, -9,-5, -2, 0, 0, 0, 0, 0, 1, 3, 3, 5, 7, 11, 16, 17, 24, 29, 30, 40, 52, 53, 85, 92, 500, 1575, 10001]
''' 
Variable que indica si se encontró la clave en la lista tal que:
- Ban = False, la clave no esta en la lista
- Ban = True, la clave esta en la lista
'''
ban = False 
# numero en el ejemplo es [ 57 ]
num = n  # Valor de prueba para buscar en la lista
# Imprima un mensaje donde se muestre el valor a buscar
print ("El valor a buscar es = ",num)
print ("")
iteracion = 0
# Ciclo que recorre la lista para buscar 
while ban == False :
    # Imprima el mensaje en el cual se muestre cada elemendo de la iteración 
    print ("Iteración = ",iteracion,", L[",iteracion,"] = ",L[iteracion])
    # Verifique si la clave se encontró
    if num == L[iteracion]:
        ban = True
        ubi = iteracion
        i = iteracion + 1
        iteracion += 1
        if num == L[iteracion] :
            cad = str (iteracion - 1)
            while num == L[iteracion]:
                cad += " , " + str (iteracion)
                print ("Iteración = ",i,", L[",i,"] = ",L[i])
                iteracion += 1
                i += 1 
            iteracion = cad
            resultante (iteracion,L,num,i,ubi)
        else :
            iteracion -= 1
            ubi = iteracion
            i = iteracion + 1
            resultante (iteracion,L,num,i,ubi)
    else :
        iteracion += 1
        if iteracion == len(L)- 1:
            ban = True
#****************************** Salida esperada ***********************************#
#
#Número: 57
#
#Iteración: 0, L[0] = 2
#Iteración: 1, L[1] = 10
#Iteración: 2, L[2] = 20
#Iteración: 3, L[3] = 23
#Iteración: 4, L[4] = 41
#Iteración: 5, L[5] = 45
#Iteración: 6, L[6] = 57
#
#Numero encontrado en la posición 6
#
#Cantidad de iteraciones 7
#**********************************************************************************#
    