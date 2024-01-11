"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numStr = input('Digite um número inteiro: ')
if numStr.isdigit():
    numInt = int(numStr)
    r = numInt % 2
    if r == 0:
        print('Número par.')
    else:
        print('Número ímpar.')
else:
    print(f'{numStr} não é um número inteiro.')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horaStr = input('Que horas são? ')
horaFloat = float(horaStr)
if horaFloat >= 0 and horaFloat <= 11:
    print('Bom dia')
elif horaFloat >= 12 and horaFloat <= 17:
    print('Boa tarde')
else:
    print('Boa noite')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

firstName = input('Digite seu primeiro nome: ')
if len(firstName) <= 4:
    print('Seu nome é curto.')
elif len(firstName) <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.') 