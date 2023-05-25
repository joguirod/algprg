from my_entsai_utils import mostrar_texto
from my_vetores_utils import novo_vetor
import random

def gerar_vetor_aleatorio(tamanho):
  vetor = novo_vetor(tamanho)

  for i in range(tamanho):
    vetor[i] = obter_numero_aleatorio()
  
  return vetor

def obter_numero_aleatorio(limite = 100):
  return random.randint(0, limite)

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
      posicoes.append(i)
    
  return posicoes

