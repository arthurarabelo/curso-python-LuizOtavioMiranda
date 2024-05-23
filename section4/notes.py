"""
Funções: retornam None por padrão
    def functionName(parameters):
        ...

    functionName(args)

Argumentos nomeados e não nomeados(posicional) em funções:
    def soma(x, y):
        print(x + y)

    soma(1, 2) -> argumentos não nomeados/posicionais
    soma(y=2, x=1) -> argumentos nomeados (keyword argument)

*args:
    def soma(*args): -> permite passar vários argumentos
        soma = 0
        for numero in args:
            soma += numero
        return soma
    
    soma(1, 2, 3, 4, 5, 6, 7, 8, 9)

    -> *args empacota os valores em uma tupla (iterável)
    obs.: o código acima só serve para argumentos não nomeados

Higher Order Functions:
    Funções que podem receber e/ou retornar outras funções.

First-Class Functions:
    Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...).

Dict / Dicionário:
    -> Pares de chave e valor.
    -> As chaves podem ser criadas com qualquer tipo imutável.
    -> Os dicionários em si são mutáveis, como as listas.

    Exemplo:
        pessoa = {
            'nome': 'Arthur',
            'sobrenome': 'Araújo Rabelo',
        }

        ou

        pessoa = dict(nome='Arthur', sobrenome: 'Araújo Rabelo')

        print(pessoa['nome']) -> imprime Arthur
        pessoa['idade'] = 20 -> cria nova chave no dicionário
        del pessoa['idade'] -> apaga chave
        pessoa.get('idade') -> se a chave existe, o método get retorna o valor dela; se não existe, retorna None por padrão. 

    Métodos úteis dos dicionários em Python:
        len - quantas chaves
        keys - iterável com as chaves
        values - iterável com os valores
        items - iterável com chaves e valores
        setdefault - adiciona valor se a chave não existe
        copy - retorna uma cópia rasa (shallow copy)
        get - obtém uma chave
        pop - Apaga um item com a chave especificada (del)
        popitem - Apaga o último item adicionado
        update - Atualiza um dicionário com outro

Set (conjunto):
    Sets em Python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno.

    s1 = set() -> vazio
    s1 = {'Luiz', 1, 2, 3} -> com dados
    
    - Sets são eficientes para remover valores duplicados de iteráveis.
    - Não aceitam valores mutáveis;
    - Seus valores serão sempre únicos;
    - não tem índexes;
    - não garantem ordem;
    - são iteráveis (for, in, not in)

    Métodos úteis:
        - add: adiciona *um* valor ao set
        - update: adiciona vários valores ao set.
        - clear: limpa o set
        - discard: descarta um determinado valor do set

    Operadores úteis:
        união | união (union) - Une
        intersecção & (intersection) - Itens presentes em ambos
        diferença - Itens presentes apenas no set da esquerda
        diferença simétrica ^ - Itens que não estão em ambos

Função lambda:
    A função lambda é uma função como qualquer
    outra em Python. Porém, são funções anônimas
    que contém apenas uma linha. Ou seja, tudo
    deve ser contido dentro de uma única
    expressão.

    Exemplo:
        lista = [
            {'nome': 'Luiz', 'sobrenome': 'miranda'},
            {'nome': 'Maria', 'sobrenome': 'Oliveira'},
            {'nome': 'Daniel', 'sobrenome': 'Silva'},
            {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
            {'nome': 'Aline', 'sobrenome': 'Souza'},
        ]

        l1 = sorted(lista, key=lambda item: item['nome'])
        l2 = sorted(lista, key=lambda item: item['sobrenome'])

Empacotamento e desempacotamento de dicts, args e kwargs usando dicionários: aula 135

List comprehension:
    É uma forma rápida de criar listas utilizando iteráveis.

    Exemplo: lista = [numero for numero in range(10)] -> gera uma lista com números de 0 a 9

Dict e set comprehension:
    Aula 141

isinstance(valor, classe) -> diz se um objeto é instância de determinada classe (str, int, float)

Generator: aula 146

Generator functions:

    def genfunction(parameter):
        yield 1 # Pausa a execução da função em 1
        yield 2 # Pausa a execução da função em 2

    print(next(gen)) -> imprime 1
    print(next(gen)) -> imprime 2

    yield from: aula 148

Finally:

    Em blocos try-except, a cláusula finally sempre será executada.

Raise:

    Lança exceções (parecido com o throw)

Módulos:

    import sys
    print(sys.platform)

    from sys import exit, platform
    print(platform)

    import sys as sistema
    print(sistema.platform)

"""
