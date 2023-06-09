def contar_divisores(numero):
    divisores = 0
    atual = 1

    while atual <= numero:
        if numero % atual == 0:
            divisores = divisores + 1
        atual = atual + 1
    return divisores


def mmc(numero1, numero2):
    resto = None
    valor_1 = numero1
    valor_2 = numero2

    while resto != 0:
        resto = valor_1 % valor_2
        valor_1 = valor_2
        valor_1 = resto
    
    mdc = valor_1

    return (numero1*numero2) // mdc


def eh_par(numero):
    return numero % 2 == 0


def eh_impar(numero):
    return numero % 2 != 0


def eh_primo(numero):
    return contar_divisores == 2


def eh_numero_perfeito(numero):
    divisor = 1
    soma = 0
    while divisor < numero:
        if numero % divisor == 0:
            soma = soma + divisor
        divisor = divisor + 1

    if soma == numero:
        return True
    else:
        return False


def fatorial(numero):
    if numero == 1:
        return 1
    return numero * fatorial(numero - 1)


def raiz(numero, indice):
    raiz = numero**(1/indice)
    return raiz


def raiz_quadrada(numero):
    raiz_quadrada = raiz(numero, 2)
    return raiz_quadrada


def raiz_cubica(numero):
    raiz_cubica = raiz(numero, 3)
    return raiz_cubica


def potencia(numero, expoente):
    return numero ** expoente


def quadrado(numero):
    return numero**2


def cubo(numero):
    return numero**3


def meu_floor(numero, divisor):
    floor = numero // divisor
    return floor
