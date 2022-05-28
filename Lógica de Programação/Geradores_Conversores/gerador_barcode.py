import random
from barcode import EAN14
from barcode.writer import ImageWriter


def Gerador():
    num = '01234567890123456789'
    total = 14

    # fazendo senha com todos
    id = "".join(random.sample(num, total))

    # criando código de barras
    codigo_barra = EAN14(id, writer=ImageWriter())
    codigo_barra.save(f"codigo_barra")

    print(id)


Gerador()




