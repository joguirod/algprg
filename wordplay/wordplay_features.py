from my_string_utils import eh_consoante, usa_apenas, nao_usa, eh_letra_maiuscula, para_caixa_baixa

def conteudo():
    filename = 'br-sem-acentos.txt'

    with open(filename) as arquivo:
        conteudo = arquivo.read()
    
    return conteudo


opcoes = ['1 - Total de palavras',
              '2 - Palavras com no mínimo X letras',
              '3 - Palavras que não contém letras',
              '4 - Palavras que contem todas as letras',
              '5 - Palavras que só contém letras',
              '6 - Quantas palavras contém mais vogais que consoantes',
              '7 - Palavras "Palíndromas"',
              '8 - Palavras "Abecedárias"',
              '9 - Palavra(s) com maior valor ASCII',
              '10 - Somatório ASCII das Palavras de Tamanho Múltiplo de N',
              '11 - Contar/listar palavras que começam e terminam com a mesma letra',
              '0 - Sair']


# Reduce
def total_de_palavras(palavras):
    total = len(palavras)
    return total


# Filter
def total_de_palavras_min_letras(palavras, minimo):
    qtd_palavras = 0

    for palavra in palavras:
        if len(palavra) >= minimo:
            qtd_palavras = qtd_palavras + 1
    
    return qtd_palavras

# Filter
def total_palavras_nao_contem_letras(palavras, letras):
    letras_definitivas = ''

    for letra in letras:
        if eh_letra_maiuscula(letra):
            letras_definitivas = letras_definitivas + para_caixa_baixa(letra)
        else:
            letras_definitivas = letras_definitivas + letra

    qtd_palavras_sem_letras = 0

    
    for palavra in palavras:
            if nao_usa(palavra, letras_definitivas):
                qtd_palavras_sem_letras = qtd_palavras_sem_letras + 1

    return qtd_palavras_sem_letras


# Filter & Reduce
def contar_palavras_com_todas_letras(palavras):
    letras = 'abcdefghijklmnopqrstuvwxyz'
    total_palavras = 0

    for palavra in palavras:
        possui_todas_letras = True
        for letra in letras:
            letra_encontrada = False
            for caractere in palavra.lower():
                if caractere == letra:
                    letra_encontrada = True
                    break
            if not letra_encontrada:
                possui_todas_letras = False
                break

        if possui_todas_letras:
            total_palavras += 1

    return total_palavras

# Filter & Reduce
def total_palavras_contem_apenas_letras(palavras, letras):
    total_palavras = 0
    for palavra in palavras:
            if usa_apenas(palavra, letras):
                total_palavras = total_palavras + 1
    return total_palavras

# Filter
def total_palavras_com_mais_vogais(palavras):

    total_palavras = 0

    for palavra in palavras:
        qtd_consoantes = 0
        qtd_vogais = 0
        for letra in palavra:
            if eh_consoante(letra):
                qtd_consoantes = qtd_consoantes + 1
            elif not eh_consoante(letra):
                qtd_vogais = qtd_vogais + 1
        
        if qtd_vogais > qtd_consoantes:
            total_palavras += 1

    return total_palavras

# Filter
def total_palavras_palindromas(palavras):
    total_palavras = 0

    for palavra in palavras:
        palavra_invertida = palavra[::-1]
        if palavra == palavra_invertida:
           total_palavras = total_palavras + 1

    return total_palavras

# Filter
def total_palavras_abecedarias(palavras):
    total_palavras = 0
    for palavra in palavras:   
        if verifica_abecedaria(palavra):
            total_palavras = total_palavras + 1
    return total_palavras
    

def verifica_abecedaria(palavra):
    for i in range(len(palavra) - 1):
        if palavra[i] > palavra[i + 1]:
            return False
    return True

# Reduce
def palavra_com_maior_soma_ascii(palavras):
    maior = -float('inf')
    palavra_maior = ''

    for palavra in palavras:
        soma_ascii = 0
        for caracter in palavra: 
            soma_ascii = soma_ascii + ord(caracter)
        if soma_ascii >= maior:
            maior = soma_ascii
            palavra_maior = palavra

    return palavra_maior

# Reduce
def somatorio_palavras_de_tamanho_multiplo_n(palavras, multiplo_n):
    somatorio = 0
    for palavra in palavras:
        soma_ascii = 0
        for caracter in palavra:
            soma_ascii = soma_ascii + ord(caracter)
        if soma_ascii % multiplo_n == 0:
            somatorio = somatorio + soma_ascii

    return somatorio

# Filter
def contar_palavras_mesma_letra(palavras):
    total_palavras = 0

    for palavra in palavras:
        if palavra[0] == palavra[-1]:
            total_palavras += 1
    
    return total_palavras
        

def percentual(qtd_palavras, total_palavras):
    return (qtd_palavras / total_palavras) * 100
