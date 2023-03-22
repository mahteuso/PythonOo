from collections import defaultdict, Counter


lista = [3, 2, 1, 5, 8, -1]
lista_2 = [5, 4, 3, -1, 10]
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
for i, l in enumerate(lista):
    for j, m in enumerate(lista):
        if l < m:
            temp = lista[i]
            lista[i] = lista[j]
            lista[j] = temp
            print(lista)
    print("out second for")
    print(lista)

print('Second ordination:')

for i in range(len(lista)):
    for j, m in enumerate(lista):
        if lista[i] < lista[j]:
            temp = lista[i]
            lista[i] = lista[j]
            lista[j] = temp
            print(lista)
    print('out second for')
    print(lista)

'''

