# Criando uma classe
class Carro():
    # Este é o método "construtor". Ele é chamado quando um novo objeto é criado.
    # 'self' se refere ao próprio objeto que será criado.
    def __init__(self, marca, modelo, ano, cor):
        # Estes são os ATRIBUTOS. São as características do carro.
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.ligado = False

    # Este é um MÉTODO. É uma ação que o carro pode fazer.
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"O {self.modelo} ligou!")
        else:
            print(f"O {self.modelo} já estava ligado.")

    def descrever(self):
        print(f'Este é {self.modelo} {self.marca} do ano {self.ano} na cor {self.cor}')

    # def ligar(self): e def descrever(self):: São métodos, ou seja, funções que pertencem 
    # à classe. Elas definem o que um objeto Carro pode fazer.


# Criando OBJETOS a partir da classe Carro
meu_civic = Carro(marca="Honda", modelo="Civic", ano=2025, cor="Black")

# Usando os métodos e acessando os atributos dos objetos
meu_civic.descrever()
meu_civic.ligar()


# Exercicio de pratica

# Exercício 1: Classe Livro
import math

class Circulo:
    
    def __init__(self, raio):
        self.raio = raio

    def calcular_perimetro(self):
        perimetro = math.pi * (self.raio ** 2)
        print(f"O raio é {perimetro:.2f}")
    
calculo = Circulo(5)
calculo.calcular_perimetro()

# Exercício 3: Classe ContaBancaria

class ContaBancaria():

    def __init__(self, numero_conta, titular):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor

    def sacar(self, valor):
        if valor < self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

    def consultar_saldo(self):
        print(f"Seu saldo é R$ {self.saldo}.")


conta = ContaBancaria(numero_conta=1234,titular="vini")

conta.depositar(500)
conta.sacar(400)
conta.consultar_saldo()

# Exercício 5: Classe Retangulo

class Retangulo():
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        print(self.altura * self.largura)
    
    def calcular_perimetro(self):
        print(2 * (self.largura + self.altura))


retan = Retangulo(4, 5)
retan.calcular_area()
retan.calcular_perimetro()