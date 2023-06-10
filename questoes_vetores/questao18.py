from my_entsai_utils import obter_numero_positivo, mostrar_texto
from my_vetores_utils import criar_matriz, preencher_matriz_manual, somatorio_vetor, meu_append

def main():
    ordem = obter_numero_positivo('Qual a ordem da matriz?\n')
    matriz = criar_matriz(ordem, ordem)
    preencher_matriz_manual(matriz)

    positivos = []
    negativos = []

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] >= 0:
                positivos = meu_append(positivos, matriz[i][j])
            else:
                negativos = meu_append(negativos, matriz[i][j])


    somatorio_positivos = somatorio_vetor(positivos)
    somatorio_negativos = somatorio_vetor(negativos)

    mostrar_texto(f'A soma dos elementos positivos é: {somatorio_positivos}')
    mostrar_texto(f'A soma dos elementos negativos é: {somatorio_negativos}')


if __name__ == '__main__':
    main()