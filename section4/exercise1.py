# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args):
    produto = 1
    for numero in args:
        produto *= numero
    return produto

variavel = multiplica(2, 2, 2, 2, 2, 2)
print(variavel)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def evenOrOdd( a):
    if(a % 2 == 0):
        return f'{a} is even'
    else:
        return f'{a} is odd'

print(evenOrOdd(5))
