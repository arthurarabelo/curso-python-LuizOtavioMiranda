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
"""