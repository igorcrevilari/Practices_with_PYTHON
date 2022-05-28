import time
print('DESCUBRA!')
time.sleep(2)
tema = input('Tema escolhido: ')
time.sleep(1)
palavra = input('Palavra escolhida: ')
time.sleep(1)
chances = int(input('Quantas chances: '))
digitadas = []
time.sleep(2)
print('___________________')
time.sleep(2)
print('COMEÇANDO!')
time.sleep(2)
print('___________________')
time.sleep(2)

while True:
    print(f'O tema escolhido foi: "{tema}"!')

    if chances <= 0:
        print('Suas chances acabaram... PERDEU!')
        break

    letra = input('Digite uma letra! ')
    if len(letra) > 1:
        print('Opss... Digite apenas uma palavra!')
        continue

    digitadas.append(letra)
    if letra in palavra:
        print(f'Parabéns! Você acertou a letra "{letra}"!')
    else:
        print(f'Errado! A letra "{letra}" não existe na palavra!')
        digitadas.pop()

    palavra_temp = ''
    for letra_temp in palavra:
        if letra_temp in digitadas:
            palavra_temp += letra_temp
        else:
            palavra_temp += '*'
    if palavra_temp == palavra:
        print(f'Que legal, VOCÊ GANHOU!!! A palavra era {palavra_temp}.')
        break
    else:
        print(f'A palavra secreta está assim: {palavra_temp}')
    
    if letra not in palavra:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')
    print()
