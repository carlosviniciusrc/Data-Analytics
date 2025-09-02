# Revisão dia 09/06

# Manipulação de arquivos em Py

# Criando arquivo
data = open("teste1.txt", "w", encoding="utf-8")

# Colocando informação na criação
data.write('Olá, Seja bem-vindo.\n')
data.close()

# Acrescentando mais informações
data = open("teste1.txt", "a", encoding="utf-8")
data.write('Meu nome é Vinicius')
data.close()

# Leitura do arquivo
data = open("teste1.txt", "r", encoding="utf-8")
print(data.read())

# exibindo o numero de caracteres
print(data.tell())

# Retornado o cursor da leitura para o inicio
data.seek(0,0)

# Fechando o arquivo
data.close()