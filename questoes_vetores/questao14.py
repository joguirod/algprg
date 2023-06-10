from my_vetores_utils import meu_append, criar_matriz, preencher_matriz_manual
from my_entsai_utils import obter_numero_positivo, mostrar_texto

def main():
    ordem = obter_numero_positivo('Qual a ordem da matriz?\n')
    matriz = criar_matriz(ordem, ordem)
    preencher_matriz_manual(matriz)

    maior_numero = -float('inf')
    menor_numero = float('inf')
    posicao_maior = None
    posicao_menor = None

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] >= maior_numero:
                maior_numero = matriz[i][j]
                posicao_maior = [i, j]
            if matriz[i][j] <= menor_numero:
                menor_numero = matriz[i][j]
                posicao_menor = [i, j]

    mostrar_texto(f'Maior número: {maior_numero} \n > Linha: {posicao_maior[0]} \n > Coluna: {posicao_maior[1]}')
    mostrar_texto(f'Menor número: {menor_numero} \n > Linha: {posicao_menor[0]} \n > Coluna: {posicao_menor[1]}')
    

if __name__ == "__main__":
    main()