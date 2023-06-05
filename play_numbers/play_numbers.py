from my_vetores_utils import novo_vetor, mapear, filtrar, meu_reduce, ordenar_crescente, construir_vetor, ordenar_decrescente

from my_entsai_utils import (obter_numero, mostrar_texto, enter_limpar_tela, obter_numero_minimo,
                            obter_numero_positivo, obter_numero_maximo, obter_texto)

from play_number_features import (preencher_vetor,preencher_vetor_automaticamente,calcular_media_vetor,
                                  encontrar_mediana_vetor,sortear_numero_vetor, ordenar_grupo_crescente,
                                  ordenar_grupo_decrescente)

from play_numbers_utils import (bye, filtrar_numeros_positivos, filtrar_numeros_negativos,
                                verificar_contem_vetor, gerar_grupos_unicos)

def main():
  opcoes = menu()
  vetor = []

  opcao = obter_numero(opcoes)

  while (opcao != 0):
    if opcao == 1:
      tamanho = obter_numero_positivo('Qual o valor de N?\n')
      vetor = novo_vetor(tamanho)
    elif (opcao == 2):
      vetor = preencher_vetor(vetor)
      mostrar_texto(f'Vetor preenchido: {vetor}')
    elif (opcao == 3):
      valor_min = obter_numero('Qual o valor mínimo desejado?\n')
      valor_max = obter_numero_minimo('Qual o valor máximo desejado?\n', valor_min + 1)
      vetor = preencher_vetor_automaticamente(vetor, valor_min, valor_max)
      mostrar_texto(f'Vetor preenchido: {vetor}')
    elif (opcao == 4):
      mostrar_texto(f'Vetor atual: {vetor}')
    elif (opcao == 5):
      expoente = obter_numero_minimo('Qual o valor do expoente N?\n', 0)
      mostrar_texto("Antes: ")
      mostrar_texto(vetor)
      vetor = mapear(vetor, lambda x: x**expoente)
      mostrar_texto("Depois: ")
      mostrar_texto(vetor)
    elif opcao == 6:
      qtd_positivos = len(filtrar(vetor, lambda x: x > 0))
      qtd_negativos = len(filtrar(vetor, lambda x: x < 0))
      qtd_zeros = len(filtrar(vetor, lambda x: x == 0))
      mostrar_texto(f'> {qtd_positivos} números positivo(s)')
      mostrar_texto(f'> {qtd_negativos} números negativo(s)')
      mostrar_texto(f'> {qtd_zeros} zero(s)')
    elif opcao == 7:
      somatorio = meu_reduce(vetor, lambda x, y: x + y, 0)
      somatorio_positivos = meu_reduce(filtrar_numeros_positivos(vetor), lambda x, y: x + y, 0)
      somatorio_negativos = meu_reduce(filtrar_numeros_negativos(vetor), lambda x, y: x + y, 0)
      print(f'- Somatório de todos: {somatorio}')
      print(f'- Somatório dos positivos: {somatorio_positivos}')
      print(f'- Somatório dos negativos: {somatorio_negativos}')
    elif opcao == 8:
      vetor_positivos = filtrar_numeros_positivos(vetor)
      vetor_negativos = filtrar_numeros_negativos(vetor)
      media = calcular_media_vetor(vetor)
      mediana = encontrar_mediana_vetor(ordenar_crescente(vetor))
      media_positivos = calcular_media_vetor(vetor_positivos)
      mediana_positivos = encontrar_mediana_vetor(vetor_positivos)
      media_negativos = calcular_media_vetor(vetor_negativos)
      mediana_negativos = encontrar_mediana_vetor(vetor_negativos)
      mostrar_texto(f'Média de todos: {media:.2f}')
      mostrar_texto(f'Mediana de todos: {mediana}')
      mostrar_texto(f'Média dos positivos: {media_positivos:.2f}')
      mostrar_texto(f'Mediana dos positivos: {mediana_positivos}')
      mostrar_texto(f'Média dos negativos: {media_negativos:.2f}')
      mostrar_texto(f'Mediana dos negativos: {mediana_negativos}')
    elif opcao == 9:
      vetor_ordenado = ordenar_crescente(vetor)
      maior = vetor_ordenado[-1]
      menor = vetor_ordenado[0]
      mostrar_texto(f'O maior número do vetor é {maior}')
      mostrar_texto(f'O menor número do vetor é {menor}')
    elif opcao == 10:
      sorteado_positivo = sortear_numero_vetor(filtrar_numeros_positivos(vetor))
      sorteado_negativo = sortear_numero_vetor(filtrar_numeros_negativos(vetor))
      mostrar_texto(f'Positivo sorteado: {sorteado_positivo}')
      mostrar_texto(f'Negativo sorteado: {sorteado_negativo}')
    elif opcao == 11:
      numero_n = obter_numero_minimo('Quantos grupos?\n', 1)
      tamanho = obter_numero_maximo('Qual o tamanho do grupo?\n', len(vetor) // numero_n + 1)
      grupos = gerar_grupos_unicos(vetor, numero_n, tamanho)
      mostrar_texto(f'Os grupos únicos gerados foram: {grupos}')
    elif opcao == 12:
      tamanho = obter_numero_maximo('Qual o tamanho do novo vetor?\n', len(vetor))
      vetor_novo = construir_vetor(tamanho)
      if verificar_contem_vetor(vetor, vetor_novo):
        mostrar_texto('O novo vetor está presente no vetor principal!')
      else:
        mostrar_texto('O novo vetor não está presente no vetor principal :(')
    elif opcao == 13:
      numero_n = obter_numero_minimo('Insira o valor de N.\n', 1)
      vetor_ordenado = ordenar_decrescente(vetor)
      top_maiores = vetor_ordenado[:numero_n]
      mostrar_texto(f'O top {numero_n} maiores é {top_maiores}')
    elif opcao == 14:
      numero_n = obter_numero_minimo('Insira o valor de N.\n', 1)
      vetor_ordenado = ordenar_crescente(vetor)
      top_menores = vetor_ordenado[:numero_n]
      mostrar_texto(f'O top {numero_n} menores é {top_menores}')
    elif opcao == 15:
      media = calcular_media_vetor(vetor)
      maiores_media = filtrar(vetor, lambda item: item >= media)
      menores_media = filtrar(vetor, lambda item: item < media)
      mostrar_texto(f'Os números maiores que a média são: {maiores_media}')
      mostrar_texto(f'Os números menores que a média são: {menores_media}')
    elif opcao == 17:
      vetor_multiplo_de_2_positivos = filtrar(vetor, lambda item: item > 0 and item % 2 == 0)
      media_multiplo_de_2_positivos = calcular_media_vetor(vetor_multiplo_de_2_positivos)
      vetor_pares_negativos = filtrar(vetor, lambda item: item < 0 and item % 2 == 0)
      vetor_reduzido_a_metade = mapear(vetor_pares_negativos, lambda x: x / 2)
      produto_negativos = meu_reduce(vetor_reduzido_a_metade, lambda x, y: x*y, 0)
      somatorio = media_multiplo_de_2_positivos + produto_negativos
      mostrar_texto(f'O somatório é igual a: {somatorio}')
    elif opcao == 18:
      grupo = obter_texto('Insira em qual grupo deseja fazer a ordenação:\n')
      grupo_ordenado = ordenar_grupo_crescente(vetor, grupo)
      mostrar_texto(f'O grupo ordenado crescentemente é: {grupo_ordenado}')
    elif opcao == 19:
      grupo = obter_texto('Insira em qual grupo deseja fazer a ordenação:\n')
      grupo_ordenado = ordenar_grupo_decrescente(vetor, grupo)
      mostrar_texto(f'O grupo ordenado decrescentemente é: {grupo_ordenado}')
    elif opcao == 20:
      numero_n = obter_numero_minimo('Insira o valor de N.\n', 1)
      numero_m = obter_numero_minimo('Insira o valor de M.\n', 1)
      mostrar_texto(f'Antes de eliminar: {vetor}')
      vetor = filtrar(vetor, lambda item: (item % numero_n != 0 or item % numero_m != 0) and item != 0)
      mostrar_texto(f'Depois de eliminar: {vetor}')

    # roda gigante
    enter_limpar_tela()
    opcao = obter_numero(opcoes)
  bye()


def menu():
  menu_options = "***************** Play Numbers *****************"
  menu_options += "\n------------------------------------------------"
  menu_options += "\n1 - Gerar vetor de tamanho N"
  menu_options += "\n2 - Preencher vetor manualmente"
  menu_options += "\n3 - Preencher vetor automaticamente"
  menu_options += "\n4 - Mostrar vetor"
  menu_options += "\n5 - Elevar números do vetor à potência N"
  menu_options += "\n6 - Contar números positivos, negativos e 0's"
  menu_options += "\n7 - Somatório (todos, negativos, positivos)"
  menu_options += "\n8 - Média e mediana (todos, negativos, positivos)"
  menu_options += "\n9 - Maior e menor número do vetor"
  menu_options += "\n10 - Sortear número positivo e negativo"
  menu_options += "\n11 - Gerar N grupos de tamanho T sem repetir valores."
  menu_options += "\n12 - Verificar se um novo vetor está 100% no vetor original (e na mesma ordem)"
  menu_options += "\n13 - Top N maiores números"
  menu_options += "\n14 - Top N menores números"
  menu_options += "\n15 - Calcular valor médio e listar números maiores e menores que a média"
  menu_options += "\n17 - Somatório da média dos números positivos múltiplos de 2 com o produto acumulado dos números negativos pares reduzidos à metade "
  menu_options += "\n18 - Ordenar os números de forma crescente:"
  menu_options += "\n\t* Todos (T) \n\t* Pares (Pa) \n\t* Impares (Im) \n\t* Positivos ou negativos (P ou N) \n\t* Multiplos (positivos ou negativos) de N (M e depois P ou N)"
  menu_options += "\n19 - Ordenar os números de forma decrescente:"
  menu_options += "\n\t* Todos (T) \n\t* Pares (Pa) \n\t* Impares (Im) \n\t* Positivos ou negativos (P ou N) \n\t* Multiplos (positivos ou negativos) de N (M e depois P ou N)"
  menu_options += "\n20 - Eliminar múltiplos de N e M"
  menu_options += "\n0 - Sair"
  menu_options += "\n\n>> "

  return menu_options

"""Somatório da Média dos Números Positivos múltiplos de dois COM o Produto acumulado dos números negativos pares reduzidos à metade
"""
main()