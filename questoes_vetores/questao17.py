from my_entsai_utils import obter_numero_minimo, mostrar_texto

from my_vetores_utils import criar_matriz, preencher_matriz_manual, somatorio_vetor

def main():
    ordem = obter_numero_minimo('Qual a ordem da matriz?\n', 1)

    matriz = criar_matriz(ordem, ordem)
    preencher_matriz_manual(matriz)

    maior_soma = -float('inf')
    menor_soma = float('inf')
    linha_maior_soma = None
    linha_menor_soma = None

    for i in range(len(matriz)):
        somatorio_linha = somatorio_vetor(matriz[i])
        if somatorio_linha >= maior_soma:
            maior_soma = somatorio_linha
            linha_maior_soma = i + 1
        if somatorio_linha <= menor_soma:
            menor_soma = somatorio_linha
            linha_menor_soma = i + 1

    mostrar_texto(f'A linha com a maior soma foi a linha {linha_maior_soma}.')
    mostrar_texto(f'A linha com a menor soma foi a linha {linha_menor_soma}.')

main()