# Calculadora 

# Menu de Exibição
def menu():
    print('************* Calculadora *************', end='\n\n')
    print('Selecione o número da operação desejada:', end='\n\n')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão', end='\n\n')


menu()

entrada = int(input('Digite uma opção (1/2/3/4): '))
print()
num1= int(input('Digite o primeiro numero: '))
print()
num2= int(input('Digite o segundo numero: '))
print()

resultado = 0

if entrada == 1:
    resultado = lambda x, y: x + y
    print(resultado(num1,num2))
elif entrada == 2:
    resultado = lambda x, y: x - y
    print(resultado(num1,num2))
elif entrada == 3:
    resultado = lambda x, y: x * y
    print(resultado(num1,num2))
else:
    resultado = lambda x, y: x / y
    print(resultado(num1,num2))