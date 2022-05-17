''''
Desenvolva os algoritmos abaixo em linguagem Python. Utilize o VS Code ou Pycharm, mas ao final entregue ao professor um arquivo .py para cada questão desenvolvida. As atividades deverão ser entregues no Github.
Um dicionário Python pode ser usado para modelar um dicionário de verdade. No entanto, para evitar confusão, chame este dicionário de glossário.
Pense em cinco palavras relacionada à programação que você conheceu nesta disciplina. Use estas palavras como chaves em seu glossário e armazene seus significados como valores.
Mostre cada palavra e seu significado em uma saída, formate a saída de uma forma bem elegante. Por exemplo: você pode exibir a palavra seguida de dois-pontos e depois o seu significado, ou apresentar a palavra em uma linha e então exibir seu significado identado em uma segunda linha. Utilize o caractere de quebra de linha (\n) para inserir uma linha em branco entre cada par palavra-significado em sua saída.
Sugestões de termos: Algoritmos, Python, Webscraping, Lógica de Programação, Google Colab, Visual Studio Code.
'''

termos = {

    'Import' : {'expressão': 'Import', 'sig': 'Meio para importação de módulos. É ele quem torna visível os módulos para o arquivo no qual foi chamado. Por exemplo, para importar o módulo math, que é um módulo que nos dá acesso a várias funções matemáticas'},

    'For' : {'expressão': 'For', 'sig': 'É uma das estruturas de repetições disponíveis na linguagem que permite a execução de um mesmo comando até que uma determinada condição seja atendida.'},

    'Python': {'expressão': 'Python', 'sig': 'É uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte.'},

    'Print' : {'expressão': 'Print', 'sig': 'É classificada como função. Seu papel é, basicamente, exibir mensagens na tela ou enviá-las para outro dispositivo, como imprimir dentro de arquivos de texto.'},

    'String' : {'expressão': 'String', 'sig' : 'Conjuntos de caracteres de texto que podem ser compreendidos como representações de informações escritas dentro de um código.'}

}

for x in termos:
    palavra = termos[x]['expressão']
    sentido = termos[x]['sig']

    print(f'O termo {palavra} significa: \n {sentido}')
    print('-=-' * 30)

