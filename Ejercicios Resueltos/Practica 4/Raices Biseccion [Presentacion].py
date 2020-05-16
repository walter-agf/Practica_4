"""
Created on Wed Mar  4 01:46:06 2020

@author: gualteros
"""
# Función
def f(x,j):
    if j == 1 :
        f = (x**3)+(2*(x**2))-(4*x)+3
    elif j == 2:
        f = (x**3)-(6*(x**2))+(11*x)-6
    elif j == 3:
        f = (x**4)-(7*(x**3))+(13*(x**2))+(23*x)-78
    else:
        print ("Valor inconcluso")
        f = None
    return f
print ("Raiz del polinomio en ciertos limites for Biseccion")
print ("",end = "\n"*2)
print (" 1° = f = (x**3)+(2*(x**2))-(4*x)+3",end = "\n"*2)
print (" 2° = f = (x**3)-(6*(x**2))+(11*x)-6",end = "\n"*2)
print (" 3° = f = (x**4)-(7*(x**3))+(13*(x**2))+(23*x)-78",end = "\n"*2)
j = int(input("Escoja la ecuacuion a evaluar = "))
pasos = 0 # Número de veces que se repite el ciclo
epsilon = 0.01 # Tolerancia
alfa = False
while alfa == False :
    print ("")
    print ("Define limite inferior")
    # en el ejemplo es -4
    inferior = float(input("---------> "))
    print ("Define limite superior")
    # en el ejemplo es -3
    superior = float(input("---------> "))
    if inferior - superior > 0 :
        print ("")
        print ("        Valor mal ordenado        ")
    else :
        # Variables del programa
        a = inferior  # Limite inferior
        b = superior # Limite superio
        # Evaluación de la función en los limites
        f1 = f(a,j)
        f2 = f(b,j)
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
                f3 = f (a,j)
                # Busqueda de la raí­z dentro del intervalo
                if f3 < epsilon:
                    alfa = True
                while alfa == False or abs(f3) >= epsilon:
                    # Actualización de las iteraciones
                    pasos += 1
                    # Cálculo del punto medio del intervalo        
                    central = (a + b)/2
                    # Búsqueda de la raí­z dentro del intervalo
                    f3 = f(central,j)
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
