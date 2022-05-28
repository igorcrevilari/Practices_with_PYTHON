from time import sleep
ingredientes = {
    'gramas/ml': {
        'ACUCAR': {1000: 7.00},
        'SAL': {1000: 7.00},
        'FARINHA-DE-TRIGO': {1000: 5.85},
        'LEITE': {1000: 6.70},
        'MACARRAO': {1000: 6.00},
        'ARROZ': {1000: 12.00},
        'FEIJAO': {1000: 12.00},
    },
    'unidade': {
        'OVO': {30: 16},
    }
}

preco_parcial = 0


# uk=ingredientes   p=quantidade    x=preco variavel  q=quantidade para multiplicar  u=preco unitario  f=valor final
def XICARA(q):
    # Cada xícara suporta 200g/ml.
    for uk in ingredientes.get('gramas/ml').values():
        for p, x in uk.items():
            u = (x / p) * 200
            f = u * q
            return f


def COLHER_SOPA(q):
    # Cada colher suporta 12g/ml.
    for uk in ingredientes.get('gramas/ml').values():
        for p, x in uk.items():
            u = (x / p) * 12
            f = u * q
            return f


def COLHER_CHA(q):
    # Cada colher suporta 4g/ml.
    for uk in ingredientes.get('gramas/ml').values():
        for p, x in uk.items():
            u = (x / p) * 4
            f = u * q
            return f

def UNIDADE(q):
    for uk in ingredientes.get('unidade').values():
        for p, x in uk.items():
            u = x / p
            f = u * q
            return f


print('Seja bem-vindo a calculadora de receitas!')
sleep(1)
print('\n')
print('Assim que for pedido a linha de receita, digite dessa forma:')
sleep(1)
print('\n')
print('EXEMPLO: 4 xicara farinha-de-trigo')
print('EXEMPLO: 8 colher_sopa acucar')
print('EXEMPLO: 5 unidade ovo')
sleep(1)
print('\n')
print('Use "_" para separar as medidas e "-" para separar ingredientes')
sleep(1)
print('\n')
print('Obrigado :)')
sleep(1)
print('\n')


while True:

    linha = input('Digite a linha da receita \n'
                  '>>> ').upper()

    linha = linha.split(' ')  # separa o input em 3 dados
    q = int(linha[0])  # número multiplicado na funcao
    calculo = str(linha[1])  # qual funçao é (xicara, colher_sopa, colher_cha...)
    ingrediente = str(linha[2])  # qual é o ingrediente

    # checagem ingredientes na lista e atribuir funcoes
    if q <= 0:
        print('Isso é uma medida inexistente! Por favor, indique uma quantidade.')

    if calculo == 'xicara' or 'colher_cha' or 'colher_sopa':  # confere as DEFS de CALCULO
        if ingrediente in ingredientes.get('gramas/ml').keys():  # confere ingrediente gramas/ml dentro do banco de dados
            if calculo == 'colher_cha'.upper():
                print(f'{q} {calculo} de {ingrediente} vale {COLHER_CHA(q):.2f}')
                preco_parcial = preco_parcial + (COLHER_CHA(q))

            elif calculo == 'colher_sopa'.upper():
                print(f'{q} {calculo} de {ingrediente} vale {COLHER_SOPA(q):.2f}')
                preco_parcial = preco_parcial + COLHER_SOPA(q)

            elif calculo == 'xicara'.upper():
                print(f'{q} {calculo} de {ingrediente} vale {XICARA(q):.2f}')
                preco_parcial = preco_parcial + XICARA(q)

            else:
                print('Isso é uma medida inexistente!.')
                break

        elif ingrediente in ingredientes.get('unidade').keys():  # confere ingrediente unitário dentro do banco de dados

            if calculo == 'unidade'.upper():
                print(f'{q} {calculo} de {ingrediente} vale {UNIDADE(q):.2f}')
                preco_parcial = preco_parcial + UNIDADE(q)
            else:
                pass

    else:
        print('Algo deu errado! Reinicie o programa...')

    print(f'O valor atual é de: R${preco_parcial:.2f}')

    print('\n')