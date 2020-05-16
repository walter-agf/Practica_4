#Importamos las funciones del documento de Funciones
import Funciones
#Usamos la Funcion de Ingreso de Listas
L = Funciones.resit_list ()
organizar = True
conti = True
#Organizamos dichas listas
print ("\n"*12)
print ("Quieres organizar los datos")
organizar = Funciones.continuar (organizar)
if organizar == True:
    L = Funciones.organizar(L)
(liss,n) = Funciones.bus_en (L,Funciones.list_vert)
#liss = [[-50, -45, -23, -21, -14, -9, -2, 0, 1, 3, 5, 16, 17, 24, 29, 30, 40, 52, 53, 92],[-1001,-1000,-1000,-1000,-100,-100,-5,0,0,0,0,3,7,11,85,500,1575,10001]]
#n = (int(input("Ingrese el valor = ")))
while conti == True:
    """
    Variable que indica si se encontró la clave en la lista tal que:
    - Ban = False, la clave no esta en la lista
    - Ban = True, la clave esta en la lista
    """
    ban = False 
    iteracion = 0
    ubi = 0
    cap = 0
    print ("")
    # Ciclo que recorre la lista para buscar 
    while ban == False :
        lista = liss [ubi]
        # Imprima el mensaje en el cual se muestre cada elemendo de la iteración 
        print ("Iteración = ",iteracion,", Lista[",ubi + 1,"] = ",lista,"Medida Lista[",cap,"] = ",lista[cap])
        # Verifique si la clave se encontró
        if n == lista[cap]:
            iteracion += 1
            print ("")
            print ("Numero encontrado en la posición ",cap)
            print ("")
            print ("Cantidad de iteraciones ",iteracion)
            print ("\n")
            if ubi == (len(liss)-1):
                ban = True
            else :
                ubi += 1
                cap = 0
        else :
            iteracion += 1
            cap += 1
            if cap == (len(lista)-1):
                print ("")
                print ("la clave NO esta en la lista")
                print ("Cantidad de iteraciones ",iteracion)
                if ubi == (len(liss)-1):
                    ban = True
                else :
                    ubi += 1
                    cap = 0
    print ("¿Desea Continuar?")
    conti = Funciones.continuar (conti)
    if conti == True :
        if organizar == False:
            print ("\n"*2)
            print ("Quieres organizar los datos")
            organizar = Funciones.continuar (organizar)
            if organizar == False:
                L = Funciones.organizar(L)
            (liss,n) = Funciones.bus_en (L,Funciones.list_vert)
"""
************************* Salida esperada en el ejemplo ***************************

Número: 57

Iteración: 0, L[0] = 2
Iteración: 1, L[1] = 10
Iteración: 2, L[2] = 20
Iteración: 3, L[3] = 23
Iteración: 4, L[4] = 41
Iteración: 5, L[5] = 45
Iteración: 6, L[6] = 57

Numero encontrado en la posición 6

Cantidad de iteraciones 7
**********************************************************************************#
"""    