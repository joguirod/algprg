from my_entsai_utils import obter_numero

def novo_vetor(tamanho=0):
    lista = [''] * tamanho
    return lista


def substituir_posicao(colecao, index, substituto):
    colecao[index] = substituto
    return colecao


def inverter_colecao(colecao):
    colecao_invertida = []

    for i in range(len(colecao)):
        colecao_invertida.append(colecao[len(colecao) - 1 - i])

    return colecao_invertida


def verificar_contem(item, colecao):
    for elemento in colecao:
        if elemento == item:
            return True
        
    return False


def contar_frequencia(item, colecao: list):
    frequencia = 0

    for elemento in colecao:
        if elemento == item:
            frequencia += 1

    return frequencia


def contem_repetidos(colecao):
    for item in colecao:
        frequencia = contar_frequencia(item, colecao)
        if frequencia > 1:
            return True
        
    return False


def contar_elementos_unicos(colecao):
    elementos_unicos = encontrar_elementos_unicos(colecao)
    contagem = len(elementos_unicos)
    return contagem


def encontrar_elementos_unicos(colecao):
    unicos = []

    for item in colecao:
        if not verificar_contem(item, unicos):
            unicos.append(item)

    return unicos


def juntar_vetores(vetor1, vetor2):
    juncao_vetores = vetor1 + vetor2
    return juncao_vetores


def uniao_vetores(vetor1, vetor2):
    pass

def intersecao_vetores(vetor1, vetor2):
    pass


def construir_vetor(tamanho):
    vetor = novo_vetor(tamanho)
    contador = 0
    while contador < tamanho:
        atual = obter_numero(f'Elemento {contador} > ')
        vetor[contador] = atual
        contador += 1
    print('Vetor criado e atualizado :)')
    return vetor