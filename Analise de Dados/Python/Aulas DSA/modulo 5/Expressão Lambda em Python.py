# Expressão Lambda

# definindo uma função em 3 linhas
def potencia(num):
    resultado = num ** 2
    return print(resultado)

potencia(2)

# definindo uma função em 2 linhas
def potencia2(num):
    return print(num ** 2)

potencia2(2)

# definindo uma função em uma linhas
def potencia3(num): return print(num ** 2)
potencia3(5)

# Definindo uma expressão lambda (Função anônima)
potencia_lam = lambda num: num ** 2
print(potencia_lam(6))

# Verificando se o numero é par
par = lambda x: x % 2 == 0
print(par(2))

# Pegando a primeira letra da string
first = lambda s: s[0]
print(first('Vinicius'))

# Revertendo a string por completo
reverse = lambda s: s[::-1]
print(reverse('Python'))

# Soma de dois valores
soma = lambda x,y: x + y
print(soma(1,2))