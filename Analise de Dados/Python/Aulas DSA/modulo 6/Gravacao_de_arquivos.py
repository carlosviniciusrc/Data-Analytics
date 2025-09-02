# Manipulação de Arquivos em Python

# Gravando arquivos

# Abrindo arquivo para gravação
arq2 = open("arquivos/arquivo2.txt", "w") # w = write(escrita)

# Importante: quando o arquivo está no modo de escrita, você não pode utilizar o
# print para exbir o arquivo. Neste caso, você fecha o arquivo com .close(), e ativa
# o modo .read() para ler.

# Gravando informações no arquivo.
arq2.write("Aprendendo a programar em Python.")

# Fechando o arquivo
arq2.close()

#✅ Dica importante:
# Sempre feche o arquivo com arquivo.close() depois de terminar, 
# para liberar o recurso no sistema.

# Agora vamos o usar o "a" para acrescentar(append) informações no arquivo. Não
# esqueca que o "w" ele sobreescreve o arquivo se ele já existir. Para adicionar
# novas informações sempre utilizar o "a".
arq2 = open("arquivos/arquivo2.txt", "a") # a = append

# Acrescentando novas informações
arq2.write("E a metodologia de ensino da Data Science Academy facilita o aprendizado.")

# Fechando o arquivo
arq2.close()

# # Garantindo que o cursor vai voltar para o inicio
# arq2.seek(0,0)

# agora lendo o arquivo completo
arq2 = open("arquivos/arquivo2.txt", "r") # r = read

# Exibindo o arquivo
print(arq2.read())

# Fechando o arquivo
arq2.close()
