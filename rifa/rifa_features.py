import random
from utils.my_vetores_utils import meu_append, verificar_contem
from utils.my_string_utils import verificar_contem_caractere

def nao_vender_pontos_aleatoriamente(pontos_disponiveis):
    contador = 0
    qtd_nao_vendida = random.randint(0, pontos_disponiveis // 2)

    with open('pontos_a_venda.txt', 'r', encoding='latin1') as texto:
        linhas = texto.readlines()

    index_sorteados = []

    while contador < qtd_nao_vendida:
        index_aleatorio = random.randint(0, len(linhas) - 1)
        while verificar_contem(index_aleatorio, index_sorteados):
            index_aleatorio = random.randint(0, len(linhas) - 1)
        index_sorteados = meu_append(index_sorteados, index_aleatorio)

        linha_sorteada = linhas[index_aleatorio]
        linhas[index_aleatorio] = linha_sorteada.strip() + '-\n'

        contador += 1
    
    with open('pontos_a_venda.txt', 'w', encoding='latin1') as pontos:
        pontos.writelines(linhas)


def resetar_pontos_a_venda():
    with open('pontos_a_venda.txt', 'w', encoding='latin1') as arquivo:
        arquivo.truncate()


def listar_compradores():
    compradores = []

    with open('pontos_a_venda.txt', 'r', encoding='latin1') as arquivo:
        for linha in arquivo:
            comprador = linha.strip()
            if not verificar_contem_caractere(comprador, '-'):
                compradores = meu_append(compradores, comprador)

    return compradores


def sortear_premios(qtd_premios, compradores):
    vencedores = []

    contador = 0
    numeros_sorteados = []

    while contador < qtd_premios:
        numero_sorteado = random.randint(0, len(compradores) - 1)
        while verificar_contem(numero_sorteado, numeros_sorteados):
            numero_sorteado = random.randint(0, len(compradores) - 1)
            
        for i in range(len(compradores)):
            if i == numero_sorteado:
                vencedor = f'{numero_sorteado} - {compradores[i]}'
        
        numeros_sorteados = meu_append(numeros_sorteados, numero_sorteado)
        vencedores = meu_append(vencedores, vencedor)
        contador += 1

    return vencedores