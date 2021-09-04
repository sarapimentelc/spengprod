
lista = [1, 10]
try:
    divisao = 10/0
    numero = lista[1]
    #x = a
except ZeroDivisionError:
    print('Não é possivel realizar uma divisão por zero')
except ArithmeticError:
    print('Houve um erro ao realizar a operação aritmetica.')
except IndexError:
    print('Erro ao acessar um indices invalido da lista')
except Exception as ex:
    print('Erro desconhecido. Erro: {}' .format(ex))
else:
    print('Executa quando não houver exceção')