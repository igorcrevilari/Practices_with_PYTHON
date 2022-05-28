from time import sleep

id = []
print('Sistema de IDs')
sleep(2)
while True:
    escolha = input('OPÇÕES:\n'
                    '[A] Adicionar\n'
                    '[R] Remover\n'
                    '[E] Exibir\n'
                    '[X] Finalizar\n'
                    '>>>> ').upper()
    print('\n')
    sleep(2)

    if escolha == 'A':
        adicionar = input('Digite o número que será adicionado: \n'
                          '>>> ')
        if adicionar.isalnum():
            pass
        else:
            print('Apenas NÚMEROS!')

        id.append(adicionar)
        print('\n')
        print('\n')

    elif escolha == 'R':
        remover = input('Digite o número que será removido: \n'
                        '>>> ')
        if remover.isalnum():
            pass
        else:
            print('Apenas NÚMEROS!')

        id.remove(remover)
        print(id)
        print('\n')
        print('\n')

    elif escolha == 'E':
        print(id)


    elif escolha == 'X':
        print(id)
        print('Finalizando sistema...')
        break

    else:
        print('Algo deu errado! Reinicie o programa.')
        break