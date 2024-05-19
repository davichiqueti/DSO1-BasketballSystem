from tela.tela_base import TelaBase


class TelaCampeonatos(TelaBase):
    def __init__(self):
        super(). __init__()

    def tela_opcoes(self):
        self.limpar_tela()
        print("--------Campeonatos--------")
        print("Escolha uma opção:")
        print("1 - Incluir campeonatos")
        print("2 - Incluir partidas em um campeonato")
        print("3 - Alterar campeonatos")
        print("4 - Excluir campeonatos")
        print("5 - Listar campeonatos")
        print("6 - Exibir relatórios de campeonatos")
        print("10 - Retornar")

        opcao = int(input("Escolha uma opcao: "))
        return opcao
        
    

