import random
from utils.my_string_utils import verificar_contem_caractere, juntar_textos
from utils.my_vetores_utils import meu_append

def nao_vender_pontos_aleatoriamente(pontos_disponiveis):
    qtd_nao_vendida = random.randint(0, pontos_disponiveis // 2)

    with open('pontos_a_venda.txt', 'r', encoding='latin1') as texto:
        linhas = texto.readlines()

    for _ in range(qtd_nao_vendida):
        index_aleatorio = random.randint(0, len(linhas) - 1)
        linha_sorteada = linhas[index_aleatorio]
        linhas[index_aleatorio] = linha_sorteada.strip() + '-\n'
    
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
            compradores.append(comprador)

    return compradores


def sortear_premios(qtd_premios, compradores):
    vencedores = []

    contador = 0
    while contador < qtd_premios:
        numero_sorteado = random.randint(0, len(compradores) - 1)
        for i in range(len(compradores)):
            if i == numero_sorteado:
                vencedor = f'{numero_sorteado} - {compradores[i]}'
        vencedores.append(vencedor)
        contador += 1

    return vencedores