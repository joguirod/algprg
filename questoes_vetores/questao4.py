from my_vetores_utils import encontrar_elementos_unicos, juntar_vetores, construir_vetor, verificar_contem
from my_entsai_utils import obter_numero_positivo, mostrar_texto

def main():
    tamanho_vetores = obter_numero_positivo('Qual o tamanho dos vetores?\n')

    vetor_a = construir_vetor(tamanho_vetores)
    vetor_b = construir_vetor(tamanho_vetores)

    vetor_c = uniao_vetores(vetor_a, vetor_b)
    vetor_d = intersecao_vetores(vetor_a, vetor_b)

    mostrar_texto(f'A união dos vetores é: {vetor_c}')
    mostrar_texto(f'A interseção dos vetores é: {vetor_d}')


def uniao_vetores(vetor_a, vetor_b):
    vetores_juntos = juntar_vetores(vetor_a, vetor_b)
    valores_unicos = encontrar_elementos_unicos(vetores_juntos)
    return valores_unicos


def intersecao_vetores(vetor_a, vetor_b):
    vetor_intersecao = []
    for item in vetor_a:
        if verificar_contem(item, vetor_b):
            vetor_intersecao.append(item)
    return vetor_intersecao


if __name__ == "__main__":
    main()