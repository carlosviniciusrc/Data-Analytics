# Função Map
# A função map em Python é uma função que aplica uma determinada função 
# a cada elemento de uma estrutura de dados iterável (como uma lista, tupla ou
# outro objeto iterável). A função mapo retorna um objeto que pode ser convertido 
# em outra estrutura de dados, como uma lista, se necessário.

# Função de potencia
def potencia(x):
    return x ** 2

# lista de numeros
numeros = [1, 2, 3, 4 ,5]

# Atribuindo a função Map()
numeros_ao_quadrado = list(map(potencia, numeros))

print(numeros_ao_quadrado)

# Outro exemplo
def fahrenheit(t):
    return ((float(9)/5) * t + 32)

# lista de temperaturas
temperatura = [0 , 22.5, 40, 100]
temperaturas_convertidas = list(map(fahrenheit, temperatura))
print(temperaturas_convertidas)

# Exemplo com lambda

# somando duas listas

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

soma = list(map(lambda x,y: x + y, a, b))

print(soma)

