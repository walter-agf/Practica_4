#Definimos variable para resibir lista
def resit_list ():
    #Damos la indicacion de como ingresar datos
    print ("  Por favor ingrese el numero de listas  ")
    print ("#Nota: si ingresa un numero decimal se tomara como el numero entero imediatamente anterior")
    #En esta parte se modifica el tipo de dato en caso de resibir un float, para intercambiarlo a int
    lis = (float(input("---------> ")))
    lis = int(lis)
    #Definimos num como numero de lista en el lenguaje del usuario
    num = 0
    #Definimos variable (de tipo lista) para ingresar las listas
    L = []
    #Definimos ciclo para resibir todas las listas requeridas por el usuario 
    for i in range (0,lis):
        #Agregamos un valor a num para entenderlo como usuario
        num += 1
        print ("")
        #Pedimos que ingrese los datos
        print ("INGRESE VALORES PARA LA LISTA = ",num)
        print ("Recuerde que cuando indique[ n ], terminara de resibir datos ")
        #el valor val se define como la variable de agregacion a la lista si vale n, termina el proceso
        val = None
        # Definimos la lista a como variable para ingresar los datos y despues agreegarlos a la lista prinsipal
        a = []
        #Ciclo que agrega variables
        while val != "n":
            print ("")
            #Ingresamos un valor a val
            val = (input("---> "))
            # Preguntamos si vale n para cancelar
            if val != "n" :
                #convertimos a float porque pueden ingresar valores que no sean enteros
                val = (float(val))
                if val == 0 :
                    val = (int(val))
                else :
                    if val % int(val) == 0 :
                        #Si val no vale n, convertirmos el valor de str a int y lo ingresamos a la lista a
                        val = (int(val))
                #Ingresamos valor a (a) 
                a.append (val)   
        #Al final a la ingresamos dentro de la lista prinsipla
        L.append (a)
    #Imprimimos para mostrar las listas ingresadas
    print ("ESTAS SON TUS LISTAS")
    b = 0
    print ("")
    #Las trasquibimos a vertical
    for i in range (len(L)):
        print ("")
        print (L[b])
        b +=1
    #retornamos el valor de la lista prinsipal osea L a la variable que solicito la funcion
    return L
#prueba para comprobar funcionamiento de resit_list
"""
L = resit_list ()
"""
#Funcion para organizar las listas ingresadas
#Se puede ingresar una sola lista o una lista de listas
def organizar (listas):
    #Espesificamos los datos a pedir
    print ("")
    print ("ORGANIZADOR DE LISTAS")
    #Averiguamos el numeor de listas que hay dentro de la lista, sea el caso
    num_one = len(listas)
    num_one -= 1
    #ciclo para organizar la o las listas segun corresponda a num_one > 1
    for i in range (len(listas)):
        print ("")
        #Si hay mas de una lista inicia con la primera y la separamaos para tratarla en la variable lis 
        lis = listas [num_one]
        #Averiguamos cuantas cantidades hay dentro de lis
        num_two = len(lis)
        print (lis)
        #Definimos a como la variable a ingresar la resultante de la organizacion
        a = []
        #Definimos el ciclo para averiguar el orde con base al valor menor
        #Definimos el rango segun la cantidad de indices en la lista 
        for d in range (num_two):
            #Restamos uno a la cantidad ya se cuenta desde 1 pero en indice desde 0
            num_two -= 1
            #Definimos una variable para el cambio de posicion dentro del instructivo
            cam = num_two
            #Definimos una variable para sacar el ultimo valor de la lista a medir
            cont = lis[cam]
            #Ciclo que resta de uno en uno hasta hallar el menor de una lista
            while cam != -1 :
                #Resta de uno en uno
                cam -= 1
                #Preguntamos si la cantidad medida es menor a cont
                if lis[cam] < cont:
                    #Si es asi la intercambiamos por cont
                    cont = lis[cam]
            #Al tener una menor la eliminamos de la lista
            lis.remove (cont)
            #La agregamos a (a), hasta eliminar todos los datos de una y agreegados en orden a (a)
            a.append (cont)
        #Print, imprimimos las nueva lista 
        print (a)
        #La intercambiamos por la pociion original en la lista preingresada
        listas[num_one] = a 
        #Cambiamos de posiicon de derecha a izquierda para la sguiente Lista dentro de la lista de listas
        num_one -= 1
    #Imprimimos los resultados 
    print ("")
    print ("LISTA DE LISTAS")
    b = 0
    print ("")
    #Imprimimos los resultados en vertical
    for i in range (len(listas)):
        print ("")
        print (listas[b])
        b +=1
    #Retornamos la lista ingresada ya organizada
    return (listas)
#Pruebas para medir funcionalidad
"""
L = organizar(L)
print ("")
print (L)
"""
#Funcion para listarorden y vertical para mostrar
def list_vert (lista):
    #Afirmar estas son tus listas
    print ("")
    print ("ESTAS SON TUS LISTAS")
    #Indica el indice de busqueda
    b = 0
    #INdica el numero al usuario
    c = 1
    print ("")
    #Las trasquibimos a vertical
    for i in range (len(lista)):
        print ("")
        #Imprime el numero de usuario y la lista como tal
        print (c," )","   ",lista[b])
        #Agrego unp a el indice para siguiente valor
        b +=1
        #Agrega uno a numero de usuario
        c +=1
    print ("")
"""
list_vert (L)
"""
def bus_en (lista,list_vert):
    print ("\n"*24)
    print ("En cuales listas desea buscar")
    list_vert (lista)
    print ("Ingrese el numero de lista 1 por 1, y termine con n")
    print ("Valor que no sea entero se tomara el entero anterior")
    print ("Recuerde colorcar solo valores de listas que existan en caso contrario tendra error")
    val = None
    num_list = []
    while val != "n" :
        val = (input("---------> "))
        if val != "n":
            val = int(val)
            num_list.append (val)
    a = []
    ubi = 0
    while ubi < len (num_list):
        cor = num_list [ubi]
        a.append (lista[cor-1])
        ubi += 1
    print ("\n"*2)
    print ("El valor se buscara en las listas")
    print (num_list)
    print ("\n")
    print ("Ingrese el valor a buscar en la lista o listas")
    print ("\n")
    bus = (input("---> "))
    bus = (float(bus))
    if bus % int(bus) == 0 :
        bus = (int(bus))
    print ("\n")
    print ("Numero a buscar es = ",bus)
    print ("\n"*2)
    return (a,bus)
"""
L = [[3,76,54,75,23,7.8,45,43,3],[45,45,3,54,236,5,76],[45,3,3,21,23,5,4,3,5,4]]
(b,c) = bus_en (L,list_vert)
print ("\n")
print (b)
print ("\n")
print (c)
"""   
def continuar (conti):
    s = False
    while s == False:
        cos = (input("[ 0 = SI] [ 1 = NO ]---> "))
        if cos == "1" :
            conti = False
            s = True
        elif cos == "0" :
            s = True
        elif cos != "1" and cos != "0":
            print ("Valor indeterminado, reingrese")
    return conti
"""
continuar (True)
"""
def resol (a,b,c):
    #Imprima el mensaje en el cual se informe la posición en la que se encontró el número, o un mensaje indicando que no se encontró
    print ("                                              Intervalo: [",c,"]")
    print ("")
    print ("Numero encontrado en la posicion [índice] = ",a)
    print ("")
    # Imprima la cantidad de iteraciones que hizo el ciclo
    print ("Cantidad de iteraciones ",b)
    print ("")
    ban = False
    return ban
#Defino una funcion para imprimir a futuro la infromacion por iteracion
def impre (a,b,c,d,e):
    print ("Iteración: ",a,"central = ",b," lista[",e,"] = ",c,", Intervalo: ",d)
#Funcion para definir una variable dentro el rango pero que no se encuentra en la lista    
def compr (L,central,num,iteraciones,ban) :
    if L[central] < num and L[central + 1] > num:
        print ("")
        print ("El numero de iteracines fues de ",iteraciones)
        print ("")
        print ("El valor NO se encontro en la lista")
        print ("_________________________")
        ban = False
    return ban
def sali (a,b):
    print ("")
    print ("El valor SI se encontro en la lista ",[a]," En la posicion [indice]",b)
    print ("")
    print ("Cantidad de iteraciones 1")
    print ("_________________________")
    ban = False
    return ban