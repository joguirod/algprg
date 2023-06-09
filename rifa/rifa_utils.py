import random
from utils.my_vetores_utils import meu_append
from utils.my_entsai_utils import mostrar_texto, mostrar_texto_inline
from utils.my_string_utils import verificar_contem_caractere, dividir_texto

def escrever_tentativas_vendas(pontos_disponiveis):
    with open('nomes.txt', 'r', encoding='latin1') as nomes:
        lista_nomes = nomes.read().split()

    selecionados = []

    for _ in range(min(pontos_disponiveis, len(lista_nomes))):
        index_aleatorio = random.randint(0, len(lista_nomes) - 1)
        selecionados.append(lista_nomes[index_aleatorio])

    with open('pontos_a_venda.txt', 'w', encoding='latin1') as pontos:
        for selecionado in selecionados:
            pontos.write(selecionado + '\n')


def filtrar_pontos_vendidos():
    lista_vendidos = []
    with open('pontos_a_venda.txt', 'r', encoding='latin1') as nomes:
        lista_nomes = nomes.read().split()
    for i in range(len(lista_nomes)):
        if not verificar_contem_caractere(lista_nomes[i], '-'):
            lista_vendidos = meu_append(lista_vendidos, i)

    return lista_vendidos


def filtrar_pontos_nao_vendidos():
    lista_nao_vendidos = []
    with open('pontos_a_venda.txt', 'r', encoding='latin1') as nomes:
        lista_nomes = nomes.read().split()
    for i in range(len(lista_nomes)):
        if verificar_contem_caractere(lista_nomes[i], '-'):
            lista_nao_vendidos = meu_append(lista_nao_vendidos, i)

    return lista_nao_vendidos


def calcular_valor_arrecadado(valor_ponto, pontos_vendidos):
    return valor_ponto*pontos_vendidos


def bye():
  tchaus = [
    "Tchau coração",
    "Até mais BB",
    "Fica bem nenem!",
    "Já estou com saudades!"
  ]

  index = random.randint(0,3)

  mostrar_texto(tchaus[index])
    

