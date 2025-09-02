# Expressões regulares

# Expressões regulares são padrões usados para combinar ou encontrar ocorrências 
# de sequências de caracteres em uma string. Em Python, expressões regulares são 
# geralmente usadas para manipular strings e realizar tarefas como validação de 
# entrada de dados, extração de informações de strings e substituição de texto.

# o módulo re é a nossa porta de entrada para trabalhar com expressões regulares.
# Com ele, podemos:

# 1.Verificar se um padrão existe em um texto.
# 2.Extrair todas as ocorrências de um padrão de um texto.
# 3.Substituir partes de um texto que correspondem a um padrão.
# 4.Dividir um texto com base em um padrão.
import re

texto = "Meu e—mail é exemplo@gmail.com e você pode me contatar em outro email@yahoo.com."

# Expressão regular para contar os caracteres arroba que aparecem no texto
# A função re.findall() (que vem de "find all", ou "encontrar todos") varre uma 
# string da esquerda para a direita e encontra todas
resultado1 = len(re.findall("@", texto))
print(resultado1)

# Expressaõ regular para extrair a palavra que aparec3e após a palavra "você" em um texto.
# Para entender a linha, vamos dividi-la em suas três partes principais:

# 1.A função: re.findall()
# 2.O padrão (a expressão regular): r'você (\w+)'
# 3. O alvo: a variável texto

# A letra r no início indica que esta é uma raw string (string bruta). 
# É uma boa prática usar isso em expressões regulares para que o Python 
# não interprete caracteres como \ (barra invertida) de maneira especial.

# \w: É um metacaractere que corresponde a qualquer "caractere de palavra". 
# Isso inclui:

# 1. Letras de 'a' a 'z' (maiúsculas e minúsculas).
# 2. Números de '0' a '9'.
# 3. O caractere de sublinhado _.

# +: É um quantificador que significa "uma ou mais vezes". Portanto, \w+ 
# significa "encontre uma ou mais letras/números/sublinhados em sequência",
#  o que, na prática, corresponde a uma palavra inteira.

resultado2 = re.findall(r'você (\w+)', texto)
# Como ele captura como lista, vamos apenas selecionar o resultado que queremos.
print(resultado2[0])

# Expressão regular para extrair endereços de e—mail de uma string
email = re.findall(r"[\w.-]+@(?:[\w-]+\.)+[a-zA-Z]{2,}", texto)

for item in email:
    print(item)