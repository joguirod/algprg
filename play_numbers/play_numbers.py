from my_entsai_utils import obter_numero, mostrar_texto, enter_limpar_tela

from play_number_features import gerar_vetor, localizar_posicoes, multiplicar_cada_numero_por_n

from play_numbers_utils import bye

def main():
  opcoes = menu()
  numeros = []

  opcao = obter_numero(opcoes)

  while (opcao != 0):
    if opcao == 1:
      numeros = gerar_vetor()
    elif (opcao == 2):
      mostrar_texto(f'Existem {len(numeros)} itens.')
    elif (opcao == 3):
      mostrar_texto(numeros)
    elif (opcao == 4):
      localizar_posicoes(numeros)
    elif (opcao == 5):
      mostrar_texto("Antes: ")
      mostrar_texto(numeros)
      numeros = multiplicar_cada_numero_por_n(numeros)
      mostrar_texto("Depois: ")
    mostrar_texto(numeros)
   

    # roda gigante
    enter_limpar_tela()
    opcao = obter_numero(opcoes)
  bye()


def menu():
  menu_options = "***** Play Numbers *****"
  menu_options += "\n-----------------------"
  menu_options += "\n1 - Gerar Números"
  menu_options += "\n2 - Mostrar Qtd Números gerados"
  menu_options += "\n3 - Mostrar números"
  menu_options += "\n4 - Buscar número"
  menu_options += "\n5 - Multiplicar números por N"
  menu_options += "\n0 - Sair"
  menu_options += "\n\n>> "

  return menu_options


main()
