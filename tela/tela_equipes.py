from tela.tela_base import TelaBase


class TelaEquipes(TelaBase):
    def __init__(self):
        super().__init__()

    def mostrar_opcoes(self, opcoes: dict) -> str:
        self.limpar_tela()
        print('--- MÓDULO DE EQUIPES ---')
        print('\nOpções disponíveis:')
        for codigo, acao in opcoes.items():
            print(f'{codigo} - {acao}')
        opcao_escolhida = input('\nSelecione uma opção: ')
        return opcao_escolhida

    def listar_equipes(self, dados_equipes: list[dict]):
        self.limpar_tela()
        print('--- LISTAGEM DE EQUIPES ---\n')
        for equipe in dados_equipes:
            nome = equipe["nome"]
            codigo = equipe["codigo"]
            print(f"- EQUIPE: {nome}  CÓDIGO: {codigo}")
        print('\n')
        self.esperar_resposta()

    def incluir_equipe(self) -> dict:
        self.limpar_tela()
        print('--- CADASTRO DE EQUIPE ---\n')
        nome = input('Nome da equipe: ')
        if not (2 <= len(nome) <= 60):
            self.mostrar_mensagem('O nome da equipe deve ter entre 2 a 60 caracteres')
            return self.incluir_equipe()
        codigo = input('Código da equipe: ')
        if not codigo.isnumeric():
            self.mostrar_mensagem('O código deve ser um número inteiro')
            return self.incluir_equipe()
        codigo_curso = input('Código do curso: ')
        if not codigo.isnumeric():
            self.mostrar_mensagem('Só existem cadastros de curso com códigos númericos')
            return self.incluir_equipe()
        return {
            'nome': nome.upper(),
            'codigo': int(codigo),
            'codigo_curso': int(codigo_curso)
        }