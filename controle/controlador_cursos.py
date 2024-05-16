from entidade.curso import Curso
from tela.tela_cursos import TelaCursos


class ControladorCursos:
    def __init__(self):
        self.__cursos = list()
        self.__tela_cursos = TelaCursos()
        self.__controlador_sistema = None

    @property
    def cursos(self) -> list[Curso]:
        return self.__cursos

    @property
    def tela_cursos(self) -> TelaCursos:
        return self.__tela_cursos

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @controlador_sistema.setter
    def controlador_sistema(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema

    def mostrar_opcoes(self):
        opcoes = {
            '1': 'Listar Cursos',
            '2': 'Incluir Curso',
            '3': 'Alterar Curso',
            '4': 'Excluir Curso',
            '10': 'Sair'
        }
        opcao_escolhida = str()
        while True:
            opcao_escolhida = self.tela_cursos.mostrar_opcoes(opcoes)
            match opcao_escolhida:
                case '1': self.listar_cursos()
                case '2': self.incluir_curso()
                case '3': self.alterar_curso()
                case '4': self.excluir_curso()
                case '10': break
                case _: self.tela_cursos.mostrar_mensagem('Opção Escolhida Não Existe')

    def listar_cursos(self):
        if len(self.cursos) == 0:
            return self.tela_cursos.mostrar_mensagem('Nenhum curso cadastrado')
        dados_cursos = list()
        for curso in self.cursos:
            dados_cursos.append({
                'codigo': curso.codigo,
                'nome': curso.nome
            })
        self.tela_cursos.listar_cursos(dados_cursos)

    def incluir_curso(self):
        dados = self.tela_cursos.incluir_curso()
        codigo = dados['codigo']
        nome = dados['nome']
        # Verificando duplicidade de códigos
        if self.pesquisar_curso_por_codigo(codigo) != None:
            self.tela_cursos.mostrar_mensagem('Um curso com este código já existe!')
            return self.incluir_curso()
        novo_curso = Curso(codigo, nome)
        self.cursos.append(novo_curso)
        self.tela_cursos.mostrar_mensagem('Curso cadastrado com sucesso')

    def excluir_curso(self):
        if len(self.cursos) == 0:
            return self.tela_cursos.mostrar_mensagem('Nenhum curso cadastrado')
        codigo = self.tela_cursos.excluir_curso()
        indice_curso = self.pesquisar_curso_por_codigo(codigo)
        if indice_curso == None:
            self.tela_cursos.mostrar_mensagem(
                f'Curso com código "{codigo}" não encontrado'
            )
        curso = self.cursos[indice_curso]
        confirmacao = self.tela_cursos.confirmar_acao(
            f'Deseja realmente excluir o curso {curso.nome}?'
        )
        if confirmacao:
            self.cursos.pop(indice_curso)
            self.tela_cursos.mostrar_mensagem('Curso excluído')
        else:
            self.tela_cursos.mostrar_mensagem('Exclusão cancelada')

    def alterar_curso(self):
        if len(self.cursos) == 0:
            return self.tela_cursos.mostrar_mensagem('Nenhum curso cadastrado')
        dados = self.tela_cursos.alterar_curso()
        codigo_antigo = dados['codigo_antigo']
        indice_curso = self.pesquisar_curso_por_codigo(codigo_antigo)
        if indice_curso == None:
            self.tela_cursos.mostrar_mensagem(
                f'Curso com código "{codigo_antigo}" não encontrado'
            )
        curso = self.cursos[indice_curso]
        confirmacao = self.tela_cursos.confirmar_acao(
            f'Deseja realmente alterar o curso {curso.nome}?'
        )
        if confirmacao:
            # Atualizando dados do curso que foram retornados pela interface
            novo_codigo = dados.get('novo_codigo')
            if novo_codigo != codigo_antigo and self.pesquisar_curso_por_codigo(novo_codigo) != None:
                self.tela_cursos.mostrar_mensagem('Já existe um curso com este código!')
                return self.alterar_curso()
            curso.codigo = novo_codigo
            curso.nome = dados.get('novo_nome', curso.nome)
            # Retornando uma mensagem de sucesso para o usuário
            self.tela_cursos.mostrar_mensagem('Curso alterado')
        else:
            self.tela_cursos.mostrar_mensagem('Alteração cancelada')

    def pesquisar_curso_por_codigo(self, codigo: int) -> int:
        """
        Retorna o índice do curso com o código informado.\n  
        Se nenhum curso possuir o código informado retorna `None`
        """
        for i in range(len(self.cursos)):
            curso = self.cursos[i]
            if curso.codigo == codigo:
                return i
