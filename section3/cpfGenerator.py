import re
import random

rangeMults1stDigit = range(10, 1, -1)
result1 = 0
firstDigit = 0
cpf9Digits = ''

for i in range(9):
    cpf9Digits += str(random.randint(0, 9))

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

cpfGenerated = f'{cpf9Digits}{firstDigit}{secondDigit}'
print(cpfGenerated)