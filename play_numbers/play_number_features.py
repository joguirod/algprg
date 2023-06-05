from my_entsai_utils import mostrar_texto, obter_numero_minimo, obter_numero_positivo, obter_numero, obter_texto

from play_numbers_utils import gerar_vetor_aleatorio, obter_posicoes_em_vetor, obter_numero_aleatorio, eh_positivo, eh_negativo

from my_vetores_utils import novo_vetor, meu_append, meu_reduce, ordenar_crescente, ordenar_decrescente,filtrar

from my_math_utils import eh_par, eh_impar

def gerar_numeros():
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


def preencher_vetor(vetor):
  contador = 0

  while contador < len(vetor):
    numero_atual = obter_numero(f'`{contador} > ')
    meu_append(vetor, numero_atual)
  
  return vetor


def preencher_vetor_automaticamente(vetor, valor_min, valor_max):
  
  for i in range(len(vetor)):
    numero_aleatorio = obter_numero_aleatorio(valor_min, valor_max + 1)
    vetor[i] = numero_aleatorio

  return vetor


def calcular_media_vetor(colecao):
  if len(colecao) == 0:
    return 0
  media = meu_reduce(colecao, lambda x, y: x+y, 0) / len(colecao)
  return media


def encontrar_mediana_vetor(colecao):
  if len(colecao) == 0:
    return 0
  mediana  = colecao[len(colecao) // 2]
  return mediana


def sortear_numero_vetor(colecao):
  index_aleatorio = obter_numero_aleatorio(0, len(colecao) - 1)
  sorteado = colecao[index_aleatorio]
  return sorteado


def ordenar_grupo_crescente(vetor, grupo):
  if grupo == 'T':
    todos_ordenados = ordenar_crescente(vetor)
    return todos_ordenados
  elif grupo == 'Pa':
    pares = filtrar(vetor, eh_par)
    pares_ordenados = ordenar_crescente(pares)
    return pares_ordenados
  elif grupo == 'Im':
    impares = filtrar(vetor, eh_impar)
    impares_ordenados = ordenar_crescente(impares)
    return impares_ordenados
  elif grupo == 'P':
    positivos = filtrar(vetor, eh_positivo)
    positivos_ordenados = ordenar_crescente(positivos)
    return positivos_ordenados
  elif grupo == 'N':
    negativos = filtrar(vetor, eh_negativo)
    negativos_ordenados = ordenar_crescente(negativos)
    return negativos_ordenados
  elif grupo == 'M':
    multiplo = obter_numero_minimo('Qual o múltiplo N?\n', 1)
    opcao = obter_texto('Positivos(P) ou Negativos(N)?')
    if opcao == 'P':
      positivos_multiplos = filtrar(vetor, lambda x: x >= 0 and x % multiplo == 0)
      return ordenar_crescente(positivos_multiplos)
    else:
      negativos_multiplos = filtrar(vetor, lambda x: x < 0 and x % multiplo == 0)
      return ordenar_crescente(negativos_multiplos)
    

def ordenar_grupo_decrescente(vetor, grupo):
  if grupo == 'T':
    todos_ordenados = ordenar_decrescente(vetor)
    return todos_ordenados
  elif grupo == 'Pa':
    pares = filtrar(vetor, eh_par)
    pares_ordenados = ordenar_decrescente(pares)
    return pares_ordenados
  elif grupo == 'Im':
    impares = filtrar(vetor, eh_impar)
    impares_ordenados = ordenar_decrescente(impares)
    return impares_ordenados
  elif grupo == 'P':
    positivos = filtrar(vetor, eh_positivo)
    positivos_ordenados = ordenar_decrescente(positivos)
    return positivos_ordenados
  elif grupo == 'N':
    negativos = filtrar(vetor, eh_negativo)
    negativos_ordenados = ordenar_decrescente(negativos)
    return negativos_ordenados
  elif grupo == 'M':
    multiplo = obter_numero_minimo('Qual o múltiplo N?\n', 1)
    opcao = obter_texto('Positivos(P) ou Negativos(N)?')
    if opcao == 'P':
      positivos_multiplos = filtrar(vetor, lambda x: x >= 0 and x % multiplo == 0)
      return ordenar_decrescente(positivos_multiplos)
    else:
      negativos_multiplos = filtrar(vetor, lambda x: x < 0 and x % multiplo == 0)
      return ordenar_decrescente(negativos_multiplos)