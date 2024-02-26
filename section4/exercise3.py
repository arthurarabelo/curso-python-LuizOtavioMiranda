# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

num_acertos = 0

for pergunta in perguntas:
    question = pergunta['Pergunta']
    print(f'Pergunta: {question}')
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i}) {opcao}')

    resposta = input('Escolha uma opção: ')
    resposta_int = None   
    if resposta.isdigit():
        resposta_int = int(resposta)
    
    if resposta_int is not None:
        if resposta_int >= 0 and resposta_int < len(opcoes):
            if opcoes[resposta_int] == pergunta['Resposta']:
                num_acertos += 1
                print('Acertou!')
            else:
                print('Errou!')
        else:
            print('Índice inválido.')
    else:
        print('Opção inválida.')

print(f'Você acertou {num_acertos} de 3.')