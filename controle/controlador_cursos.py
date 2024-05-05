from entidade.curso import Curso
from tela.tela_cursos import TelaCursos
import os


class ControladorCursos:
    def __init__(self):
        self.__cursos = list()
        self.__tela_cursos = None

    @property
    def cursos(self) -> list[Curso]:
        return self.__cursos

    @property
    def tela_cursos(self) -> TelaCursos:
        return self.__tela_cursos

    @tela_cursos.setter
    def tela_cursos(self, tela_cursos: TelaCursos):
        self.__tela_cursos = tela_cursos

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
                case '1':
                    self.listar_cursos()
                case '2':
                    self.incluir_curso()
                case '3':
                    listagem_sucedida = self.listar_cursos()
                    if listagem_sucedida:
                        self.alterar_curso()
                case '4':
                    listagem_sucedida = self.listar_cursos()
                    if listagem_sucedida:
                        self.excluir_curso()
                case '10':
                    break
                case _:
                    self.tela_cursos.mostrar_mensagem('Opção Escolhida Não Existe')

    def listar_cursos(self):
        listagem_sucedida = False
        if len(self.cursos) == 0:
            self.tela_cursos.mostrar_mensagem('Nenhum Curso Cadastrado')
        else:
            dados_cursos = list()
            for curso in self.cursos:
                dados_cursos.append({
                    'codigo': curso.codigo,
                    'nome': curso.nome
                })
            self.tela_cursos.listar_cursos(dados_cursos)
            listagem_sucedida = True
        return listagem_sucedida

    def incluir_curso(self):
        try:
            dados = self.tela_cursos.incluir_curso()
            codigo = int(dados["codigo"])
            nome = dados["nome"]
            novo_curso = Curso(codigo, nome)
            self.cursos.append(novo_curso)
            self.tela_cursos.mostrar_mensagem('Curso cadastrado com sucesso')
        except:
            self.tela_cursos.mostrar_mensagem(
                'Um erro ocorreu durante o cadastro de curso'
            )

    def excluir_curso(self):
        codigo = self.tela_cursos.excluir_curso()
        if codigo:
            indice_curso = self.pesquisar_curso_por_codigo(codigo)
            self.cursos.pop(indice_curso)

    def alterar_curso(self):
        dados = self.tela_cursos.alterar_curso()
        codigo_antigo = int(dados['codigo_antigo'])
        novo_codigo = dados["novo_codigo"]
        novo_nome = dados["novo_nome"]
        indice_curso = self.pesquisar_curso_por_codigo(codigo_antigo)
        if not indice_curso:
            self.tela_cursos.mostrar_mensagem(
                f'Curso com código "{codigo_antigo}" não encontrado'
            )
        curso = self.cursos[indice_curso]
        if curso:
            if novo_codigo != "":
                curso.codigo = int(novo_codigo)
            if novo_nome != "":
                curso.nome = novo_nome

    def pesquisar_curso_por_codigo(self, codigo: int) -> int:
        """
        Retorna o índice do curso com o código informado.\n  
        Se nenhum curso possuir o código informado retorna `None`
        """
        for i in range(len(self.cursos)):
            curso = self.cursos[i]
            if curso.codigo == codigo:
                return i
