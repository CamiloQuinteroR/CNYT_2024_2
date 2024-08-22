
#Camilo Andrés Quintero Rodriguez

import math

#Funcion que suma dos numeros compejos
def sumar(a, b):
    return ((a[0]+b[0],a[1]+b[1]))

#Funcion que multiplica dos numeros complejos
def producto(a, b):
    return ((a[0]*b[0] - a[1]*b[1],a[0]*b[1]+b[0]*a[1]))

#Funcion que resta dos numeros complejos a-b
def resta(a, b):
    return ((a[0] - b[0],a[1] - b[1]))

#Funcion que calcula el conjugado de un numero complejo
def conjugado(b):
    return (b[0],-b[1])

#Funcion que divide dos numeros complejos a/b
def division(a,b):
    up = producto(a,conjugado(b))
    down = b[0]*b[0]+b[1]*b[1]
    return ((up[0]/down,up[1]/down))

#Funcion que calcula el modulo de un numero complejo
def modulo(a):
    return (a[0]**2+a[1]**2)**(1/2)

#Funcion que convierte un polar a uno cartesiano ->> True 
#Convierte un cartesiano en polar ->> False
def conversion(a,b):
    if b == True:
        return (a[0]*math.cos(a[1]),a[0]*math.sin(a[1]))
    else:
        if a[1] < 0:
            return (modulo((a[0],a[1])),math.atan(a[1]/a[0])+ 2*math.pi)
        else:
            return (modulo((a[0],a[1])),math.atan(a[1]/a[0]))


#Calcula la fase de un numero complejo
def fase(a):
    if a[1] < 0:
        return math.atan(a[1]/a[0]) + 2*math.pi
    else:
        return math.atan(a[1]/a[0])


