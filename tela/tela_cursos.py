from tela.tela_base import TelaBase


class TelaCursos(TelaBase):
    def __init__(self):
        super().__init__()

    def mostrar_opcoes(self, opcoes: dict) -> str:
        self.limpar_tela()
        print('--- MÓDULO DE CURSOS ---')
        print('\nOpções disponíveis:')
        for codigo, acao in opcoes.items():
            print(f'{codigo} - {acao}')
        opcao_escolhida = input('\nSelecione uma opção: ')
        return opcao_escolhida

    def listar_cursos(self, dados_cursos: list[dict]):
        self.limpar_tela()
        print('--- LISTAGEM DE CURSOS ---\n')
        for curso in dados_cursos:
            codigo = curso["codigo"]
            nome = curso["nome"]
            print(f"- NOME: {nome}  CÓDIGO: {codigo}")
        print('\n')
        self.esperar_resposta()

    def incluir_curso(self) -> dict:
        self.limpar_tela()
        print('--- CADASTRO DE CURSO ---\n')
        codigo = input('Código do curso: ')
        if not codigo.isnumeric():
            self.mostrar_mensagem('O código deve ser um número inteiro')
            return self.incluir_curso()
        nome = input('Nome do curso: ')
        if not (5 <= len(nome) <= 60):
            self.mostrar_mensagem('O nome do curso deve ter entre 5 a 60 caracteres')
            return self.incluir_curso()
        return {
            'codigo': int(codigo),
            'nome': nome.upper().strip()
        }

    def excluir_curso(self) -> int:
        self.limpar_tela()
        print('--- EXCLUIR CURSO ---\n')
        codigo = input('Código do curso a ser exclúido: ')
        if not codigo.isnumeric():
            self.mostrar_mensagem('Tentativa de exclusão por código não númerico')
            return self.excluir_curso()
        return int(codigo)

    def alterar_curso(self) -> dict:
        self.limpar_tela()
        dados_retorno = dict()
        print('--- ALTERAR CURSO ---\n')
        # Tratamento para o código do curso a ser alterado
        codigo_antigo = input('Código do curso a ser alterado: ')
        if not codigo_antigo.isnumeric():
            self.mostrar_mensagem('Tentativa de alteração por código não númerico')
            return self.alterar_curso()
        dados_retorno["codigo_antigo"] = int(codigo_antigo)
        # Tratamento para o novo código (Se for inserido)
        novo_codigo = input('Novo código: ')
        if novo_codigo and not novo_codigo.isspace():
            if not novo_codigo.isnumeric():
                self.mostrar_mensagem('O novo código deve ser um inteiro')
                return self.alterar_curso()
            dados_retorno["novo_codigo"] = int(novo_codigo)
        # Tratamento para o novo nome (Se for inserido)
        novo_nome = input('Novo nome: ')
        if novo_nome and not novo_nome.isspace():
            if not (5 <= len(novo_nome) <= 60):
                self.mostrar_mensagem('O novo nome do curso deve ter entre 5 a 60 caracteres')
                return self.alterar_curso()
            dados_retorno["novo_nome"] = novo_nome.upper()
        return dados_retorno
