"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpfGiven = input('Digite o CPF: ')
cpf = ''
cpf9Digits = ''
rangeMults1stDigit = range(10, 1, -1)
result1 = 0
firstDigit = 0

for char in cpfGiven:
    if char.isdigit():
        cpf += char
    else:
        continue

cpf9Digits = cpf[:9]

index  = 0
while index < len(cpf9Digits):
    cpfCurrentDigit = int(cpf9Digits[index])
    prod = cpfCurrentDigit * rangeMults1stDigit[index]
    result1 += prod
    index += 1
    

result1 *= 10
result1 %= 11

if result1 <= 9:
    firstDigit = result1

print(f'O primeiro dígito do CPF é {firstDigit}')

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

cpf10Digits = cpf9Digits + str(firstDigit)
rangeMults2ndDigit = range(11, 1, -1)
result2 = 0
secondDigit = 0

index  = 0
while index < len(cpf10Digits):
    cpfCurrentDigit = int(cpf10Digits[index])
    prod = cpfCurrentDigit * rangeMults2ndDigit[index]
    result2 += prod
    index += 1

result2 *= 10
result2 %= 11

secondDigit = result2 if result2 <= 9 else secondDigit

print(f'O segundo dígito do CPF é {secondDigit}')

cpfCorrect = f'{cpf9Digits}{firstDigit}{secondDigit}'

if cpfCorrect == cpf:
    print(f'{cpfGiven} é válido.')
else:
    print('CPF inválido.')