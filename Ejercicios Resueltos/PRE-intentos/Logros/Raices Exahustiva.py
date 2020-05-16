"""
Created on Sun Mar  1 19:27:42 2020

@author: gualteros
"""
def f(x):
    f =(x**3)-(6*(x**2))+(11*x)-6
    return f
print ("Raiz del polinomio en ciertos limites")
print ("f = (x**3)-(6*(x**2))+(11*x)-6",end = "\n"*2)
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

