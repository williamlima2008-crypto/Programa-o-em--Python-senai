# produto = input('produto:')
# valor_ = float(input('R$: '))


produtos = ['','1uva', '2laranja', '3arroz','4feijão']
valor = [0,10.55,8.90,10.70,8.90]
# produtos.append(produto)
# valor.append(valor_)

print(f'''


{produtos[1]} R$ {valor[1]}
{produtos[2]} R$ {valor[2]}
{produtos[3]} R$ {valor[3]}
{produtos[4]} R$ {valor[4]}


''')
escolha_prod1 = int(input('Produto: '))
escolha_prod2 = int(input('Produto: '))
                    
carrinho = []
total = []


carrinho.append(produtos[escolha_prod1])
carrinho.append(produtos[escolha_prod2])
                    
                
total.extend([valor[escolha_prod1],valor[escolha_prod2]])
print('**'*10)
print('R$', round(sum(total),2))                    
print('**'*10)
print(carrinho)                
