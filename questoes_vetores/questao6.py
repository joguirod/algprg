from my_vetores_utils import construir_vetor
from my_entsai_utils import mostrar_texto

def main():
    binario = construir_vetor(8)

    decimal = transformar_para_decimal(binario)

    hexadecimal = transformar_para_hexadecimal(decimal)

    mostrar_texto(decimal)
    mostrar_texto(hexadecimal)

def transformar_para_hexadecimal(binario):
    binario = str(binario)
    parte1 = binario[0:4]
    parte2 = binario[3:7]

    parte1_em_decimal = transformar_para_decimal(parte1)  
    parte2_em_decimal = transformar_para_decimal(parte2)


    hexadecimal = formatar_hexadecimal(parte1_em_decimal) + formatar_hexadecimal(parte2_em_decimal)

    return hexadecimal


def transformar_para_decimal(binario):
    decimal = 0
    for i in range(len(binario)):
        atual = int(binario[-1 - i])*(2**i)
        decimal += atual

    return decimal


def formatar_hexadecimal(numero):
    if numero > 10:
        return 'A'
    if numero > 11:
        return 'B'
    if numero > 12:
        return 'C'
    if numero > 13:
        return 'D'
    if numero > 14:
        return 'E'
    if numero > 15:
        return 'F'
    else:
        return str(numero)


main()