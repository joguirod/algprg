from my_entsai_utils import mostrar_texto
from my_vetores_utils import novo_vetor, meu_append, filtrar, encontrar_elementos_unicos, verificar_contem
import random

def gerar_vetor_aleatorio(tamanho):
  vetor = novo_vetor(tamanho)

  for i in range(tamanho):
    vetor[i] = int(obter_numero_aleatorio())
  
  return vetor

def obter_numero_aleatorio(limite_inferior=0, limite_superior = 100):
  return random.randint(limite_inferior, limite_superior)

def bye():
  tchaus = [
    "Tchau coração",
    "Até mais BB",
    "Fica bem nenem!",
    "Já estou com saudades!"
  ]

  index = random.randint(0,3)

  mostrar_texto(tchaus[index])


def obter_posicoes_em_vetor(vetor, valor):
  posicoes = []

  for i in range(len(vetor)):
    if vetor[i] == valor:
      posicoes = meu_append(posicoes, i)
    
  return posicoes


def filtrar_numeros_negativos(colecao):
  vetor_negativo = filtrar(colecao, lambda x: x < 0)
  return vetor_negativo


def filtrar_numeros_positivos(colecao):
  vetor_negativo = filtrar(colecao, lambda x: x >= 0)
  return vetor_negativo


def verificar_contem_vetor(vetor_original, vetor_dif):
    i = 0

    for elemento in vetor_original:
      if i == len(vetor_dif):
        break
      if elemento == vetor_dif[i]:
        i += 1

    return i == len(vetor_dif)


def verificar_maior_ou_menor(numero1, numero2):
  return numero1 >= numero2


def eh_positivo(numero):
  return numero > 0

def eh_negativo(numero):
  return not eh_positivo(numero)


def gerar_grupos_unicos(vetor, numero_n, tamanho):
  vetor = encontrar_elementos_unicos(vetor)
  grupos = []
  contador = 0

  while contador < numero_n:
    grupo = vetor[:tamanho]
    grupos = meu_append(grupos, grupo)
    vetor = vetor[tamanho:]
    contador += 1

  valores_restantes = len(vetor) % numero_n
  if valores_restantes > 0:
    for i in range(valores_restantes):
      grupos[i] = meu_append(grupos[i], (vetor[-(i + 1)]))
  
  return grupos