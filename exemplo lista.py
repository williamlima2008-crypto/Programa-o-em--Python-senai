print('SISTEMA DE NOTAS')
# Lista de notas vazias
nomes = []
notas = []
nome1 = str(input('Nome:'))
n1 = float(input('nota:'))
nomes.append(nome1)
notas.append(n1)


nome2 = str(input('Nome:'))
n2 = float(input('nota:'))
nomes.append(nome2)        
notas.append(n2)


nome3 = str(input('Nome:'))            
n3 = float(input('nota:'))
nomes.append(nome3)
notas.append(n3)


print(nomes)
print(notas)

posicao_maior_nota = notas.index(max(notas))
print('Aluno com a maior nota', nomes[posicao_maior_nota])


