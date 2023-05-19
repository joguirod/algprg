# Entrada e Saida

def mostrar_texto(conteudo):
    print(conteudo)

def mostrar_texto_inline(conteudo):
    pass

def mostrar_texto_caixa_alta(contexto):
    texto_caixa_alta = para_caixa_alta(contexto)
    print(texto_caixa_alta)


def mostrar_texto_caixa_baixa(contexto):
    texto_caixa_baixa = para_caixa_baixa(contexto)
    print(texto_caixa_baixa)


def obter_texto(label='Insira o texto\n'):
    texto = input(label)
    return texto


def obter_texto_tam_min(label, minimo):
    texto = obter_texto(label)
    while len(texto) < minimo:
        print(f'Texto menor que o minimo permitido ({minimo})!')
        texto = obter_texto(label)
    return texto


def obter_texto_tam_max(label, maximo):
    texto = obter_texto(label)
    while len(texto) > maximo:
        print(f'Texto maior que o maximo permitido ({maximo})!')
        texto = obter_texto(label)
    return texto


def obter_texto_tam_min_max(label, minimo, maximo):
    texto = obter_texto(label)
    while len(texto) > maximo or len(texto) < minimo:
        print(f'O tamanho do exto não está entre o intervalo permitido ({minimo}-{maximo})!')
        texto = obter_texto(label)
    return texto

def obter_opcoes(opcoes, label='Escolha uma das opções a seguir:'):
    print(label)
    for i in range(len(opcoes)):
       opcao = opcoes[i]
       print(f'> {opcao}')
    opcao_escolhida = input('\n')
    return opcao_escolhida


def obter_numero(label='Insira um número inteiro\n'): # Unica maneira que consegui fazer dar certo, com isdigit() não é legal, quando tentamos utilizar numeros negativos acontece um erro.
    while True:
        try:
            numero = int(obter_texto(label))
            return numero
        except ValueError:
            print('Valor inválido!')


def obter_numero_float(label='Insira um número\n'):
    while True:
        try:
            numero = float(obter_texto(label))
            return numero
        except ValueError:
            print('Valor inválido!')


def obter_numero_positivo(label='Insira um número positivo\n'):
    numero = obter_numero(label)
    while numero < 0:
        print('O número deve ser positivo!')
        numero = obter_numero(label)
    return numero


def obter_numero_negativo(label='Insira um número negativo\n'):
    numero = obter_numero(label)
    while numero > 0:
        print('O número deve ser positivo!')
    return numero


def obter_numero_minimo(label, minimo):
    numero = obter_numero(label)
    while numero < minimo:
        print(f'O número informado é menor que o minimo permitido ({minimo})!')
        numero = obter_numero(label)
    return numero


def obter_numero_maximo(label, maximo):
    numero = obter_numero(label)
    while numero > maximo:
        print(f'O número deve ser menor que o máximo permitido ({maximo})!')
        numero = obter_numero(label)
    return numero
    
def obter_numero_float_positivo(label='Insira um número positivo\n'):
    numero = obter_numero_float(label)
    while numero < 0:
        print('O número deve ser positivo!')
        numero = obter_numero_float(label)
    return numero


def obter_numero_float_negativo(label='Insira um número negativo\n'):
    numero = obter_numero_float(label)
    while numero > 0:
        print('O número deve ser positivo!')
        numero = obter_numero_float(label)
    return numero


def obter_numero_float_minimo(label, minimo):
    numero = obter_numero_float(label)
    while numero < minimo:
        print(f'O número informado é menor que o minimo permitido ({minimo})!')
        numero = obter_numero(label)
    return numero


def obter_numero_float_maximo(label, maximo):
    numero = obter_numero_float(label)
    while numero > maximo:
        print(f'O número deve ser menor que o máximo permitido ({maximo})!')
        numero = obter_numero_float(label)
    return numero


def obter_numero_faixa(label, minimo, maximo):
    numero = obter_numero(label)
    while numero < minimo or numero > maximo:
        print(f'O número deve estar entre a faixa {minimo} - {maximo}!')
        numero = obter_numero(label)
    return numero


def obter_numero_float_faixa(label, minimo, maximo):
    numero = obter_numero_float(label)
    while numero < minimo or numero > maximo:
        print(f'O número deve estar entre a faixa {minimo} - {maximo}!')
        numero = obter_numero_float(label)
    return numero


def para_caixa_alta(texto):
    texto_caixa_alta = ''
    for i in range(len(texto)):
        caractere = texto[i]
        if eh_letra_minuscula(caractere):
            texto_caixa_alta = texto_caixa_alta + chr(ord(caractere) - 32)
        else:
            texto_caixa_alta = texto_caixa_alta + caractere
    return texto_caixa_alta


def para_caixa_baixa(texto):
    texto_caixa_baixa = ''
    for i in range(len(texto)):
        caractere = texto[i]
        if eh_letra_maiuscula(caractere):
            texto_caixa_baixa = texto_caixa_baixa + chr(ord(caractere) - 32)
        else:
            texto_caixa_baixa = texto_caixa_baixa + caractere
    return texto_caixa_baixa


def eh_letra(caractere):
    return 65 <= ord(caractere) <= 90 or 97 <= ord(caractere) <= 122


def eh_letra_maiuscula(caractere):
    return 65 <= ord(caractere) <= 90


def eh_letra_minuscula(caractere):
    return 97 <= ord(caractere) <= 122
