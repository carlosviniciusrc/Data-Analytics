# Manipulação de Arquivos em Python

# Lendo arquivos

# A função open() serve para abrir arquivos no Python, 
# retornando um objeto que representa esse arquivo.

# Abrindo o arquivo para leitura
arq1 = open("arquivos/arquivo1.txt", "r") # r = read
# Lendo o arquivo
print(arq1.read())

# Importante: Quando você lê um arquivo em python ele utiliza um cursor para fazer
# a leitura, ao finalizar a leitura o cursor sempre ira para o final do arquivo.
# Para trazer novamente o cursor utilizamos o metodo .seek().

# Parâmetros importantes:
# Modo 	 Descrição
# 'r' 	 Leitura. O arquivo deve existir.
# 'w' 	 Escrita. Cria ou sobrescreve.
# 'a' 	 Acrescentar. Adiciona ao final do arquivo.
# 'b' 	 Binário. Usado com imagens, por exemplo.
# '+' 	 Leitura e escrita. Ex.: 'r+'.

# Contar o número de caracteres
# tell() retorna a posição atual do cursor de leitura/escrita, em bytes.
print(arq1.tell())


# seek() move o cursor para uma posição específica no arquivo.

# Sintaxe:
# arquivo.seek(posicao, referencia)

# posicao: número de bytes a se mover.
# referencia (opcional):

# 0 → desde o início (padrão).
# 1 → a partir da posição atual.
# 2 → a partir do final do arquivo.

# Retornando para o inicio do arquivo
print(arq1.seek(0,0))

arq1.close()