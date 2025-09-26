## Programação com Acesso a Banco de Dados
# Revisão de Orientação a Objetos
# Prof. Guilherme Leal Santos
'''
frutas = ['Maça' , 'Banana' , 'Laranja'] # Lista de frutas
print(frutas)
print(frutas[0])
print(f'Quantidade de frutas: {len(frutas)}')

frutas.append('Uva') # Adiciona um elemento ao final da lista
print(frutas)

frutas.insert(1, 'Abacaxi') # Adiciona um elemento na posição desejada
print(frutas)

#frutas = frutas.pop() # Remove o último elemento da lista
#frutas = frutas.pop(-1) # Remove o último elemento da lista
# frutas = frutas.pop(0) # Remove elemento da posição desejada
# print(f'Removida: {frutas}')
# print(frutas)

frutas.remove('Uva') # Remove o elemento desejado
print(frutas)

numeros = [5, 3, 8, 1, 4]
print(numeros)

numeros_ord_c = sorted(numeros) # Ordena a lista em ordem crescente
print(f'Ordenada (c) : {numeros_ord_c}')

numeros_ord_d = sorted(numeros, reverse=True) # Ordena a lista em ordem decrescente
print(f'Ordenada (d) : {numeros_ord_d}')

numeros_dobrados = []
for n in numeros:
    numeros_dobrados.append(n * 2) # Dobra o valor de cada elemento da lista
print(f'Números dobrados: {numeros_dobrados}')
numeros_dobrados = list(map(lambda n: n * 2, numeros)) # Dobra o valor de cada elemento da lista usando map e lambda
print(f'Números dobrados (map): {numeros_dobrados}')

#numeros_filtrados = []
#for n in numeros:
#    if n > 4:
#        numeros_filtrados.append(n) # Filtra os números maiores que 4
#print(f'Números filtrados: {numeros_filtrados}')
numeros_filtrados = list(filter(lambda n: n > 4, numeros)) # Filtra os números maiores que 4 usando filter e lambda
print(f'Números filtrados (filter): {numeros_filtrados}')

soma = 0 
for n in numeros:
    soma += n # Soma todos os elementos da lista
print(soma)

from functools import reduce
soma = reduce (lambda soma, n: soma + n, numeros) # Soma todos os elementos da lista usando reduce e lambda
print(soma)'''
    
    
# Aula 19/09 - Orientação a Objetos
from conta import Conta
from cliente import Cliente

cliente1 = Cliente('Elvis Presley', '111.222.333-44')
conta1 = Conta(cliente1, 1, 123, 'elvis@gmail.com', 12345678)
conta1.extrato()
# conta1.deposita(100)
# conta1.extrato()

# conta2 = conta1
# conta2.extrato()
# conta2.saca(100)
# conta2.extrato()
# conta1.extrato()

# if(conta1.saca(1000)):
#     print('OK')
# else:
#     print('Tá Liso')

cliente2 = Cliente('Jonhny Cage', '222.333.444-55')
conta2 = Conta(cliente2, 2, 234, 'jonhnny@outlook.com', 234567)
conta2.extrato()

if(conta2.transfere(conta1, 1000)):
    print('OK')
else:
    print('Tá liso')



