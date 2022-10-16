n1 = float(input('N1: '))
n2 = float(input('N2: '))
res = 0

def Calcular(x, y):
    print('\n')
    op = input('Digite a operação que você deseja: \n [ + ] SOMAR\n [ - ] SUBTRAIR\n [ / ] DIVIDIR\n [ * ] MULTIPLICAR\n >>> ')
    global res
    if op == '+':
        res = x + y
    
    elif op == '-':
        res = x - y
    
    elif op == '/':
        if y == 0:
            print('Não é possível DIVIDIR POR 0')
        else:
            res = x / y
        
    elif op == '*':
        res = x * y
    
    else:
        print('Digite um operador válido!')
        pass

    print('\n')

    while True:
        print(res)
        print('\n')
        op2 = input('Digite a operação que você deseja: \n [ P ] PARAR O PROGRAMA\n [ + ] SOMAR\n [ - ] SUBTRAIR\n [ / ] DIVIDIR\n [ * ] MULTIPLICAR\n >>> ').upper()

        if op2 == 'P':
             print('Programa Finalizado!')
             return res
             print('\n')
             break

        elif op2 == '+':
            z = float(input('N2: '))
            res = res + z
            print('\n')
            continue
    
        elif op2 == '-':
            z = float(input('N2: '))
            res = res - z
            print('\n')
            continue
    
        elif op2 == '/':
            if n2 == 0:
                print('Não é possível DIVIDIR POR 0')
                continue
            else:
                z = float(input('N2: '))
                res = res / z
                print('\n')
                continue

        
        elif op2 == '*':
            z = float(input('N2: '))
            res = res * z
            print('\n')
            continue

        else:
            print('Digite uma operação válida!')
            print('\n')
            continue

Calcular(n1, n2)
print(res)


    
            
