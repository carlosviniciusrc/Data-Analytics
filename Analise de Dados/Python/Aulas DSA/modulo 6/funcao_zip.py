# Função Zip

# A função zip() é uma das ferramentas mais úteis e elegantes do Python 
# para se trabalhar com múltiplas sequências de dados.

# Imagine que você tem duas ou mais listas (ou qualquer outro iterável, 
# como tuplas) e quer "costurá-las" juntas, item por item. A função zip() 
# faz exatamente isso: ela pega um elemento de cada iterável e os agrupa em 
# uma tupla.

# Vamos começar com o caso mais simples: combinar duas listas.

nomes = ['Ana', 'Bruno', 'Carla']
idades = [28, 35, 22]

combinacao = list(zip(nomes, idades))

# Importante: zip() retorna um objeto 'zip', que é um iterador.
# Para ver o resultado, precisamos convertê-lo para uma lista.
for n, i in combinacao:
    print(f'nome: {n}, idade: {i}')

# Comportamento com Listas de Tamanhos Diferentes

# Caso os iteraveis forem de tamanhos diferentes, ele vai iterar os itens correspondentes
# e o restante vai descartar

produtos = ['Café', 'Açúcar', 'Leite', 'Pão']
precos = [15.50, 4.20] # A lista de preços é menor

mercado = list(zip(produtos,precos))
print(mercado)


# Resumo:

# zip() agrupa elementos de múltiplos iteráveis em tuplas.

# Ela retorna um iterador, então você geralmente o converte para uma list 
# ou dict, ou o usa em um loop for.

# Ela para quando o menor iterável termina.

# É fantástica para iterar em paralelo e para criar dicionários.

# Use zip_longest se precisar incluir todos os elementos do iterável mais longo.