"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista = []

while True:
    opt = (input('Selecione uma opção \n'
          '[i]nserir [a]pagar [l]istar \n').lower())[0]
    
    if opt == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opt == 'a':
        os.system('clear')
        try:
            i = int(input('Escolha o índice para apagar: '))
            del lista[i]
        except ValueError:
            print('Digite um número inteiro')
        except IndexError:
            print('Índice não existe')
    elif opt == 'l':
        os.system('clear')
        if len(lista) == 0:
            print('Lista vazia')
            continue
        enumerateLista = list(enumerate(lista))
        for indice, valor in enumerateLista:
            print(indice, valor)
    else:
        os.system('clear')
        print('Opção inválida.')
        continue
        