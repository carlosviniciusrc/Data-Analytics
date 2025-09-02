# Função Filter

# A função filter() é uma ferramenta integrada do Python, projetada para criar 
# um novo iterador a partir dos elementos de um iterável existente para os quais 
# uma determinada função retorna True. Em outras palavras, ela permite "filtrar" 
# uma sequência, mantendo apenas os itens que atendem a uma condição específica.

# Criando uma função de números pares

def verificaPar(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
print(verificaPar(5))

# Utilizando Filter

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

numeros_pares = filter(verificaPar,lista)
print(list(numeros_pares))

# Obs: Na função filter ele apenas vai retornar os valores True.

# Ex 2:

alunos = [
    {'nome': 'Ana', 'nota': 9.5},
    {'nome': 'Bruno', 'nota': 6.8},
    {'nome': 'Carla', 'nota': 7.0},
    {'nome': 'Daniel', 'nota': 5.2},
    {'nome': 'Elisa', 'nota': 8.4}
]

# A função lambda acessa a nota de cada aluno e verifica a condição
alunos_aprovados = filter(lambda aluno: aluno['nota'] >= 7.0, alunos)

print('\nAlunos aprovados:')
for aluno in alunos_aprovados:
    for chave, valor in aluno.items():
        print(f'{chave}: {valor}')
    print('---')
