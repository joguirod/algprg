def mostrar_palavra_por_linha(texto):
    palavras = dividir_texto(texto, ' ')
    for i in range(len(palavras)):
        print(palavras[i])
    

def mostrar_caractere_por_linha(texto):
    for i in range(len(texto)):
        print(texto[i])


def dividir_texto(texto: str, splitador= ''):
    """Essa função divide o texto de acordo com o separador"""
    texto_dividido = []
    texto_atual = ''

    for i in range(len(texto)):
        if texto[i] == splitador:
            texto_dividido.append(texto_atual)
            texto_atual = '' # Reseta
        else:
            texto_atual = texto_atual + texto[i]

    if texto_atual != '':
        texto_dividido.append(texto_atual)

    return texto_dividido


def juntar_textos(textos: list[str], joinador= ''):
    """Essa função junta textos"""
    texto_junto = ''
    for i in range(len(textos)):
        if i + 1 < len(textos):
            texto_junto = texto_junto + textos[i] + joinador
        else:
            texto_junto = texto_junto + textos[i]
    return texto_junto

juntos = juntar_textos(['arroz', 'agua', 'feijao'], 'r') 
print(juntos)         



def juntar_texto_list_para_string(texto_dividido):
    texto_juntado = ''
    for i in range(len(texto_dividido)):
        texto_juntado = texto_juntado + texto_dividido[i]
    return texto_juntado


def contar_caractere(texto, caractere_desejado, ignore_case=False):
    if ignore_case:
        caractere_desejado = para_caixa_baixa(caractere_desejado)
        texto = para_caixa_baixa((texto))
    contador_caractere = 0
    for i in range(len(texto)):
        if caractere_desejado == texto[i]:
            contador_caractere = contador_caractere + 1
    return contador_caractere


def verificar_contem_caractere(texto, caractere_desejado, ignore_case=False):
    if ignore_case:
        caractere_desejado = para_caixa_baixa(caractere_desejado)
        texto = para_caixa_baixa((texto))

    for i in range(len(texto)):
        if caractere_desejado == texto[i]:
            return True
        

def substituir_caractere(texto, caractere, substituto, ignore_case=False):
    substituido = ''
    if ignore_case:
        texto = para_caixa_baixa(texto)
        caractere = para_caixa_baixa(texto)

    for i in range(len(texto)):
        if ignore_case and caractere == texto[i]:
            substituido += substituto
        elif not ignore_case and caractere == texto[i]:
            substituido += substituto
        else:
            substituido += texto[i]

    return substituido


def remover_caractere(texto, caractere, ignore_case=False):
    texto_final = ''
    if ignore_case:
        texto = para_caixa_baixa(texto)
        caractere = para_caixa_baixa(caractere)

    for i in range(len(texto)):
        if ignore_case and texto[i] == caractere:
            continue
        elif not ignore_case and texto[i] == caractere:
            continue
        else:
            texto_final += texto[i]
    return texto_final


def para_caixa_baixa(texto):
    texto_caixa_baixa = ''
    for i in range(len(texto)):
        caractere = texto[i]
        if eh_letra_maiuscula(caractere):
            texto_caixa_baixa = texto_caixa_baixa + chr(ord(caractere) - 32)
        else:
            texto_caixa_baixa = texto_caixa_baixa + caractere
    return texto_caixa_baixa


def para_caixa_alta(texto):
    texto_caixa_alta = ''
    for i in range(len(texto)):
        caractere = texto[i]
        if eh_letra_minuscula(caractere):
            texto_caixa_alta = texto_caixa_alta + chr(ord(caractere) - 32)
        else:
            texto_caixa_alta = texto_caixa_alta + caractere
    return texto_caixa_alta


def usa_apenas(texto, caracteres: str, ignore_case=False) -> bool:
    """imagino que verifica se o texto usa apenas certos caracteres"""
    if ignore_case:
        texto = para_caixa_baixa(texto)
        caracteres = para_caixa_baixa(caracteres)
    
    for i in range(len(texto)):
        for caracter in caracteres:
            if texto[i] != caracter:
                return False
        
    return True


def nao_usa(texto, caracteres: str, ignore_case=False) -> bool:
    """imagino que verifica se o texto nao usa certos caracteres"""
    if ignore_case:
        texto = para_caixa_baixa(texto)
        caracteres = para_caixa_baixa(caracteres)
    
    for i in range(len(texto)):
        for caracter in caracteres:
            if texto[i] != caracter:
                return True
        
    return False


def substring(texto, inicio: int, fim: int):
    substring = texto[inicio:fim]
    return substring


def substring_tam(texto, inicio: int, tamanho: int):
    substring = texto[inicio:inicio + tamanho]
    return substring


def contem_substring(texto, substring, ignore_case=False):
    if ignore_case:
        texto = para_caixa_baixa(texto)
        substring = para_caixa_baixa(substring)
    tamanho_substring = len(substring)

    for i in range(len(texto)):
        if texto[i:i + tamanho_substring] == substring:
            return True
    
    return False


def contar_substring(texto, substring, ignore_case=False):
    if ignore_case:
        texto = para_caixa_baixa(texto)
        substring = para_caixa_baixa(substring)
    tamanho_substring = len(substring)
    
    contador = 0

    for i in range(len(texto)):
        if texto[i:i + tamanho_substring] == substring:
            contador = contador + 1
    
    return contador


def substituir_substring(texto, substring, substring_substituta, ignore_case=False):
    substring_nova = ''

    if ignore_case:
        texto = para_caixa_baixa(texto)
        substring = para_caixa_baixa(substring)

    tamanho_substring = len(substring)
    
    if contem_substring(texto, substring, ignore_case=False):
        i = 0
        while i < len(texto):
            if texto[i:i + tamanho_substring] == substring:
                substring_nova = substring_nova + substring_substituta
                i = i + tamanho_substring
            else:
                substring_nova = substring_nova + texto[i]
                i = i + 1
    else:
        substring_nova = substring

    return substring_nova


def remover_substring(texto, substring, ignore_case=False):
    texto_final = ''

    if ignore_case:
        texto = para_caixa_baixa(texto)
        substring = para_caixa_baixa(substring)
    
    tamanho_substring = len(substring)
    
    i = 0
    while i < len(texto):
        if ignore_case and texto[i:i + tamanho_substring] == substring:
            i = i + tamanho_substring
            continue
        elif not ignore_case and texto[i:i + tamanho_substring] == substring:
            i = i + tamanho_substring
            continue
        else:
            texto_final += texto[i]
            i = i + 1
    return texto_final


def remover_substring_por_faixa(texto, index_inicio, index_fim):
    texto_desejado = texto[:index_inicio] + texto[index_fim+1:]
    return texto_desejado


# Outras funções que considero importantes e reutilizavéis

def eh_letra(caractere):
    return 65 <= ord(caractere) <= 90 or 97 <= ord(caractere) <= 122


def eh_letra_maiuscula(caractere):
    return 65 <= ord(caractere) <= 90


def eh_letra_minuscula(caractere):
    return 97 <= ord(caractere) <= 122


def eh_consoante(caracter):
    if 66 <= ord(caracter) <= 68 or 98 <= ord(caracter) <= 100:
        return True
    if 70 <= ord(caracter) <= 72 or 102 <= ord(caracter) <= 104:
        return True
    if 74 <= ord(caracter) <= 78 or 106 <= ord(caracter) <= 110:
        return True
    if 80 <= ord(caracter) <= 84 or 112 <= ord(caracter) <= 114:
        return True
    elif 86 <= ord(caracter) <= 90 or 118 <= ord(caracter) <= 122:
        return True
    else:
        return False
    

def duplicar_caractere(texto):
    texto_novo = ''
    for i in range(len(texto)):
        caracter = texto[i]
        texto_novo = texto_novo + caracter*2
    return texto_novo


def inverter_frase(frase):
    frase_invertida = ''
    for index in range(len(frase)):
        frase_invertida = frase_invertida + frase[len(frase) - 1 - index]
    return frase_invertida


import sys
sys.path.append('C:\\Users\\José Guilherme\\Desktop\\ADS1\\my_utils_final')