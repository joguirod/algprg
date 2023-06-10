from my_entsai_utils import obter_numero, mostrar_texto

from my_vetores_utils import criar_matriz, preencher_matriz_manual, encontrar_diagonal_principal

def main():
    ordem = obter_numero()

    matriz = criar_matriz(ordem, ordem)
    preencher_matriz_manual(matriz)

    if verificar_simetria(matriz):
        mostrar_texto('A matriz é simétrica!')
    else:
        mostrar_texto('A matriz não é simétrica :(')


def verificar_simetria(matriz):

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == matriz[j][i]:
                return True
    
    return False


main()