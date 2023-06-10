from rifa_utils import escrever_tentativas_vendas, bye, filtrar_pontos_vendidos, filtrar_pontos_nao_vendidos, calcular_valor_arrecadado
from rifa_features import nao_vender_pontos_aleatoriamente, resetar_pontos_a_venda, listar_compradores, sortear_premios
from utils.my_entsai_utils import mostrar_texto, obter_numero_faixa, obter_numero_positivo, obter_numero_float_positivo, enter_limpar_tela

def main():
    opcoes = menu()
    opcao = obter_numero_faixa(opcoes, 0, 8)
    pontos_disponiveis = 0
    pontos_vendidos = 0
    compradores = None
    valor_ponto = 0
    taxa_administracao = 0
    qtd_premios = 0

    while opcao != 0:
        if opcao == 1:
            pontos_disponiveis = obter_numero_positivo('Pontos disponíveis: ')
            escrever_tentativas_vendas(pontos_disponiveis)
            nao_vender_pontos_aleatoriamente(pontos_disponiveis)
            compradores = listar_compradores()
        elif opcao == 2:
            lista_pontos_vendidos = filtrar_pontos_vendidos()
            lista_pontos_nao_vendidos = filtrar_pontos_nao_vendidos()
            pontos_nao_vendidos = len(lista_pontos_nao_vendidos)
            pontos_vendidos = len(lista_pontos_vendidos)
            mostrar_texto(f'N° pontos vendidos: {pontos_vendidos}')
            mostrar_texto(f'N° pontos não vendidos: {pontos_nao_vendidos}')
            mostrar_texto(f"Lista de pontos vendidos: {lista_pontos_vendidos}")
            mostrar_texto(f"Lista de pontos não vendidos: {lista_pontos_nao_vendidos}")
        elif opcao == 3:
            valor_ponto =  obter_numero_float_positivo("Valor do ponto > R$ ")
            mostrar_texto('Valor atualizado!')
        elif opcao == 4:
            taxa_administracao = obter_numero_float_positivo("% Da taxa de administração > ")
            mostrar_texto('Valor atualizado!')
        elif opcao == 5:
            valor_arrecadado = calcular_valor_arrecadado(valor_ponto, pontos_vendidos)
            total_administracao = valor_arrecadado * (taxa_administracao/100)
            mostrar_texto(f'O total arrecadado foi: {valor_arrecadado:.2f}')
            mostrar_texto(f'O total da taxa de administração foi: {total_administracao:.2f}')
        elif opcao == 6:
            qtd_premios = obter_numero_positivo("Qtd prêmios > ")
            mostrar_texto('Quantidade atualizada!')
        elif opcao == 7:
            sorteados = sortear_premios(qtd_premios, compradores)
            mostrar_texto('Os vencedores foram:')
            for sorteado in sorteados:
                mostrar_texto(sorteado)
        elif opcao == 8:
            resetar_pontos_a_venda()
            pontos_disponiveis = 0
            valor_ponto = 0
            taxa_administracao = 0
            qtd_premios = 0

        enter_limpar_tela()
        opcao = obter_numero_faixa(opcoes, 0, 8)

    resetar_pontos_a_venda()
    bye()


def menu():
    opcoes = "0 - Sair do programa"
    opcoes += "\n1 - Informar a quantidade de pontos disponíveis para venda"
    opcoes += "\n2 - Ver quantidade de pontos vendidos e não vendidos e lista pontos vendidos e não vendidos"
    opcoes += "\n3 - Informar o valor do ponto"
    opcoes += "\n4 - Informar o valor da taxa de administração"
    opcoes += "\n5 - Mostrar valor arrecado (valor líquido e total da taxa de administração)"
    opcoes += "\n6 - Informar quantos prêmios serão rifados"
    opcoes += "\n7 - Realizar sorteio"
    opcoes += "\n8 - Resetar"
    opcoes += "\n> "
    
    return opcoes


if __name__ == '__main__':
    main()