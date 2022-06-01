''''
Desenvolva um programa utilizando os recursos que já vimos: if, elif, else, while, for, listas, dicionários.
Não precisa utilizar todos, apenas os que julgar necessários.

Desenvolva um algoritmo que apresente as seguintes opções ao usuário:
1 - Cadastrar um funcionário
2 - Alterar um funcionário
2 - Listar (imprimir) todos os funcionários
3 - Excluir um funcionário
4 - Adicionar um aumento de salário


Sabendo que todos os funcionários cadastrados precisam ter no mínimo os dados: Código do Funcionário, Nome, E-mail, Data de Admissão e Salário.

ATENÇÃO!!!
Essa atividade poderá ser realizada em equipes de até 4 pessoas;
Todos da equipe devem postar no Github e depois encaminhar o link para o professor;
Alguns grupos serão sorteados para apresentar seu código, também será sorteada a pessoa que irá apresentar;
Não haverá ajuda do professor!
'''

from os import remove


lista_de_cadastro = []

opcao = 1
print ('CONTROLE DE FUNCIONÁRIOS')

while opcao !=0:
    print('''O que você deseja fazer?\n
    1 - Incluir funcionário
    2 - Alterar funcionário
    3 - Listar funcionários
    4 - Remover funcionário
    5 - Aumento de salário
    6 - Sair''')
    opcao = int(input("Escolha uma opção:"))
   
    if opcao == 1:
        print('INCLUSÃO DE FUNCIONÁRIO:')
        pessoa = []
        codigo = input('Código do funcionário: ')
        pessoa.append(codigo)
        nome = input('Nome do funcionário: ')
        pessoa.append(nome)
        email = input('E-mail:')
        pessoa.append(email)
        datainicio = str(input('Digite a data de admissão (00/00/00)'))
        pessoa.append(datainicio)
        salario = float(input('Salário do funcionário em R$: '))
        pessoa.append(salario)
        lista_de_cadastro.append(pessoa)

        print('Funcionário Cadastrado')

    if opcao == 2:
       
        print('ALTERAÇÃO DE FUNCIONÁRIO')

    if opcao == 3:
        print('LISTAR FUNCIONNARIOS')

    if opcao ==4:
         print(' REMOVER FUNCIONARIO ')
         remove.pop(removerfunc)
         print('Funcionário removido')

    if opcao == 5:
        print('ALTERAÇÃO DE SALÁRIO')


    elif opcao == 6:
        print('Programa encerrado!')
        break
