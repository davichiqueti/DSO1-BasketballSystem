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
            arbitro = partida['arbitro']
            print(f"Data Partida: {data.strftime('%d/%m/%Y')}   Código: {codigo}")
            print(f'Árbitro: {arbitro["nome"]} ({arbitro["cpf"]})')
            if partida["empate"]:
                print(' Resultado: EMPATE')
            else:
                print(f'Resultado: Equipe "{partida["vencedor"].nome}" Vencedora!')
            for equipe, pontuacao in partida['pontuacao'].items():
                print(f"Pontuação da Equipe {equipe.nome}: [{pontuacao['total']} Pontos]")
                for aluno, pontuacao_aluno in pontuacao['pontuacao_individual'].items():
                    print(f'\t - Jogador: {aluno.nome}({aluno.matricula}) Pontos: {pontuacao_aluno}')
            print('\n\n')
        self.esperar_resposta()

    def incluir_partida(self) -> dict:
        self.limpar_tela()
        print('--- CADASTRO DE PARTIDA ---\n')
        # Tratamento das equipes
        codigo_equipe_1 = input('Código da Equipe 1: ').strip()
        codigo_equipe_2= input('Código da Equipe 2: ').strip()
        if not (codigo_equipe_1.isnumeric() and codigo_equipe_2.isnumeric()):
            self.mostrar_mensagem('O código das Equipes devem ser valores númericos')
            return self.incluir_partida()
        # Tratamento do arbitro
        cpf_arbitro = input('CPF do árbitro (Apenas números): ').strip()
        if not (cpf_arbitro.isnumeric() and len(cpf_arbitro) == 11):
            self.mostrar_mensagem('O cpf do Árbitro deve conter os 11 dígitos do CPF sem caracteres adicionais')
            return self.incluir_partida()
        # Tratamento da data da partida
        data_atual = datetime.now()
        while True:
            data_partida = input("Data da partida (dd/mm/aaaa): ")
            try:
                data_partida = datetime.strptime(data_partida, "%d/%m/%Y")
                if data_partida > data_atual:
                    self.mostrar_mensagem('A data da partida não é válida. Posterior a data atual')
                    continue
                break
            except ValueError:
                print("A Data da partida está incorreta, por favor informe uma data no modelo dd/mm/aaaa.")
                input("Aperte ENTER para continuar.")   
        return {
            'data': data_partida,
            'cpf_arbitro': cpf_arbitro,
            'codigo_equipe_1': int(codigo_equipe_1),
            'codigo_equipe_2': int(codigo_equipe_2)
        }

    def excluir_partida(self) -> int:
        self.limpar_tela()
        print('--- EXCLUIR PARTIDA ---\n')
        codigo = input('Código da partida a ser exclúida: ')
        if not codigo.isnumeric():
            self.mostrar_mensagem('Tentativa de exclusão por código não númerico')
            return self.excluir_partida()
        return int(codigo)
