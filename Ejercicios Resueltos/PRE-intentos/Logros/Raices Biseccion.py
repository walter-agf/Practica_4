"""
Created on Wed Mar  4 01:46:06 2020

@author: gualteros
"""
# Función
def f(x):
    f = (x**3)+(2*(x**2))-(4*x)+3
    return f
print ("Raiz del polinomio en ciertos limites for Biseccion")
print ("f = (x**3)+(2*(x**2))-(4*x)+3",end = "\n"*2)
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