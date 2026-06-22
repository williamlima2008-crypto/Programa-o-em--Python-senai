#Exercicio 1

n = int(input('Digite um número:'))
if n < 0:
    print('O número é negativo!👎')
elif n == 0:
    print('O número é zero!')
else:
    print('O número é positivo!👍 ')
print('Fim do Programa!!!🏁')


# Exercicio 2

idade = int(input('Qual é sua IDADE? '))
if idade >= 18:
    print('Idade Obrigatória para Votar (TSE 2026)', idade, 'anos')
elif idade < 18 and idade == 16:
    print('Você já pode votar (TSE 2026)', idade,'anos')
elif idade == 15:
    print('Idade minima para Solicitar o titulo de eleitor\napenas com 16 anos para votar (TSE 2026)', idade,'anos')
else:
    print('Você não tem idade para votar!', idade,'anos')
print('Fim do Programa!🏁')


# Exercicio 3

n1 = int(input('Digite um número: '))
if n1 % 2 == 0:
    print(f'O número digitado é PAR {n1}')
else:
    print(f'O número digitado é IMPAR {n1}')


# Exercicio 4

print('--Programa para ver qual tipo de Triangulo--')

n1 = float(input('Primeiro lado: '))
n2 = float(input('Segundo lado: '))
n3 = float(input('Terceiro lado: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1+ n2: # Essa condição é uma das principais razões de não formar um triangulo!
    print('Essa condição pode formar um triangulo,', end='')
    if n1 == n2 == n3:
        print('Equilátero!')
    elif n1 != n2 != n3 != n1:
        print('Escaleno!')
    else:
        print('Isósceles!')

print('Fim do Programa!🏁')
    
     
# Exercicio 5

n = int(input('Digite um número: '))

if n % 5 == 0 and n % 7 == 0:
    print(f'O número {n} é multiplo de 5 e 7! ')
else:
    print(f'O número {n} não é multiplo de 5 e 7!')

    
# Exercicio 6

n = int(input('Digite um número: '))
if n >= 0 and n > 10:
    print(f'O número {n} é positivo e maior que 10!')
else:
    print(f'O número {n} é positivo mais não é maior que 10!')


# Exercicio 7

n = int(input('Digite um número: '))

if n % 3 == 0 or n % 5 == 0:
    print(f'O número {n} é divisivel por 3 ou 5!')
else:
    print(f'O número {n} não é divisivel por 3 ou 5!')
    