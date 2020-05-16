import Funciones
#Usamos la Funcion de Ingreso de Listas
L = Funciones.resit_list ()
#Organizamos dichas listas
L = Funciones.organizar(L)
""" 
Variable que indica si se encontró la clave en la lista tal que:
- Ban = False, la clave no esta en la lista
- Ban = True, la clave esta en la lista
"""
# Imprima un mensaje donde se muestre la clave
(liss,n) = Funciones.bus_en (L,Funciones.list_vert)
#liss = [[-50, -45, -23, -21, -14, -9, -2, 0, 1, 3, 5, 16, 17, 24, 29, 30, 40, 52, 53, 92],[-1001,-1000,-1000,-1000,-100,-100,-5,0,0,0,0,3,7,11,85,500,1575,10001]]
#n = (int(input("Ingrese el valor = ")))
conti = True
while conti == True:
    iteraciones = 0 # Contador de iteraciones
    ban = True
    ubi = 0
    # Ciclo que recorre la lista para buscar
    while ban == True:
        lista = liss[ubi]
        bajo = 0  # Índice inferior
        alto = (len(lista)-1) # Índice superior
        if n > lista[alto] or n < lista[bajo]:
            print ("")
            print ("El valor NO se encontro en la lista ",[ubi])
            print ("")
            print ("Cantidad de iteraciones 1")
            print ("_________________________")
        elif n == lista[alto]:
            ban = Funciones.sali (ubi,alto)
        elif n == lista[bajo]:
            ban = Funciones.sali (ubi,bajo)
        else :
            while ban == True :
                # Actualice el numeto de iteraciones
                iteraciones += 1
                # Calcule el valor del índice central (Use una variable llamada central para esto)
                use = alto + bajo
                central = use // 2
                # Compare el valor del elemento central con la clave (recuerde los 3 casos)
                if lista[central] == n:
                    ban = True
                    intervalo = []                
                    intervalo = lista[central]
                    ban = Funciones.resol (central,iteraciones,intervalo)
                elif lista[central] > n :
                    alto = central
                    intervalo = lista[bajo:alto]
                    #uso la funcion para imprimir informacion de la iteracion
                    Funciones.impre(iteraciones,central,lista[central],intervalo,ubi)
                    ban = Funciones.compr (lista,central,n,iteraciones,ban)
                elif lista[central] < n :
                    bajo = central
                    intervalo = lista[central:alto]
                    #uso la funcion para imprimir informacion de la iteracion
                    Funciones.impre(iteraciones,central,lista[central],intervalo,ubi)
                    ban = Funciones.compr (lista,central,n,iteraciones,ban)
        if ubi < (len(liss)-1):
            ban = True
            ubi += 1
    print ("")
    print ("¿Desea Continuar?")
    conti = Funciones.continuar (conti)
    if conti == True :
        (liss,n) = Funciones.bus_en (L,Funciones.list_vert) 
"""
****************************** Salida esperada ***********************************#
Número: 57

Iteración: 1, central = 3, L[central] = 23, Intevalo: [2, 10, 20, 23, 41, 45, 57, 90]
Iteración: 2, central = 5, L[central] = 45, Intevalo: [41, 45, 57, 90]
Iteración: 3, central = 6, L[central] = 57, Intevalo: [57, 90]

Numero encontrado en la posición 6

Cantidad de iteraciones 3
**********************************************************************************#
"""