# Revisão dia 02/07

# Filter

# lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# # verificar numeros pares
# def numero_par(num):
#     if num % 2 == 0:
#         return True
    
#     return False

# pares = filter(numero_par,lista)
# print(list(pares))

# # verificar numeros impares
# def numero_impar(num):
#     if num % 2 == 1:
#         return True
#     return False

# impar = filter(numero_impar,lista)
# print(list(impar))

# Reduce

# from functools import reduce

# vendas_diarias = [
#     [150, 20, 35],
#     [80, 120],
#     [200, 300, 25]
# ]

# Etapa 1: "Achatar" a lista de listas em uma única lista
# lista_unica = list(reduce(lambda subslista,listarestante: subslista + listarestante, vendas_diarias))
# print(lista_unica)

# Etapa 2: Somar todos os valores da lista única
# valor_total = reduce(lambda x,y: x + y, lista_unica)
# print(valor_total)


