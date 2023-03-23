from collections import defaultdict, Counter
import time


lista = [3, 2, 1]
lista_2 = [5, 4, 3, -1, 10]
'''
print(set(lista) ^ set(lista_2))

phrases = 'Tomorrow I go to the shopping and after I will play soccer with my friends'
new_phrases = phrases.lower().split()
print(new_phrases)
letter_dic = defaultdict(int)
for letter in new_phrases:
    letter_dic[letter] += 1
print(letter_dic)

print(Counter(new_phrases))

print(Counter('banana'))
'''

lista = list(range(10000000))
lista.reverse()
t1 = time.time()
print('using function native sort()')
lista.sort()
#print(lista)
tempoExec = time.time() - t1
print(f"Tempo de execução: {tempoExec} segundos")

t1 = time.time()
print('')
# código aqui
print('first ordination')
lista = list(range(10000))
lista.reverse()
for i, l in enumerate(lista):
    for j, m in enumerate(lista):
        if l < m:
            temp = lista[i]
            lista[i] = lista[j]
            lista[j] = temp
#print(lista)


print('\n')
tempoExec = time.time() - t1
print(f"Tempo de execução: {tempoExec} segundos")

print('')
print('Second ordination:')
lista = list(range(10000))
lista.reverse()
t1 = time.time()
for i in range(len(lista)):
    for j, _ in enumerate(lista):

        if lista[i] < lista[j]:
            temp = lista[i]
            lista[i] = lista[j]
            lista[j] = temp
#print(lista)
tempoExec = time.time() - t1
print(f"Tempo de execução: {tempoExec} segundos")

