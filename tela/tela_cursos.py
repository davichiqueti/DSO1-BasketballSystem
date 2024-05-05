from tela.tela_base import TelaBase


class TelaCursos(TelaBase):
    def __init__(self):
        super().__init__()

    @property
    def controlador_cursos(self):
        return self.__controlador_cursos

    @controlador_cursos.setter
    def controlador_cursos(self, controlador_cursos):
        self.__controlador_cursos = controlador_cursos

    def mostrar_opcoes(self, opcoes: dict):
        self.limpar_tela()
        print('--- MÓDULO DE CURSOS ---')
        print('\nOpções disponíveis:')
        for codigo, acao in opcoes.items():
            print(f'{codigo} - {acao}')
        opcao_escolhida = input('\nSelecione uma opção: ')
        return opcao_escolhida

    def listar_cursos(self, dados_cursos: list[dict]):
        print('--- LISTAGEM DE CURSOS ---\n')
        for curso in dados_cursos:
            codigo = curso["codigo"]
            nome = curso["nome"]
            print(f"- NOME: {nome}  CÓDIGO: {codigo}")

    def incluir_curso(self):
        self.limpar_tela()
        print('--- CADASTRO DE CURSO ---\n')
        codigo = input('Código do curso: ')
        nome = input('Nome do curso: ')
        return {'codigo': codigo, 'nome': nome}

    def excluir_curso(self):
        print('--- EXCLUIR CURSO ---\n')
        codigo = input('Código do curso a ser exclúido: ')
        confirmacao = input('\nConfirmar exclusão? (S/N): ')
        if confirmacao in {'S', 's'}:
            print('Exclusão confirmada')
            return codigo
        else:
            print('Exclusão cancelada')
            return None

    def alterar_curso(self):
        print('--- ALTERAR CURSO ---\n')
        codigo_antigo = input('Código do curso a ser alterado: ')
        novo_codigo = input('Novo código: ')
        novo_nome = input('Novo nome: ')
        return {
            'codigo_antigo': codigo_antigo,
            'novo_codigo': novo_codigo,
            'novo_nome': novo_nome
        }
