from my_vetores_utils import construir_vetor, novo_vetor
from my_entsai_utils import obter_numero_positivo, mostrar_texto

def main():
    tamanho = obter_numero_positivo('Insira o tamanho do vetor\n')

    vetor_a = construir_vetor(tamanho)
    vetor_b = construir_vetor_b(vetor_a, tamanho)


def construir_vetor_b(vetor_a, tamanho):
    vetor_b = novo_vetor(tamanho)
    for i in range(len(vetor_a)):
        if i % 2 == 0:
            vetor_b[i] = 0
        else:
            vetor_b[i] = 1
    return vetor_b


main()