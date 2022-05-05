'''
Faça um algoritmo para ler 50 números e armazenar em um vetor VET, verificar e escrever se existem números repetidos no vetor VET e em que posições se encontram.
'''

import random

lista=[]
for c in range (0,50):
    lista.append(random.randint(1,1000))
print(lista)

for i in range (0, len(lista)):
    print(f'valor testado:{lista[i]} | indice testado: {i}')
    
    for j in range(0, len(lista)):
        if lista[i] == lista [j] and i != j:
            print(f'indice: {j} | valor: {lista[j]} \n')
