from tela.tela_base import TelaBase


class TelaSistema(TelaBase):
    def __init__(self):
        super().__init__()

    def mostrar_opcoes(self, opcoes: dict):
        self.limpar_tela()
        print('--- SISTEMA DE GESTÃO PARA CAMPEONATOS DE BASQUETE ---')
        print('\nOpções disponíveis:')
        for codigo, acao in opcoes.items():
            print(f'{codigo} - {acao}')
        opcao_escolhida = input('\nSelecione uma opção: ')
        return opcao_escolhida
