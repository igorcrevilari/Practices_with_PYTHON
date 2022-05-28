import time

# Conversor de medidas

print('Explicação')
print('/ Celcius / Kelvin / Fahrenheit /')
time.sleep(2)

Tc = 'Celcius'
Tk = 'Kelvin'
Tf = 'Fahrenheit'

print('Você deseja converter:\n ')
time.sleep(2)

print('Celcius para Kelvin:  [C/K] \n'
      'Celcius para Fahrenheit: [C/F] \n')
time.sleep(1)

print('Kelvin para Fahrenheit: [K/F] \n'
      'Kelvin para Celcius: [K/C] \n')
time.sleep(1)

print('Fahrenheit para Kelvin: [F/K] \n'
      'Fahrenheit para Celcius: [F/C] \n')

time.sleep(1)

while True:
    converter = input('Digite aqui >> ')
    time.sleep(3)
    convertido = int(input('Temperatura a ser convertida >> '))

    if converter == 'C/K':
        resultado = convertido + 273
        print(f'O resultado é {resultado} Kelvins.')
    elif converter == 'C/F':
        resultado = convertido * 1.8 + 32
        print(f'O resultado é {resultado} Fahrenheit.')
    elif converter == 'K/F':
        resultado = (convertido - 273) * 1.8 + 32
        print(f'O resultado é {resultado} Fahrenheit.')
    elif converter == 'K/C':
        resultado = convertido - 273
        print(f'O resultado é {resultado} Celcius.')
    elif converter == 'F/K':
        resultado = (convertido - 32) * 5 / 9 + 273
        print(f'O resultado é {resultado} Kelvins.')
    elif converter == 'F/C':
        resultado = (convertido - 32) / 1.8
        print(f'O resultado é {resultado} Celcius.')

    else:
        print('Não foi possível conferir os resultados.')
