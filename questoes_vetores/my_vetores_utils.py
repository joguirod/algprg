from my_entsai_utils import obter_numero, mostrar_texto_inline, mostrar_texto

def novo_vetor(tamanho=0, valor_padrao=0):
    lista = [valor_padrao] * tamanho
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
    print('Vetor criado e/ou atualizado :)')
    return vetor


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


def somatorio_vetor(vetor):
    return meu_reduce(vetor, lambda x, y: x + y, 0)
    

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


def criar_matriz(qtd_linhas, qtd_colunas, valor_padrao=0):
    matriz = novo_vetor(qtd_linhas)
    for i in range(len(matriz)):
        matriz[i] = novo_vetor(qtd_colunas, valor_padrao)

    return matriz


def preencher_matriz_manual(matriz):
    qtd_linhas = len(matriz)
    for i in range(qtd_linhas):
        for j in range(len(matriz[i])):
            matriz[i][j] = obter_numero(f'[{i}][{j}] > ')



def somar_matrizes(matriz1, matriz2):
    if len(matriz1) == len(matriz2) and len(matriz1[0]) == len(matriz2[0]):
        qtd_linhas = len(matriz1)
        qtd_colunas = len(matriz1[0])

        matriz_soma = criar_matriz(qtd_linhas, qtd_colunas)

        for i in range(qtd_linhas):
            for j in range(qtd_colunas):
                matriz_soma[i][j] = matriz1[i][j] + matriz2[i][j]

        return matriz_soma


def transformar_matriz_para_transposta(matriz):
    qtd_linhas = len(matriz)
    qtd_colunas = len(matriz[0])
    matriz_transposta = criar_matriz(qtd_colunas, qtd_linhas)

    for i in range(qtd_linhas):
        for j in range(qtd_colunas):
            # Nas matrizes transpostas, o numero da coluna passa a ser o numero da linha e vice-versa
            matriz_transposta[j][i] = matriz[i][j]

    return matriz_transposta


def encontrar_diagonal_principal(matriz):
    diagonal_principal = []

    for i in range(len(matriz)):
        diagonal_principal = meu_append(diagonal_principal, matriz[i][i])

    return diagonal_principal


def encontrar_diagonal_secundaria(matriz):
    diagonal_secundaria = []
    
    for i in range(len(matriz)):
        diagonal_secundaria = meu_append(diagonal_secundaria, matriz[len(matriz) - 1 - i][i])

    return diagonal_secundaria


def mostrar_vetor(vetor, barra_ou_colchete='|'):
    mostrar_texto_inline(barra_ou_colchete)
    for item in vetor:
        mostrar_texto_inline(f' {item}')
    mostrar_texto(f' {barra_ou_colchete}')


def mostrar_matriz(matriz):
    for linha in matriz:
        mostrar_vetor(linha)