# with open("arquivos/arquivo2.txt", "r") as arq:
#     data = arq.read()
#     rows = data.split('\n')
#     print(rows)

#     full_data = []

#     for row in rows:
#         split_row = row.split(',')
#         full_data.append(split_row)

#     #print(full_data)

# # para saber o numero de colunas

# count = 0
# primeira_linha = full_data[0]

# for columm in primeira_linha:
#     count += 1

# #print(count)

# # iterando elementos

# iteravel = 0

# for lista in full_data:
#     for info in lista:
#         print(lista[iteravel])
#         iteravel += 1
    
#     iteravel = 0

# teste 2

import os

texto = "Cientista de dados pode ser uma excelente alternativa de carrreira.\n"
texto = texto + "Esses profissionais precisam saber como programar em Python. "
texto += "E, claro, devem ser proficientes em Data Science. "

print(texto)

# Criando arquivo
# os.path.join(...) é usado para montar caminhos de forma portável entre 
# sistemas operacionais (Linux, Windows, macOS). Por exemplo:
# Em Linux/Mac: 'arquivos/cientistas.txt'
# Em Windows: 'arquivos\\cientistas.txt'

# Embora nesse caso o caminho já pareça simples, usar os.path.join() 
# é uma boa prática para garantir compatibilidade.

arquivo = open(os.path.join('arquivos/cientistas.txt'), 'w')

# Gravando dados no arquivo
# O split sem parametro faz a separação por espaço

for palavra in texto.split():
    arquivo.write(palavra + ' ')

# fechando o Arquivo
arquivo.close()

# Lendo o Arquivo
arquivo = open("arquivos/cientistas.txt", "r")
conteudo = arquivo.read()
arquivo.close()

print(conteudo)

