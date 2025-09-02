# Fazendo split dos dados
def separador_de_strings(text):
    return text.split(" ")

texto = "Esta função será bastante útil para separar grandes volumes de dados"

# Isso divide a string em uma lista de palavras
print(separador_de_strings(texto))


# ✅ O que é "token" em Python?
# Em programação, um "token" é simplesmente uma unidade básica de informação.
# No contexto de Python e processamento de texto, token significa:
# → Cada palavra, símbolo ou pedaço que você extrai de uma string.

# ✅ Exemplo clássico: "Tokenização"
# Tokenização → Processo de dividir um texto em tokens (palavras, 
# frases ou símbolos).
token = separador_de_strings(texto)
print(token)


def separador_de_strings_maisculas(text):
    texto = text.upper()
    for letra in texto:
        print(letra)

separador_de_strings_maisculas(texto)