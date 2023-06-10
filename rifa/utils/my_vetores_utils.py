def novo_vetor(tamanho=0):
    lista = [''] * tamanho
    return lista


def substituir_posicao(colecao, index, substituto):
    colecao[index] = substituto
    return colecao


def meu_append(colecao, item):
    vetor_final = colecao + [item]
    return vetor_final


def meu_pop(colecao, index=-1):
    if index != -1:
        nova_colecao = colecao[:index] + colecao[index + 1:]
        elemento = colecao[index]
        return nova_colecao, elemento
    
    nova_colecao =  colecao[:index]
    elemento = colecao[index]
    return nova_colecao, elemento


def inverter_colecao(colecao):
    colecao_invertida = []

    for i in range(len(colecao)):
        colecao_invertida = meu_append(colecao_invertida, colecao[len(colecao) - 1 - i])

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
            unicos = meu_append(unicos, item)

    return unicos


def juntar_vetores(vetor1, vetor2):
    juncao_vetores = vetor1 + vetor2
    return juncao_vetores


def uniao_vetores(vetor1, vetor2):
    vetores_juntos = juntar_vetores(vetor1, vetor2)
    valores_unicos = encontrar_elementos_unicos(vetores_juntos)
    return valores_unicos

def intersecao_vetores(vetor1, vetor2):
    vetor_intersecao = []
    for item in vetor1:
        if verificar_contem(item, vetor2):
            vetor_intersecao = meu_append(vetor_intersecao, item)
    return vetor_intersecao


def construir_vetor(tamanho):
    vetor = novo_vetor(tamanho)
    contador = 0
    while contador < tamanho:
        atual = obter_numero(f'Elemento {contador} > ')
        vetor[contador] = int(atual)
        contador += 1
    print('Vetor criado e atualizado :)')
    return vetor

expoente = 2

def mapear(vetor, funcao):
    vetor_mapeado = novo_vetor(len(vetor))

    for i in range(len(vetor)):
        atual = funcao(vetor[i])
        vetor_mapeado[i] = atual
    
    return vetor_mapeado


def filtrar(vetor, funcao):
    vetor_filtrado = []

    for item in vetor:
        if funcao(item):
            vetor_filtrado = meu_append(vetor_filtrado, item)
    return vetor_filtrado


def meu_reduce(vetor, funcao_redutora, valor_inicial):
    total = valor_inicial

    for item in vetor:
        total = funcao_redutora(item, total)
    
    return total


def ordenar_crescente(lista_valores):
    if len(lista_valores) < 2:
        return lista_valores
    
    pivo = lista_valores[0]
    menores = []
    maiores = []

    for item in lista_valores[1:]:
        if item >= pivo:
            maiores = meu_append(maiores, item)
        else:
            menores = meu_append(menores, item)
    return ordenar_crescente(menores) + [pivo] + ordenar_crescente(maiores)


def ordenar_decrescente(lista_valores):
    if len(lista_valores) < 2:
        return lista_valores
    
    pivo = lista_valores[0]
    menores = []
    maiores = []

    for item in lista_valores[1:]:
        if item >= pivo:
            maiores = meu_append(maiores, item)
        else:
            menores = meu_append(menores, item)
    return ordenar_decrescente(maiores) + [pivo] + ordenar_decrescente(menores)

def obter_numero(label='Insira um número inteiro\n'): # Unica maneira que consegui fazer dar certo, com isdigit() não é legal, quando tentamos utilizar numeros negativos acontece um erro.
    while True:
        try:
            numero = int(obter_texto(label))
            return numero
        except ValueError:
            print('Valor inválido!')


def obter_texto(label='Insira o texto\n'):
    texto = input(label)
    return texto
