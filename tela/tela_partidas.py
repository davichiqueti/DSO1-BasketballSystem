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
            print(f"Árbitro: {arbitro['nome']} ({arbitro['cpf']})")
            print(f"PONTUAÇÕES:")
            for equipe, pontuacao in partida['pontuacao_equipes'].items():
                print(f"\n- EQUIPE {equipe}")
                total = 0
                for pontuacao_aluno in pontuacao:
                    print(f'\t- {pontuacao_aluno['nome']} ({pontuacao_aluno['matricula']}): {pontuacao_aluno['pontos']}')
                    total += pontuacao_aluno['pontos']
                print(f"- TOTAL EQUIPE {equipe}: {total}")
        print('\n')
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
            self.mostrar_mensagem('O código do Árbitro deve ser númerico com 11 dígitos sem caracteres separadores')
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
            data = datetime(year=int(ano), month=int(mes), day=int(dia))
            if data > data_atual:
                self.mostrar_mensagem('A data da partida não é inválida por ser posterior a data atual')
                return self.incluir_partida()        
        return {
            'data': data,
            'cpf_arbitro': cpf_arbitro,
            'codigo_equipe_1': int(codigo_equipe_1),
            'codigo_equipe_2': int(codigo_equipe_2)
        }

    def alterar_pontuacao_equipe(self, nome_equipe, dados_alunos: list[dict]) -> dict:
        print(f'\nPontuação Equipe "{nome_equipe}"')
        for aluno in dados_alunos:
            pontos_aluno = input(f'- Pontos de {aluno['nome']} ({aluno['matricula']}): ')
            if not pontos_aluno.isnumeric() or int(pontos_aluno) < 0:
                self.mostrar_mensagem('A pontuação dos alunos deve ser um número inteiro igual ou maior do que 0')
                return self.incluir_partida()
            else:
                aluno['pontos'] = int(pontos_aluno)
        return dados_alunos
