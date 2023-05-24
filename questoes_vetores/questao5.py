from my_entsai_utils import mostrar_texto
from my_vetores_utils import construir_vetor

def main():
    vetor = construir_vetor(19)

    valor_s = calcular_soma(vetor)

    mostrar_texto(f'O resultado do cálculo é {valor_s}')


# Reduce
def calcular_soma(vetor):
    soma = 0

    for i in range(10):
        soma += (vetor[i] - vetor[-1 - i]) ** 2

    return soma


if __name__ == '__main__':
    main()