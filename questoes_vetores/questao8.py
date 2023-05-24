from my_vetores_utils import construir_vetor
from my_entsai_utils import mostrar_texto, obter_numero_positivo

def main():
    tamanho = obter_numero_positivo('Insira o tamanho do vetor\n')

    vetor = construir_vetor(tamanho)

    lista_num_posicao = encontrar_maior_menor(vetor)

    mostrar_texto(f'O maior número é {lista_num_posicao[0]} e sua posição é {lista_num_posicao[1]}')
    mostrar_texto(f'O maior número é {lista_num_posicao[2]} e sua posição é {lista_num_posicao[3]}')


def encontrar_maior_menor(vetor):
    maior = -float('inf')
    menor = float('inf')
    posicao_maior = 0
    posicao_menor = 0

    for i in range(len(vetor)):
        if vetor[i] >= maior:
            maior = vetor[i]
            posicao_maior = i
        else:
            menor = vetor[i]
            posicao_menor = i

    lista_num_posic = [maior, posicao_maior, menor, posicao_menor]

    return lista_num_posic


main()
