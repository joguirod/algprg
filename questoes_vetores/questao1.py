from my_vetores_utils import novo_vetor, inverter_colecao
from my_entsai_utils import obter_numero_positivo, obter_numero

def main():
    tamanho_vetor = obter_numero_positivo('Quantos elementos tem o vetor?\n')

    vetor_inicial = novo_vetor(tamanho_vetor)

    contador = 0
    while contador < tamanho_vetor:
        atual = obter_numero(f'Elemento {contador} > ')
        vetor_inicial[contador] = atual
        contador += 1

    vetor_invertido = inverter_colecao(vetor_inicial)

    print(f'O vetor informado invertido fica: {vetor_invertido}')


if __name__ == '__main__':
    main()