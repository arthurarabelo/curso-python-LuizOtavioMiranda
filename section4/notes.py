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

"""