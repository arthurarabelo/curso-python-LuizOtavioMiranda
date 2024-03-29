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

        Exemplo:
            nome = 'Arthur'
            preco = 100.50
            variavel = '%s, o preço é R$ %f' % (nome, preco)
            print(variavel) -> Arthur, o preço é R$ 100.50

            Obs: é possível mudar o número de casas decimais após a % (%.2f ou %08X, por exemplo).

    F-strings:
        Aula 45 mostra mais ferramentas.
        
    Fatiamento de strings:
        Fatiamento [i:f:p] [::] -> i: inicio, f: final, p: passo

        str = 'Ola mundo'
        print(str[4:]) -> imprime 'mundo'
        print(str[4:7]) -> imprime 'mun' (indice final não é incluído)
        print(str[0:9:2]) -> imprime 'Oamno'
        print(str[::-1]) -> imprime 'odnum alO'

        Obs.: a função len retorna a qtd 
        de caracteres da string

    Try & Except:
        Aula 49 introduz.

    Identidade de um valor na memória:
        v1 = 'a'
        id(a) -> identidade da variável v1

    is e is not:
        -> Geralmente utilizado com None
        is -> ==
        is not -> !=

    Tipos built-in: 
        -> Tipos embutidos no python
        -> Documentação do python: https://docs.python.org/pt-br/3/library/stdtypes.html
        -> Tipos imutáveis: str, int, float, bool

    Estruturas de repetição:
        while condicao:
            ...
            if condicao2:
                continue
            if condicao3:
                break
                
       -----------------
        str  =  'Arthur'
        for letra in str:
            print(letra)

        -> range:
            range(start, stop, step)
        -> for + range:
            numeros = range(5, 10)
            for numero in numeros:
                print(numero) -> imprime do 5 até o 9
        -> iterador e iterável:
            Iterável -> str, range, etc (__iter__)
            Iterador -> quem sabe entregar um valor por vez
            next -> me entregue o próximo valor
            iter -> me entregue seu iterador

            -> Funcionamento do for:

            texto = 'Luiz'  # iterável

            # iterador = iter(texto)  # iterator

            # while True:
            #     try:
            #         letra = next(iterador)
            #         print(letra)
            #     except StopIteration:
            #         break

    List:
        type: list
        lista = [123, True, 'Arthur', 4.5, ['Outra lista']]
        print(lista[2]) -> imprime 'Arthur'
        lista[2] = 'Emily' -> altera o valor do índice 2 da lista

        -> Tipo mutável
        -> Suporta vários valores de qualquer tipo
        -> del lista[2] - deleta valor da lista e reorganiza os índices
        -> lista.append(50) - adiciona 50 ao final da lista
        -> lista.pop() - remove o último elemento da lista e retorna o valor dele
        -> lista.pop(i) - remove o i-ésimo elemento da lista e retorna o valor dele
        -> lista.clear() - remove todos os elementos da lista
        -> lista.insert(i, v) - insere no i-ésimo índice da lista um elemento de valor
        -> É possível fazer a concatenação de duas ou mais listas com o operador +
        -> O método extend concatena listas mexendo diretamente na lista que o chama
        -> O for funciona do mesmo modo com listas

    Cuidados com dados mutáveis:
        Exemplo:
            lista_a = ['Arthur', 'Emily']
            lista_b = lista_a 

            -> As duas variáveis irão compartilhar o mesmo valor na memória: se eu alterar
               uma delas, ambas são alteradas
            -> O método lista_a.copy() retorna uma nova lista igual a lista_a, criando duas listas separadas
    
    Desempacotamento:
        nomes = ['Arthur', 'Emily', 'Vitor']
        nome1, nome2, nome3 = nomes]
        nome1, nome2, nome3 = ['Arthur', 'Emily', 'Vitor']

        -> pode-se pegar apenas 1 dos valores:
            nome1, *resto = ['Arthur', 'Emily', 'Vitor'] - resto vai ser outra lista com o restante dos valores
            É convenção chamar uma variável inútil de _ : nome1, *_ = ['Arthur', 'Emily', 'Vitor']
            _, nome2, *_ = ['Arthur', 'Emily', 'Vitor']

    Tuplas:
        Uma tupla é uma lista imutável.
        type: tuple

        tupla = 'Maria', 'José', 'Jesus'
        tupla = ('Maria', 'José', 'Jesus')

    Enumerate:
        nomes = ['Arthur', 'Emily', 'Vitor']
        lista_enumerada = enumerate(nomes) -> enumerate object (iterator) - next(lista_enumerada) é (0, 'Arthur')
        
        -> um objeto enumerate é basicamente um ponteiro: depois de percorrer toda a lista enumerada, o
           ponteiro aponta para outra caixinha de memória que não seja aquelas que guardam os valores da lista.
        -> enumerate(nomes) aponta para uma caixinha de memória que funciona como um cabeçalho para a lista enumerada.
        -> pode-se converter um enumerate object para uma lista ou uma tupla.

    Imprecisão de ponto flutuante:
        -> pode-se contornar esse problema usando f-strings ou a função round:
            round(numero, numero de casas decimais) - float type
        -> módulo decimal:
            import decimal
            numero = decimal.Decimal('float number') - argumento é passado como string

    Split, Join, Strip (Aula 93):
        split - divide uma string (list)
        join - une uma string
        strip - corta os espaços do começo e/ou do final de uma string

    Operação ternária (condicional de uma linha):
        <valor> if <condicao> else <outro valor>

'''
