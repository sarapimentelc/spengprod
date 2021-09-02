# conjunto = {1, 2, 3, 4}
# conjunto.add(5)
# conjunto.discard(2)
# print(conjunto)

# conjunto = {1, 2, 3, 4, 5}
# conjunto2 = {5, 6, 7, 8}
#
# conjunto_uniao = conjunto.union(conjunto2) #união
# print('União: {}' .format(conjunto_uniao))
#
# conjunto_interceccao = conjunto.intersection(conjunto2) #intersecção
# print('Interceção: {}' .format(conjunto_interceccao))
#
# conjunto_diferenca1 = conjunto.difference(conjunto2) #diferença
# conjunto_diferenca2 = conjunto2.difference(conjunto)
# print('Diferença entre 1 e 2: {}' .format(conjunto_diferenca1))
# print('Diferença entre 2 e 1: {}' .format(conjunto_diferenca2))
#
# conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2) #diferença simetrica
# print('Diferença simétrica {}' .format(conjunto_diff_simetrica))

# conjunto_a = {1, 2, 3}
# conjunto_b = {1, 2, 3, 4, 5}
#
# conjunto_subset = conjunto_b.issubset(conjunto_a) #pergunta se é subconjunto do outro
# print('A é subconjunto de B: {}' .format(conjunto_subset))
#
# conjunto_superset = conjunto_b.issuperset(conjunto_a)
# print('B é um superconjunto de A: {}' .format(conjunto_superset))

lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print(lista)

conjunto_animais = set(lista) #transformar para conjunto
print(conjunto_animais)

lista_animais = list(conjunto_animais) #transformar para lista
print(lista_animais)