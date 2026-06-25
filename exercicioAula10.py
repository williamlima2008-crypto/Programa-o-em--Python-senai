# exercicio 1

# n = 0
# while n <= 1000:
#     print(n)
#     n += 1


# exercicio 2
# 
# lista = []
# i = 0
# while i < 10:
#     nome = input(f'Digite um nome: {i+1} ')
#     lista.append(nome)
#     i += 1
# print('Lista de pessoas')

# i = 0
# while i < len(lista):
#     print(lista[i])
#     i += 1


# ATIVIDADE 2

print('===SISTEMAS DE NOTAS===')

for i in range(3):

    usuario = str(input('Seu login: '))
    senha = str(input('Senha: '))
    if usuario == 'william' and senha == '123':
        print('Seja bem vindo ao sistema!')

        cont = input('Deseja continuar (s)')

    while cont == 's':
        aluno = str(input('Digite nome do aluno: '))
        n1 = float(input('Digte a nota: '))
        n2 = float(input('Digite a nota: '))
        n3 = float(input('Digite a nota: '))
        media = (n1 + n2 + n3) / 3
        print(f'O aluno {aluno} média das notas é {media} ')

        continuar = input('Quer continuar (s/n): ')
        if continuar == 'Nn':
            break
else:
    print('Senha incorreta! conta bloqueada.')
        

