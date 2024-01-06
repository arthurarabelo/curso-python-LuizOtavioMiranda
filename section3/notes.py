# comentários são feitos com '#'
# "comentários" multilinhas são feitos com """ ... """ ou com ''' ... ''' -> são chamados de docstring

'''
    Função print:
        -> Possui quebra de linha e separador espaço por padrão. 
        -> É possível mudar o separador dos argumentos:
            print(1, 2, sep = '')
        -> É possível adicionar final da impressão (substitui o '\n'):
            print(1, 2, end = '')
'''

'''
    Tipos de dados:
        -> Python tem tipagem dinâmica e forte, ou seja, já reconhece o tipo sem que seja preciso o declarar explicitamente.
        -> A função type mostra o tipo que o Python atribuiu à variável: type(1), type('Arthur'), type(1.5)
        -> Os tipos primimitivos (int, string, float, bool) são imutáveis.1

    Coerção/conversão de tipos:
        int('1') -> '1' passa a ser do tipo inteiro.
        float('1.2'), bool('')[False], bool(' ')[True], str(11)...

    Variáveis:
        nome_variavel = expressao
        Exemplo: 
            nome_completo =  'Arthur Araujo Rabelo'
            idade = 20
            maior_de_idade = idade >= 18
'''
