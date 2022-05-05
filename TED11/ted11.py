'''
Consutra uma matriz A de tamanho 10 x 10 com valores inteiros e randômicos. Depois:
Imprima o resultado da soma de todos os valores da matriz no terminal;
E, criei uma nova matriz B, no qual cada item seja o valor da matriz A * 3;

'''

import random
from re import M

m=[]
for c in range (0,10):
    m2=[]
    m2.append(random.randint(0,1000))
   
    for d in range (0,10):
        m2.append(random.randint(0,1000))
    m.append(m2)

for linha in m:
    print(linha)

resultado_soma = 0

for l in m:
    
    for c in l:
        
        resultado_soma += c

print(f'Resultado da Soma = {resultado_soma}')

matriz_b = []

for l in range(0, len(m)):
    
    lista_auxiliar = []
    
    for c in range(0, len(m[l])):
        
        resultado_multiplicacao = m[l][c] * 3
        lista_auxiliar.append(resultado_multiplicacao)
        
    matriz_b.append(lista_auxiliar)
        
print(matriz_b)

