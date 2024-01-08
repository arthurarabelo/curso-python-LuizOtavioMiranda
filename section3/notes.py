# comentários são feitos com '#'
# "comentários" multilinhas são feitos com """ ... """ ou com ''' ... ''' -> são chamados de docstring

'''
    Função print:
        -> Possui quebra de linha e separador espaço por padrão. 
        -> É possível mudar o separador dos argumentos:
            print(1, 2, sep = '')
        -> É possível adicionar final da impressão (substitui o '\n'):
            print(1, 2, end = '')
            
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

    Operadores aritméticos:
        divisão inteira: //
        exponenciação: **
        -> O operador + concatena strings também.
        -> O operador * também faz a repetição de uma string.
        -> Precedência de operadores:
            1. (x + y)
            2. **
            3. *, /, //, %
            4. +, -

    fStrings (formatação de string):
        str = f'{variavel}...{outra variavel}'
        -> Formatar casas decimais de um número: f'{variavel do numero:.xf}...', sendo x o número de casas.
        -> É possível colocar vírgula para dividir o número: f'{variavel do numero:,.xf}...'.   

    Format:
        str.format() -> format é um método do objeto string

    Função input:
        Exemplo: 
        nome = input('Qual é o seu nome?') -> nome é do tipo string

    Operações condicionais:
        if [expressao]:
            ...
        elif [expressao]:
            ...
        else:
            ...
        
    Operadores lógicos:
        && -> and
        || -> or
        ! -> not

        Falsy: 0, 0.0, '', False

    Operadores in e not in:
        Exemplo:
            nome = 'Arthur'
            print('r' in nome) -> retorna True
    
    Interpolação básica de strings:
        s - string
        d e i - int
        f - float
        x e X - hexadecimal (ABCDEF0123456789)
'''
