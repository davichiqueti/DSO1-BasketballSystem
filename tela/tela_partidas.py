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
        while True:
            data_partida = input("Nova data da partida (dd/mm/aaaa): ")
            try:
                data_partida = datetime.strptime(data_partida, "%d/%m/%Y").date()
                if data_partida > data_atual:
                    self.mostrar_mensagem('A data da partida não é válida. Posterior a data atual')
                    continue
                break
            except ValueError:
                print("Data de nascimento está incorreta, por favor informe uma data no modelo dd/mm/aaaa.")
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

    def alterar_partida(self) -> dict:
        self.limpar_tela()
        dados_retorno = dict()
        print('--- ALTERAR PARTIDA ---\n')
        # Tratamento para o código do curso a ser alterado
        codigo_antigo = input('Código da partida a ser alterada: ')
        if not codigo_antigo.isnumeric():
            self.mostrar_mensagem('Tentativa de alteração por código não númerico')
            return self.alterar_partida()
        # Tratamento para o novo nome (Se for inserido)
        novo_nome = input('Nova data: ')
        if novo_nome and not novo_nome.isspace():
            if not (5 <= len(novo_nome) <= 60):
                self.mostrar_mensagem('O novo nome do curso deve ter entre 5 a 60 caracteres')
                return self.alterar_curso()
            dados_retorno["novo_nome"] = novo_nome.upper()
        return dados_retorno
