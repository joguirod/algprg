from my_entsai_utils import obter_numero, mostrar_texto

from my_vetores_utils import criar_matriz, preencher_matriz_manual, encontrar_diagonal_principal, encontrar_diagonal_secundaria, verificar_contem, meu_append, meu_reduce

def main():
    ordem = obter_numero()

    matriz = criar_matriz(ordem, ordem)
    preencher_matriz_manual(matriz)

    diagonal_principal = encontrar_diagonal_principal(matriz)
    diagonal_secundaria = encontrar_diagonal_secundaria(matriz)
    total_diagonais = diagonal_principal + diagonal_secundaria

    soma_diagonal_principal = meu_reduce(diagonal_principal, somatorio, 0)
    soma_diagonal_secundaria = meu_reduce(diagonal_secundaria, somatorio, 0)
    soma_elementos_restantes = meu_reduce(elementos_fora_diagonais(total_diagonais, matriz), somatorio, 0)
    
    mostrar_texto(f'A soma dos elementos que estão na diagonal principal é: {soma_diagonal_principal}')
    mostrar_texto(f'A soma dos elementos que estão na diagonal secundária é: {soma_diagonal_secundaria}')
    mostrar_texto(f'A soma dos elementos que não estão em uma diagonal é: {soma_elementos_restantes}')

def elementos_fora_diagonais(total_diagonais, matriz):
    elementos_restantes = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if not verificar_contem(matriz[i][j], total_diagonais):
                elementos_restantes = meu_append(elementos_restantes, matriz[i][j])

    return elementos_restantes

def somatorio(item, item2):
    return item + item2

main()