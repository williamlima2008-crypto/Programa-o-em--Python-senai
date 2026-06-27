# EXERCICIO 1

# print('--ATIVIDADES PARA TRABALHAR COM TRY AND EXCEPT--')
# print('='* 20)


# try:
#     n = int(input('Digite um número: '))
# except ZeroDivisionError as error:
#     print(error)

# except ValueError as erro2:
#     print('Erro no valor da variável')

# except NameError as erro:
#     print(erro)

# finally:
#     print('O sistema foi carregado')


# EXERCICIO 2


# try :
#     n1 = float(input('Qual é o valor? '))
#     n2 = float(input('Qual é o valor? '))
#     d = n1 / n2

# except ZeroDivisionError:
#     print('Nenhum número não pode ser dividido por zero!')

# print('Divisão bem sucedida!')




# EXERCICIO 3


try:
    lista = []
    n = int(input('Digite um número: '))
    lista.append(n)
    print(lista)

except ZeroDivisionError:
    print('Não pode ser dividido')

except TypeError:
    print('Tipo da variavel invalida')

except ValueError as erro:
    print(erro)

except NamError as erro:
    print(erro)
    