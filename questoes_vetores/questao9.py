from my_vetores_utils import construir_vetor, ordenar_crescente
from my_entsai_utils import obter_numero_positivo, mostrar_texto

def main():
    tamanho = obter_numero_positivo('Qual o tamanho do vetor?\n')
    vetor = construir_vetor(tamanho)

    vetor_ordenado = ordenar_crescente(vetor)

    mostrar_texto(f'Vetor desordenado: {vetor}')
    mostrar_texto(f'Vetor ordenado: {vetor_ordenado}')


if __name__ == '__main__':
    main()