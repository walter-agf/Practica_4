"""
Created on Wed Mar  4 05:32:21 2020

@author: Gualteros
"""
def bus_lin (ban,L,num) :
    iteracion = 0
    # Ciclo que recorre la lista para buscar 
    while ban == False :
        # Imprima el mensaje en el cual se muestre cada elemendo de la iteración 
        print ("Iteración = ",iteracion,", L[",iteracion,"] = ",L[iteracion])
        # Verifique si la clave se encontró
        if num == L[iteracion]:
            ban = True
        else :
            iteracion += 1
            if iteracion == len(L)- 1:
                ban = True
    i = iteracion + 1
    #Imprimir ultimo comentario
    if num == L[iteracion]:
        #En caso de que ban == True
        print ("")
        print ("Numero encontrado en la posición ",iteracion)
        print ("")
        print ("Cantidad de iteraciones ",i)
        print ("___________________________________________",end = "\n"*2)
    else :
        #En caso de que ban == False
        print ("")
        print ("la clave NO esta en la lista")
        print ("Cantidad de iteraciones ",i)
    return i
def bus_bis (ban,L,num):
    iteraciones = 0
    def resol (a,b):
        """
        Imprima el mensaje en el cual se informe la posición
        en la que se encontró el número, o un mensaje indicando que no se encontró
        """
        print ("")
        print ("Numero encontrado en la posicion [índice] = ",a)
        print ("")
        print ("Y en la ubicacion  = ",a + 1)
        print ("")
        # Imprima la cantidad de iteraciones que hizo el ciclo
        print ("Cantidad de iteraciones ",b)
        print ("___________________________________________",end = "\n"*2)
        return b
    """
    Defino una funcion para imprimir a futuro la infromacion por iteracion
    """
    def impre (a,b,c,d):
        print ("Iteración: ",a,"central = ",b,"L[",b,"] = ",c,", Intervalo: ",d)
    """
    Funcion para definir una variable dentro
    el rango pero que no se encuentra en la lista   
    """ 
    def compr (L,central,num,iteraciones,ban) :
        if L[central] < num and L[central + 1] > num:
            ban = True
            print ("")
            print ("El numero de iteracines fues de ",iteraciones)
            print ("")
            print ("El valor NO se encontro en la lista")
        return ban
    bajo = 0  # Índice inferior
    alto = len (L) # Índice superior
    if num > L[alto - 1] or num < L[bajo]:
        print ("")
        print ("El valor NO se encontro en la lista")
        print ("")
        print ("Cantidad de iteraciones 1")
        return 1
    else :
        # Ciclo que recorre la lista para buscar
        while ban == False:
            # Actualice el numeto de iteraciones
            iteraciones += 1
            # Calcule el valor del índice central (Use una variable llamada central para esto)
            use = alto + bajo
            central = use // 2
            # Compare el valor del elemento central con la clave (recuerde los 3 casos)
            if L[central] == num:
                ban = True
                q = resol (central,iteraciones)
                return q
            elif L[central] > num :
                alto = central
                intervalo = L[bajo:alto]
                #uso la funcion para imprimir informacion de la iteracion
                impre(iteraciones,central,L[central],intervalo)
                ban = compr (L,central,num,iteraciones,ban)
            elif L[central] < num :
                bajo = central
                intervalo = L[central:alto]
                #uso la funcion para imprimir informacion de la iteracion
                impre(iteraciones,central,L[central],intervalo)
                ban = compr (L,central,num,iteraciones,ban)
def rai_exa (inferior,superior):
    """Definicion de variables de uso """
    """ Variables del programa """
    pasos = 1 # Numero de pasos que se repite el ciclo
    a = inferior # Limite inferior
    b = superior # Limite superior
    epsilon = 0.01 # Tolerancia al error
    delta = 0.0001 # Tamaño de paso
    """ Inicialización de la variable que contendra el valor de la raiz """
    xl = a
    h = f(xl)
    # Evaluacion iterativa de la funcion en la rai­z sospechada
    while xl < b and abs(h) >= epsilon :
        # Actualizacion del numero de pasos
        pasos += 1
        # Incremento de la variable que contiene la rai­z
        xl += delta 
        # Evaluacion iterativa de la funcion en la rai­z sospechada
        h = f(xl)
    # Despliegue de los resultados
    print ("")
    print ("La cantidad de iteraciones fue de = ",pasos)
    print ("")
    print ("la raiz del polinomio es aproximadamente = ",xl)
    print ("da como resultado = ",h)
    print ("___________________________________________",end = "\n"*2)
    print ("___________________________________________",end = "\n"*2)
    return pasos
def rai_bis (inferior,superior) :
    pasos = 0 # Número de veces que se repite el ciclo
    epsilon = 0.01 # Tolerancia
    alfa = False
    while alfa == False :
        # Variables del programa
        a = inferior  # Limite inferior
        b = superior # Limite superio
        # Evaluación de la función en los limites
        f1 = f(a)
        f2 = f(b)
        """
        # Verificar que existe raí­z en los limites
        # Hay 4 posibilidades:
        # 1. Que la raíz sea a. Si f1 == 0.
        # 2. Que la raí­z sea b. Si f2 == 0.
        # 3. Que no haya raí­z. Si f1*f2 > 0 (asumiendo que hay máximo una raí­z en el intervalo)
        # 4. Que la raí­z se encuentre en el intervalo [a,b]. Si f1*f2 < 0
        """
        if f1 != 0 or f2 != 0 :
            fr = f1 * f2
            if fr > 0 : #Asumiendo que hay MAXIMO una raíz en el intervalo
                print ("")
                print ("La raiz no esta dentro del intervalo")
            elif fr < 0 :
                f3 = f (a)
                # Busqueda de la raí­z dentro del intervalo
                while alfa == False or abs(f3) >= epsilon:
                    # Actualización de las iteraciones
                    pasos += 1
                    # Cálculo del punto medio del intervalo        
                    central = (a + b)/2
                    # Búsqueda de la raí­z dentro del intervalo
                    f3 = f(central)
                    # Determinación del intervalo en el que se encuentra la raí­z
                    if f3 == 0 :
                        alfa = True
                    elif f3 < 0:
                        a = central
                    elif f3 > 0:
                        b = central
    # Despliegue de los resultados
    print ("")
    print ("La cantidad de iteraciones fue de = ",pasos)
    print ("")
    print ("la raiz del polinomio es aproximadamente = ",central)
    print ("da como resultado = ",f3)
    return pasos
u = int(input("Ingrese el tipo de problema a comparar || [Busqueda = 0] [Raices = 1] ----> "))
if u == 0 :
    print ("")
    # se muestra el comentario de introduccion al usuario
    print ("Ingrese el numero a buscar dentro de la lista =")
    print ("Lista = [-50, -45, -23, -21, -14, -9, -2, 0, 1, 3, 5, 16, 17, 24, 29, 30, 40, 52, 53, 92] ")
    # El usuario ingresa el numero a evaluar 
    """ numero en el ejemplo es [ 57 ] """
    n = int (input ("------> "))
    # Variables a emplear
    L = [-50, -45, -23, -21, -14, -9, -2, 0, 1, 3, 5, 16, 17, 24, 29, 30, 40, 52, 53, 92]
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
    print ("___________________________________________",end = "\n"*2)
    buslin = bus_lin (ban,L,num)
    busbis = bus_bis (ban,L,num)
    print ("-----------------------------------------------------> ",buslin)
    print ("-----------------------------------------------------> ",busbis)
elif u == 1 :
    print ("___________________________________________",end = "\n"*2)
    print ("___________________________________________",end = "\n"*2)
    def f(x):
        f = (x**3)+(2*(x**2))-(4*x)+3
        return f
    print ("Raiz del polinomio en ciertos limites")
    print ("f = (x**3)+(2*(x**2))-(4*x)+3",end = "\n"*2)
    alfa = False
    while alfa == False :
        print ("Define limite inferior")
        # en el ejemplo es -4
        inferior = float(input("---------> "))
        print ("Define limite superior")
        # en el ejemplo es -3
        superior = float(input("---------> "))
        """Definicion de variables de uso """
        """ Variables del programa """
        
        if inferior - superior > 0 :
                print ("")
                print ("        Valor mal ordenado        ",end = "\n"*2)
        else :
            alfa = True
    raiexa = rai_exa (inferior,superior)
    raibis = rai_bis (inferior,superior)
    print ("___________________________________________",end = "\n"*2)
    print ("___________________________________________",end = "\n"*2)
    print ("-----------------------------------------------------> ",raiexa)
    print ("-----------------------------------------------------> ",raibis)

    