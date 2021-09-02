class Calculadora:
    def __init__(self, num1, num2):
        pass

    def soma (self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao (self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

calculadora = Calculadora()
print(calculadora.soma(10,2))
print(calculadora.subtracao(20,14))
print(calculadora.subtracao(5,3))
print(calculadora.multiplicacao(100,30))
print(calculadora.divisao(12,20))
