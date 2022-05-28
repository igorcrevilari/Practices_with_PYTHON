# Jogar dados contra a máquina, a maior combinação ganha
# Jogo dados, 3 valores somar
# Máquina joga dados, 3 valores somar
# Comparar valores
# Resultado

import random
import time

print('BATALHA DE DADOS!\n')
time.sleep(2)
print('Você irá jogar 3 dados comuns e a soma deles deverá ser maior\n'
      'que a soma dos dados do Computador!\n'
      'AVISO: Há probabilidades do dado cair da mesa, logo quando ocorrer, você perderá um dos dados!\n')  # explicação
time.sleep(2)
print('Você está preparado?! Vamos começar!!')

while True:
    time.sleep(2)
    jogar = input(f'Digite ALGUMA TECLA para jogar os dados!\n'
                  '> ')

    x1 = random.randint(0, 6)
    x2 = random.randint(0, 6)
    x3 = random.randint(0, 6)
    soma_jogador = x1 + x2 + x3
    if x1 >= 1:
        print(f'O valor do primeiro dado foi: {x1} ')
        time.sleep(1)
    else:
        print('Ooops! O seu primeiro dado caiu da mesa... 0!')

    if x2 >= 1:
        print(f'O valor do segundo dado foi: {x2} ')
        time.sleep(1)
    else:
        print('Ooops! O seu segundo dado caiu da mesa... 0!')
    if x3 >= 1:
        print(f'O valor do terceiro dado foi: {x3} ')
        time.sleep(1)
    else:
        print('Ooops! O seu terceiro dado caiu da mesa... 0!')

    print(f'A soma de seus dados foi: {soma_jogador}!')
    time.sleep(2)

    print('...')
    print('VEZ DO COMPUTADOR!')
    print('...')

    cx1 = random.randint(0, 6)
    cx2 = random.randint(0, 6)
    cx3 = random.randint(0, 6)
    soma_computador = cx1 + cx2 + cx3

    if cx1 >= 1:
        print(f'O valor do primeiro dado foi: {cx1} ')
        time.sleep(1)
    else:
        print('Ooops! O primeiro dado caiu da mesa... 0!')

    if cx2 >= 1:
        print(f'O valor do segundo dado foi: {cx2} ')
        time.sleep(1)
    else:
        print('Ooops! O segundo dado caiu da mesa... 0!')
    if cx3 >= 1:
        print(f'O valor do terceiro dado foi: {cx3} ')
        time.sleep(1)
    else:
        print('Ooops! O terceiro dado caiu da mesa... 0!')

    print(f'A soma de seus dados foi: {soma_computador}!')
    time.sleep(1)

    print('...')
    if soma_jogador > soma_computador:
        print('Parabéns! Você ganhou essa partida!')
    else:
        print('Puuts! Você perdeu para o Computador!')
    print('...')