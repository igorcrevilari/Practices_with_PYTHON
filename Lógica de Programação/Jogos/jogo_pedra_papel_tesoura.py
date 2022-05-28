import random
import time

lista = ['Pedra', 'Papel', 'Tesoura']
lista[0] = 1
lista[1] = 2
lista[2] = 3

print('...')
print('PEDRA, PAPEL, TESOURA!')
print('...')
time.sleep(2)


joga_pc = (random.choice(lista))

while True:
    time.sleep(2)
    joga_eu = input('Selecione:\n'
                    '[1] PEDRA\n'
                    '[2] PAPEL\n'
                    '[3] TESOURA\n'
                    '> ')  # Escolha jogador
    if len(joga_eu) > 1:
        print('Opss! Isso não vale... Repita o comando!')
        continue
    else:
        joga_eu = int(joga_eu)

    if joga_eu == 1:
        if joga_pc == 1:
            print('O Computador escolheu PEDRA!')
            time.sleep(2)
            print('Você EMPATOU!')

        elif joga_pc == 2:
            print('O Computador escolheu PAPEL!')
            time.sleep(2)
            print('Você PERDEU!')

        elif joga_pc == 3:
            print('O Computador escolheu TESOURA!')
            time.sleep(2)
            print('Você GANHOU!')

        else:
            print('Operação INVÁLIDA!')
            break

    if joga_eu == 2:  # PEDRA PAPEL TESOURA
        if joga_pc == 1:
            print('O Computador escolheu PEDRA!')
            time.sleep(2)
            print('Você GANHOU!')

        elif joga_pc == 2:
            print('O Computador escolheu PAPEL!')
            time.sleep(2)
            print('Você EMPATOU!')

        elif joga_pc == 3:
            print('O Computador escolheu TESOURA!')
            time.sleep(2)
            print('Você PERDEU!')

        else:
            print('Operação INVÁLIDA!')
            break

    if joga_eu == 3:  # PEDRA PAPEL TESOURA
        if joga_pc == 1:
            print('O Computador escolheu PAPEL!')
            time.sleep(2)
            print('Você PERDEU!')

        elif joga_pc == 2:
            print('O Computador escolheu PEDRA!')
            time.sleep(2)
            print('Você GANHOU!')

        elif joga_pc == 3:
            print('O Computador escolheu TESOURA!')
            time.sleep(2)
            print('Você EMPATOU!')

        else:
            print('Operação INVÁLIDA!')
            break
