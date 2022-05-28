import time

print('explicando')
print()
time.sleep(3)
gabarito = {
    'Pergunta 1': {
        'Pergunta': 'x',
        'respostas': {
            'a': 'x',
            'b': 'x',
            'c': 'x',
            'd': 'x',
        },
        'resposta_certa': 'x',
    },
    'Pergunta 2': {
        'Pergunta': 'x',
        'respostas': {
            'a': 'x',
            'b': 'x',
            'c': 'x',
            'd': 'x',
        },
        'resposta_certa': 'x',
    },
    'Pergunta 3': {
        'Pergunta': 'x',
        'respostas': {
            'a': 'x',
            'b': 'x',
            'c': 'x',
            'd': 'x',
        },
        'resposta_certa': 'x',
    },
    'Pergunta 4': {
        'Pergunta': 'x',
        'respostas': {
            'a': 'x',
            'b': 'x',
            'c': 'x',
            'd': 'x',
        },
        'resposta_certa': 'x',
    },
    'Pergunta 5': {
        'Pergunta': 'x',
        'respostas': {
            'a': 'x',
            'b': 'x',
            'c': 'x',
            'd': 'x',
        },
        'resposta_certa': 'x',
    },
    'Pergunta 6': {
        'Pergunta': 'x',
        'respostas': {
            'a': 'x',
            'b': 'x',
            'c': 'x',
            'd': 'x',
        },
        'resposta_certa': 'x',
    },
    'Pergunta 7': {
        'Pergunta': 'x',
        'respostas': {
            'a': 'x',
            'b': 'x',
            'c': 'x',
            'd': 'x',
        },
        'resposta_certa': 'x',
    },
    'Pergunta 8': {
        'Pergunta': 'x',
        'respostas': {
            'a': 'x',
            'b': 'x',
            'c': 'x',
            'd': 'x',
        },
        'resposta_certa': 'x',
    },
    'Pergunta 9': {
        'Pergunta': 'x',
        'respostas': {
            'a': 'x',
            'b': 'x',
            'c': 'x',
            'd': 'x',
        },
        'resposta_certa': 'x',
    },
    'Pergunta 10': {
        'Pergunta': 'x',
        'respostas': {
            'a': 'x',
            'b': 'x',
            'c': 'x',
            'd': 'x',
        },
        'resposta_certa': 'x',
    },
}

respostas_certas = 0

for pk, pv in gabarito.items():
    print(f'{pk}: {pv["Pergunta"]}')

    print('Escolha as opções abaixo: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('Parabéns, você acertou!')
        respostas_certas += 1
    else:
        print('Oops! Você errou... :(')
    print()

quantidade_perguntas = len(gabarito)
porcentagem_acerto = respostas_certas / quantidade_perguntas * 100
print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua satisfeita de acerto foi {porcentagem_acerto} ')
