from my_entsai_utils import obter_numero_minimo, mostrar_texto
from my_vetores_utils import preencher_matriz_manual, transformar_matriz_para_transposta, criar_matriz

def main():
    ordem_matriz = obter_numero_minimo('Qual a ordem da matriz?\n', 1)

    matriz = criar_matriz(ordem_matriz, ordem_matriz)
    preencher_matriz_manual(matriz)
    matriz_transposta = transformar_matriz_para_transposta(matriz)

    mostrar_texto(f'Inicialmente sua matriz era: {matriz}')
    mostrar_texto(f'Inicialmente sua matriz transposta sera: {matriz_transposta}')


main()
