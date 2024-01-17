"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

word = 'Academia'
charsGuessed = ''
numTries = 0

while True:
    numTries += 1
    charDigited = input('Digite apenas uma letra: ')
    word = word.lower()
    charDigited = charDigited.lower()
    if len(charDigited) > 1:
        continue

    if charDigited in word:
        charsGuessed += charDigited

    printedWord = ''
    for char in word:
        if char in charsGuessed:
            printedWord += char
        else:
            printedWord += '*'

    print(f'Palavra secreta: {printedWord}')

    if printedWord == word:
        os.system('clear')
        print(f'You won with {numTries} tries.')
        break
    
    

        
    