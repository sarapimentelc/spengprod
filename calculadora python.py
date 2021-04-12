# Calculadora em Python
print("\n********** Python Calculator *********")

#Aqui ele disse ao programa quais as operações matematicas que o programa tem que fazer
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x/y

#Aqui ele disse quais as mensagens que o programa deve dizer ao usuário
print("\nSelecione o número da operação desejada: \n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

#Aqui ele pede pro usuário escolher qual o tipo de operação
escolha = input("\nDigite sua opção (1/2/3/4): ")

#Aqui ele pede pra que o usuário repasse os dados
num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("\nDigite o segundo número: "))

#Aqui são as condições de acordo com a escolha do usuário para poder dar o resultado
if escolha == '1':
    print("\n")
    print(num1, "+", num2, "=", add(num 1, num 2))
    print("\n")

elif escolha == '2':
    print("\n")
    print(num 1, "-", num2, "=", substract(num1, num2))
    print("\n")

elif escolha == '3':
    print("\n")
    print(num 1, "-", num2, "=", multiply(num1, num2))
    print("\n")
    
elif escolha == '4':
    print("\n")
    print(num 1, "-", num2, "=", divide(num1, num2))
    print("\n")

#Caso o usuário não escolha nenhum número entre 1-4 aparece essa informação
else:
    print("\nOpção Inválida!")
    
