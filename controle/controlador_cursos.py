from entidade.curso import Curso
from tela.tela_cursos import TelaCursos


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

    def listar_cursos(self):
        dados_cursos = list()
        for curso in self.cursos:
            dados_cursos.append({
                'codigo': curso.codigo,
                'nome': curso.nome
            })
        self.tela_cursos.listar_cursos(dados_cursos)

    def incluir_curso(self):
        dados = self.tela_cursos.incluir_curso()
        codigo = int(dados["codigo"])
        nome = dados["nome"]
        novo_curso = Curso(codigo, nome)
        self.cursos.append(novo_curso)

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
        curso = self.cursos[indice_curso]
        if curso:
            if novo_codigo != "":
                curso.codigo = int(novo_codigo)
            if novo_nome != "":
                curso.nome = novo_nome

    def pesquisar_curso_por_codigo(self, codigo) -> int:
        """Retorna a posição do curso na lista utilizando o código"""
        codigo = int(codigo)
        for i in range(len(self.cursos)):
            curso = self.cursos[i]
            if curso.codigo == codigo:
                return i
