'''
Faça um algoritmo para ler 20 números e armazenar em um vetor. Após a leitura total dos 20 números, o algoritmo deve escrever esses 20 números lidos na ordem inversa.
'''

import random

n=[]
for c in range(1,21):
    n.append(random.randint(1,1000))
print(n)

for y in range (0, len(n)):
     maior_numero = n[y]
     maior_indice = y

     for x in range ((y+1), len(n)):
         if n[x]>= maior_numero:
             maior_numero=n[x]
             maior_indice = x
     n.insert(y, n.pop(maior_indice))
print (n)

            
