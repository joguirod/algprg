from my_vetores_utils import construir_vetor, juntar_vetores
from my_entsai_utils import obter_numero_positivo, mostrar_texto

def main():
    tamanho_vetores = obter_numero_positivo('Qual o tamanho dos vetores?\n')

    vetor_a = construir_vetor(tamanho_vetores)
    vetor_b = construir_vetor(tamanho_vetores)
    vetor_c = juntar_vetores(vetor_a, vetor_b)

    mostrar_texto(f'Juntando os dois vetores criados, formamos: {vetor_c}.')


if __name__ == '__main__':
    main()