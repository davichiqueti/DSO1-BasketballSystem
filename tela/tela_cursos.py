import os


class TelaCursos:
    def __init__(self):
        self.__controlador_cursos = None

    @property
    def controlador_cursos(self):
        return self.__controlador_cursos

    @controlador_cursos.setter
    def controlador_cursos(self, controlador_cursos):
        self.__controlador_cursos = controlador_cursos

    def listar_cursos(self, dados_cursos: list[dict]):
        os.system('cls' if os.name=='nt' else 'clear')
        print('--- LISTAGEM DE CURSOS ---\n')
        for curso in dados_cursos:
            codigo = curso["codigo"]
            nome = curso["nome"]
            print(f"- NOME: {nome}  CÓDIGO: {codigo}")

    def incluir_curso(self):
        os.system('cls' if os.name=='nt' else 'clear')
        print('--- CADASTRO DE CURSO ---\n')
        codigo = input('Código do curso: ')
        nome = input('Nome do curso: ')
        return {'codigo': codigo, 'nome': nome}

    def excluir_curso(self):
        os.system('cls' if os.name=='nt' else 'clear')
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
        os.system('cls' if os.name=='nt' else 'clear')
        print('--- ALTERAR CURSO ---\n')
        codigo_antigo = input('Código do curso a ser alterado: ')
        novo_codigo = input('Novo código: ')
        novo_nome = input('Novo nome: ')
        return {
            'codigo_antigo': codigo_antigo,
            'novo_codigo': novo_codigo,
            'novo_nome': novo_nome
        }
