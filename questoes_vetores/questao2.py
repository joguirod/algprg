from my_entsai_utils import obter_numero_positivo
from my_vetores_utils import construir_vetor, contem_repetidos

def main():
    tamanho = obter_numero_positivo('Qual o tamanho do vetor?\n')

    vetor = construir_vetor(tamanho)

    if contem_repetidos(vetor):
        print('Há números repetidos!')
    else:
        print('Não há números repetidos :O')


if __name__ == '__main__':
    main()

