# List Comprehension

# Armazenando valores de 0 a 10 em um lista
valores = [x for x in range(11)]
print(valores)

# List Comprehension que imprime os números menores que 5 em um intervalo de 1 a 10
intervalo_5 = [x for x in range(10) if x < 5]
print(intervalo_5)

# Buscando palavra apenas com a letra 'm' na lista
# Lista de Frutas
lista_frutas = ["banana", "maçã", "abacate", "melancia", "cereja", "manga"]
# Lista Nova
lista_nova = []

for item in lista_frutas:
    if "m" in item:
        lista_nova.append(item)
print(lista_nova)

# Selecionando as frutas com List Comprehension
lista = [item for item in lista_frutas if "m" in item]
print(lista)

# Dict Comprehension

# Dicionário de alunos e notas
dict_alunos = {'Bob': 68, 'Michel': 84, 'Zico': 57, 'Ana': 93}

# Criando um novo Dicionario imprimindo os pares chave:valor
# ✅ Significado:
# k: representa a chave (key) de cada item do dicionário.
# v: representa o valor (value) correspondente à chave.
dict_alunos_status = {k:v for (k, v) in dict_alunos.items()}
print(dict_alunos_status)

# Criando um novo Dicionario verificando os alunos reprovados
dict_notas_alunos = {k:('Aprovado' if v > 70 else 'Reprovado') for (k, v) in dict_alunos.items()}
print(dict_notas_alunos)