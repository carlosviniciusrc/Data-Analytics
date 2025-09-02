# Função reduce
# A função reduce0 em Python é uma função da biblioteca functools que aplica 
# uma determinada função binária  a pares consecutivos de elementos em uma  
# estrutura de dados iterável (como uma lista, tupla ou outro objeto iterável), 
# reduzindo-a a um único valor.

# Para utilizar a função reduce(), primeiro você precisa importá-la 
# do módulo functools:
from functools import reduce

lista = [47, 11, 42, 13]

# Utilizando Def
def soma(x,y):
    z = x + y
    return z

redu = reduce(soma, lista)
print(redu)

# Utilizando lambda

redu2 = reduce(lambda x, y: x + y, lista)
print(redu2)

# verificando o maior da lista
maior_valor_da_lista = lambda a,b: a if (a > b) else b

verificador = reduce(maior_valor_da_lista, lista)

print(verificador)
