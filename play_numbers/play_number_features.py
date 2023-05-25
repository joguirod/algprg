from my_entsai_utils import mostrar_texto, obter_numero_minimo, obter_numero_positivo

from play_numbers_utils import gerar_vetor_aleatorio, obter_posicoes_em_vetor

from my_vetores_utils import novo_vetor

def gerar_vetor():
  tamanho = obter_numero_positivo("Quantos elementos? ")
  numeros = gerar_vetor_aleatorio(tamanho)

  return numeros

def localizar_posicoes(numeros):
  numero = obter_numero_minimo("Número: ", 0)
  posicoes = obter_posicoes_em_vetor(numeros, numero)

  if len(posicoes) > 0:
    mostrar_texto(f'Numero {numero} localizado nas posições: {posicoes}')
  else:
    mostrar_texto("Sinto muito! Número não encontrado!")
  

def multiplicar_cada_numero_por_n(numeros):
  vetor = novo_vetor(len(numeros))
  n = obter_numero_positivo("Multiplicador: ")

  for i in range(len(numeros)):
    vetor[i] = numeros[i] * n
  
  return vetor

