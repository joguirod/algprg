from wordplay_features import (conteudo,
                            total_de_palavras, total_de_palavras_min_letras,
                            percentual, total_palavras_nao_contem_letras,
                            contar_palavras_com_todas_letras, total_palavras_contem_apenas_letras,
                            total_palavras_com_mais_vogais, total_palavras_palindromas,  opcoes,
                            total_palavras_abecedarias, palavra_com_maior_soma_ascii, 
                            somatorio_palavras_de_tamanho_multiplo_n, contar_palavras_mesma_letra)


from my_entsai_utils import obter_opcoes, mostrar_texto, obter_numero_positivo, obter_texto


def main():

    conteudo_arquivo = conteudo()
    palavras = conteudo_arquivo.split()

    # Processamento & Saída
    mostrar_saida(palavras)


def mostrar_saida(palavras):
    opcao = -1
    total_palavras = total_de_palavras(palavras)
    
    while opcao != 0:
        opcao = obter_opcoes(opcoes)
        if opcao == 0:
            mostrar_texto('Tchau!!')
            break
        elif opcao == 1:
            mostrar_texto(f'> O total de palavras é {total_palavras}')
        elif opcao == 2:
            minimo = obter_numero_positivo('Você deseja visualizar palavras com no mínimo quantas letras?\n')
            qtd_palavras = total_de_palavras_min_letras(palavras, minimo)
            mostrar_texto(f'> O total de palavras com no mínimo {minimo} letras é {qtd_palavras} palavras. ({percentual(qtd_palavras, total_palavras):.2f}% do total) \n')
        elif opcao == 3:
            letras = obter_texto('Quais as letras que você não quer nas palavras?\n')
            qtd_palavras = total_palavras_nao_contem_letras(palavras, letras)
            mostrar_texto(f'> O total de palavras sem as letras {letras} é {qtd_palavras} palavras. ({percentual(qtd_palavras, total_palavras):.2f}% do total) \n')
        elif opcao == 4:
            qtd_palavras = contar_palavras_com_todas_letras(palavras)
            mostrar_texto(f'> O total de palavras com todas as letras é {qtd_palavras} palavras. ({percentual(qtd_palavras, total_palavras):.2f}% do total) \n')
        elif opcao == 5:
            letras = obter_texto('Quais são as letras que você quer nas palavras?\n')
            qtd_palavras = total_palavras_contem_apenas_letras(palavras, letras)
            mostrar_texto(f'> O total de palavras com as letras desejadas é {qtd_palavras} palavras. ({percentual(qtd_palavras, total_palavras):.2f}% do total) \n')
        elif opcao == 6:
            qtd_palavras = total_palavras_com_mais_vogais(palavras)
            mostrar_texto(f'> O total de palavras com mais vogais do que consoantes é {qtd_palavras} palavras. ({percentual(qtd_palavras, total_palavras):.2f}% do total) \n')
        elif opcao == 7:
            qtd_palavras = total_palavras_palindromas(palavras)
            mostrar_texto(f'> O total de palavras palíndromas é {qtd_palavras}. ({percentual(qtd_palavras, total_palavras):.2f}% do total) \n')
        elif opcao == 8:
            qtd_palavras = total_palavras_abecedarias(palavras)
            mostrar_texto(f'> O total de palavras abecedárias é {qtd_palavras}. ({percentual(qtd_palavras, total_palavras):.2f}% do total) \n')
        elif opcao == 9:
            maior_soma = palavra_com_maior_soma_ascii(palavras)
            mostrar_texto(f'> A palavra com maior soma ASCII é "{maior_soma}" \n')
        elif opcao == 10:
            multiplo_n = obter_numero_positivo('Qual o múltiplo desejado?\n')
            somatorio = somatorio_palavras_de_tamanho_multiplo_n(palavras, multiplo_n)
            mostrar_texto(f'O somatório ASCII das palavras de tamanho múltiplo de {multiplo_n} é {somatorio} \n')
        elif opcao == 11:
            qtd_palavras = contar_palavras_mesma_letra(palavras)
            mostrar_texto(f'> {qtd_palavras} palavras começam e terminam com a mesma letra. \n')


if __name__ == '__main__':
    main()

