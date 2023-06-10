from my_entsai_utils import obter_numero_positivo
from my_vetores_utils import criar_matriz, mostrar_matriz

def main():
    ordem = obter_numero_positivo('Qual a ordem da matriz?\n')

    matriz = criar_matriz(ordem, ordem, 1)
    alterar_matriz_ate_o_centro(matriz)
            
    mostrar_matriz(matriz)


def alterar_matriz_ate_o_centro(matriz):
    for i in range(1, len(matriz) - 1):
        for j in range(1, len(matriz) - 1):
            matriz[i][j] = 2

    for i in range(2, len(matriz) - 2):
        for j in range(2, len(matriz) - 2):
            matriz[i][j] = 3


main()