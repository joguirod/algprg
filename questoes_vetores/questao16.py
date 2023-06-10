from my_entsai_utils import obter_numero_minimo

from my_vetores_utils import criar_matriz, mostrar_matriz

def main():
    ordem = obter_numero_minimo('Qual a ordem da matriz identidade?\n', 1)

    matriz_identidade = criar_matriz(ordem, ordem)
    substituir_diagonal_principal(matriz_identidade)

    mostrar_matriz(matriz_identidade)

def substituir_diagonal_principal(matriz_identidade):
    for i in range(len(matriz_identidade)):
        matriz_identidade[i][i] = 1

if __name__ == '__main__':
    main()
