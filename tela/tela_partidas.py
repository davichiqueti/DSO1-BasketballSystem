from tela.tela_base import TelaBase
from datetime import datetime, date


class TelaPartidas(TelaBase):
    def __init__(self):
        super().__init__()

    def mostrar_opcoes(self, opcoes: dict) -> str:
        self.limpar_tela()
        print('--- MÓDULO DE PARTIDAS ---')
        print('\nOpções disponíveis:')
        for codigo, acao in opcoes.items():
            print(f'{codigo} - {acao}')
        opcao_escolhida = input('\nSelecione uma opção: ')
        return opcao_escolhida

    def listar_partidas(self, dados_partidas: list[dict]):
        self.limpar_tela()
        print('--- LISTAGEM DE PARTIDAS ---\n')
        for partida in dados_partidas:
            codigo = partida["codigo"]
            data = partida["data"]
            print(f"- CÓDIGO: {codigo} DATA: {data}")
        print('\n')
        self.esperar_resposta()

    def incluir_partida(self) -> dict:
        self.limpar_tela()
        print('--- CADASTRO DE PARTIDA ---\n')
        # Tratamento das equipes
        codigo_equipe_1 = input('Código da Equipe 1: ').strip()
        codigo_equipe_2= input('Código da Equipe 2: ').strip()
        pontuacao_equipe_1 = input('Pontuação da Equipe 1: ').strip()
        pontuacao_equipe_2 = input('Pontuação da Equipe 2: ').strip()
        if not (
            codigo_equipe_1.isnumeric()
            and pontuacao_equipe_1.isnumeric()
            and codigo_equipe_2.isnumeric()
            and pontuacao_equipe_2.isnumeric()
        ):
            self.mostrar_mensagem('O código das Equipes e suas pontuações devem ser valores númericos')
            return self.incluir_partida()
        if (int(pontuacao_equipe_1) < 0 and int(pontuacao_equipe_2) < 0):
            self.mostrar_mensagem('A pontuação das Equipes deve ser maior do que zero')
            return self.incluir_partida()
        if not (codigo_equipe_2.isnumeric() and pontuacao_equipe_2.isnumeric()):
            self.mostrar_mensagem('O código da Equipe e a sua pontuação devem ser valores númericos')
            return self.incluir_partida()
        # Tratamento da data da partida
        data_atual = datetime.now()
        dia = input('Dia da partida: ').strip()
        mes = input('Mês da partida: ').strip()
        ano = input('Ano da partida: ').strip()
        if not (ano.isnumeric() and mes.isnumeric() and dia.isnumeric()):
            self.mostrar_mensagem('Os campos da data devem ser um números inteiros')
            return self.incluir_partida()
        else:
            data = date(ano, mes, dia)
            if data > data_atual.date():
                self.mostrar_mensagem('A data da partida não é inválida por ser posterior a data atual')
                return self.incluir_partida()        
        return {
            'data': data,
            'codigo_equipe_1': int(codigo_equipe_1),
            'pontuacao_equipe_1': int(pontuacao_equipe_1),
            'codigo_equipe_2': int(codigo_equipe_2),
            'pontuacao_equipe_2': int(pontuacao_equipe_2)
        }
