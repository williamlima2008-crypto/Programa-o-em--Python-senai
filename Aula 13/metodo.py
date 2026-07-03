import random

def aleatorio(a,z):
    n =  random.randint(a,z)
    print( n )
   

def contagem():
    for x in range(10,0,-1):
        print(x)
    print('Fogo')


def tabuada(numero):
 
    for x in range(11):
        calculo =  x  *  numero
        print(numero , 'x', x , '=', calculo )
   
    c  =  0
    while c <= 10:
        calculo = numero *  c
        print(numero , 'x', c , '=', calculo )
        c  =  c  +  1


def impares_reversos():
    for n in range(99,0,-2):
        print(n)