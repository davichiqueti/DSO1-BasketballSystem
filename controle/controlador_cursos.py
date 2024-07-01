from tela.tela_cursos import TelaCursos
from entidade.curso import Curso
from DAOs.curso_dao import CursoDAO
from exceptions.sem_registro_exception import SemRegistroException


class ControladorCursos:
    def __init__(self, controlador_sistema):
        self.__cursoDAO = CursoDAO()
        self.__tela_cursos = TelaCursos()
        self.__controlador_sistema = controlador_sistema
            
    def listar_cursos(self):
        dados_cursos = []
        cursos = self.__cursoDAO.get_all()
        try:
            if len(cursos) == 0:
                raise SemRegistroException()
        except SemRegistroException as e:
            return self.__tela_cursos.mostra_mensagem(e)
        
        for item in cursos:
            dados_cursos.append({"codigo": item.codigo, "nome": item.nome})
        return self.__tela_cursos.listar_cursos(dados_cursos)


    def incluir_curso(self):
        dados = self.__tela_cursos.incluir_curso()
        codigo = dados['Codigo']
        nome = dados['Nome']

        #tratamento de exceção
        # Verificando duplicidade de códigos
        if self.pesquisar_curso_por_codigo(int(codigo)) is not None:
            self.__tela_cursos.mostra_mensagem('Um curso com este código já existe!')
            return self.incluir_curso()
        # Verificando duplicidade de nomes
        for curso in self.__cursoDAO.get_all():
            if curso.nome == nome:
                self.__tela_cursos.mostra_mensagem('Um curso com este nome já existe!')
                return self.incluir_curso()
            

        # Adicionando o curso à lista de cursos
        novo_curso = Curso(codigo, nome)
        self.__cursoDAO.add(novo_curso)
        self.__tela_cursos.mostra_mensagem(f'Curso {novo_curso.nome} cadastrado com sucesso!')




    def excluir_curso(self):
        self.listar_cursos()
        if len(self.__cursoDAO.get_all()) == 0:
            return self.__tela_cursos.mostra_mensagem('Nenhum curso cadastrado')
        codigo_curso = self.__tela_cursos.selecionar_curso()
        curso_exclusao = self.pesquisar_curso_por_codigo(codigo_curso)
        if curso_exclusao is None:
            self.__tela_cursos.mostra_mensagem(
                f'Curso com código "{codigo_curso}" não encontrado'
            )
        else:
            self.__cursoDAO.remove(curso_exclusao.nome)
            self.__cursoDAO.remove(curso_exclusao.codigo)
            self.__tela_cursos.mostra_mensagem('Curso excluído')
    



    def alterar_curso(self):
        self.listar_cursos()
        codigo_curso = self.__tela_cursos.selecionar_curso()
        if len(self.__cursoDAO.get_all()) == 0:
            return self.__tela_cursos.mostra_mensagem('Nenhum curso cadastrado')
        
        nome_alteracao = self.__tela_cursos.alterar_curso()
        curso_alteracao = self.pesquisar_curso_por_codigo(codigo_curso)

        if curso_alteracao is not None:
            if nome_alteracao is None:
                self.__tela_cursos.mostra_mensagem('Já existe um curso com este código!')
                return self.alterar_curso()
        
            curso_alteracao.nome = nome_alteracao

            self.__cursoDAO.update(curso_alteracao)
            self.__tela_cursos.mostra_mensagem('Curso alterado')
            return self.listar_cursos()


    def pesquisar_curso_por_codigo(self, codigo: int) -> Curso:
        for curso in self.__cursoDAO.get_all():
            if curso.codigo == codigo:
                if isinstance(curso, Curso):
                    return curso
        return None

    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_curso,
            2: self.alterar_curso,
            3: self.excluir_curso,
            4: self.listar_cursos,
            0: self.retornar
        }

        continua = True
        while continua:
            lista_opcoes[self.__tela_cursos.mostrar_opcoes()]()
    
