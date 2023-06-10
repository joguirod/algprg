from my_entsai_utils import obter_numero_minimo, mostrar_texto
from my_vetores_utils import meu_append

def main():
    tamanho_n = obter_numero_minimo('Quantos números da sequência de fibonacci você deseja ver?\n', 1)

    sequencia_fibonacci = construir_fibonacci(tamanho_n)
    
    if tamanho_n > 1:
        mostrar_texto(f'Os primeiros {tamanho_n} números de fibonacci são: {sequencia_fibonacci}')
    else:
        mostrar_texto(f'O primeiro número de fibonacci é 0')


def construir_fibonacci(tamanho):
    sequencia = [0, 1, 1]

    if tamanho <= 3:
        return sequencia[:tamanho]

    antecessor = 1
    sucessor = 1
    
    for i in range(tamanho - len(sequencia)):
        proximo = antecessor + sucessor
        sequencia = meu_append(sequencia, proximo)
        antecessor = sucessor
        sucessor = proximo

    return sequencia


if __name__ == '__main__':
    main()