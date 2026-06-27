print('Programa PAR OU IMPAR')

def comparar():
    n1 = int(input('>>'))
    n2 = int(input('>>'))
    
    if n1 % 2 == 0 and n2 % 2 == 0:
        print('Ambos são PARES')
        
    elif n1 % 2 == 0 and n2 % 2 != 0:
        print('Apenas o 1° é PAR')
        
    elif n1 % 2 != 0 and n2 % 2 == 0:
        print('Apenas o 2° é PAR')
    
    else:
        print('Ambos são IMPARES...')
        
comparar()
        
        