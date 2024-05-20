from entidade.aluno import Aluno
from datetime import date
from tela.tela_alunos import TelaAlunos
import time


class ControladorAlunos:
    def __init__(self):
        self.__alunos = []
        self.__tela_alunos = TelaAlunos()
        self.__controlador_sistema = None


    @property
    def alunos(self):
        return self.__alunos


    @alunos.setter
    def alunos(self, alunos: list):
        self.__alunos = alunos


    @property
    def tela_alunos(self):
        return self.__tela_alunos
  

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema


    @controlador_sistema.setter
    def controlador_sistema(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema


    def mostrar_opcoes(self):
        retorno = 0
        while True:
            retorno = self.tela_alunos.tela_opcoes()
            if retorno == 1:
                self.incluir_aluno()
            elif retorno == 2:
                self.alterar_aluno()
            elif retorno == 3:
                self.excluir_aluno()
            elif retorno == 4:
                self.listar_aluno()
            elif retorno == 10:
                break
            else:
                self.tela_alunos.mostrar_mensagem('Opção inválida.')


    def incluir_aluno(self):
        info_aluno = self.__tela_alunos.incluir_aluno()
        indice_curso = self.__controlador_sistema.controlador_cursos.pesquisar_curso_por_codigo(info_aluno["codigo do curso"])
        if indice_curso != None:
            curso_aluno = self.controlador_sistema.controlador_cursos.cursos[indice_curso]
        else:
            if len(self.controlador_sistema.controlador_cursos.cursos) == 0:
                self.tela_alunos.mostrar_mensagem("O código informado não corresponde a nenhum curso, cadastre um curso primeiro.")
                return self.controlador_sistema.mostrar_opcoes()
            
                

        if curso_aluno in self.controlador_sistema.controlador_cursos.cursos:
            novo_aluno = Aluno(
                                info_aluno['Nome'], 
                                info_aluno['CPF'],
                                info_aluno["Data de nascimento"], 
                                info_aluno['Estado'], 
                                info_aluno['Cidade'], 
                                info_aluno['Bairro'],
                                info_aluno['Matricula'],
                                curso_aluno
                               )
            for aluno in self.__alunos:
                if aluno.cpf == novo_aluno.cpf or aluno.matricula == novo_aluno.matricula:
                    return self.tela_alunos.mostrar_mensagem("Já existe um aluno cadastrado com esses dados.")
                     
            self.__alunos.append(novo_aluno)
            return self.__tela_alunos.mostrar_mensagem("O aluno foi cadastrado com sucesso!")
        else:
            return self.tela_alunos.mostrar_mensagem("Não é possível cadastrar esse aluno pois o código informado não corresponde a um curso valido")


    def alterar_aluno(self):
        if len(self.__alunos) == 0:
            return self.tela_alunos.mostrar_mensagem("Nenhum aluno está cadastrado.")
        #recebe o dicionario de alteracao 
        dados_aluno_alteracao =  dict()
        dados_aluno_alteracao = self.__tela_alunos.alterar_aluno()
        cpf_aluno_antigo = dados_aluno_alteracao["CPF alteracao"]

        #encontra o indice do curso na lista de objetos
        codigo_curso = dados_aluno_alteracao["codigo_curso"]
        indice_curso = self.controlador_sistema.controlador_cursos.pesquisar_curso_por_codigo(codigo_curso)
        
        #verificacao codigo do curso
        if indice_curso is None:
            return self.tela_alunos.mostrar_mensagem("O código informado não corresponde a nenhum curso cadastrado.")
            
        
        #define o curso com base no indice encontrado
        curso_aluno = self.controlador_sistema.controlador_cursos.cursos[indice_curso]

        #se o CPF antigo informado for encontrado na lista de objetos de alunos, o mesmo pode ser alterado 
        novo_aluno = None
        for aluno in self.__alunos:
            if cpf_aluno_antigo == aluno.cpf:
                novo_aluno = aluno
                break
        if novo_aluno is None:
            return self.tela_alunos.mostrar_mensagem("O CPF informado não corresponde a nenhum aluno previamente cadastrado.")
                    
        #alteracao            
        aluno.nome = dados_aluno_alteracao["Nome"]
        aluno.cpf =  dados_aluno_alteracao["CPF"]
        aluno.data_nascimento =  dados_aluno_alteracao["Data de nascimento"]
        aluno.estado =  dados_aluno_alteracao["Estado"]
        aluno.cidade =  dados_aluno_alteracao["Cidade"]
        aluno.bairro = dados_aluno_alteracao["Bairro"] 
        aluno.matricula = dados_aluno_alteracao["Matricula"] 
        aluno.curso = curso_aluno
        self.tela_alunos.limpar_tela()
        return self.tela_alunos.mostrar_mensagem(f"O cadastro do aluno{aluno.nome}, matricula {aluno.matricula} do curso {aluno.curso.nome}, foi alterado com sucesso!")


    def excluir_aluno(self):
        if len(self.__alunos) != 0:
            matricula_aluno = self.__tela_alunos.excluir_aluno()
            for aluno in self.__alunos:
                if aluno.matricula == matricula_aluno:
                    resposta = self.__tela_alunos.confirmar_acao(f"Deseja excluir o cadastro do aluno: {aluno.nome}, matricula: {aluno.matricula}?")
                    if resposta:
                        self.__alunos.remove(aluno)
                        self.__tela_alunos.mostrar_mensagem(f"Aluno: {aluno.nome} foi excluido.")
                    else:
                        return self.tela_alunos.tela_opcoes()
                else:
                    return self.__tela_alunos.mostrar_mensagem("O aluno não foi encontrado.")
        else:
            return self.tela_alunos.mostrar_mensagem("Nenhum aluno cadastrado.")

    def listar_aluno(self):
        contador = 1
        if len(self.__alunos) == 0:
            return self.tela_alunos.mostrar_mensagem("\nAinda não temos alunos cadastrados.\n")
        dados_alunos = list()
        for aluno in self.__alunos:
            dados_alunos_dict = {
                "Nome": aluno.nome,
                "CPF": aluno.cpf,
                "Data de Nascimento": aluno.data_nascimento,
                "estado": aluno.endereco.estado,
                "cidade": aluno.endereco.cidade,
                "bairro": aluno.endereco.bairro,
                "matricula": aluno.matricula,
                "curso": aluno.curso
            }
            dados_alunos.append(dados_alunos_dict)

        return self.__tela_alunos.listar_alunos(dados_alunos) 

    def pesquisar_aluno_por_matricula(self, matricula: str):
        for item in self.__alunos:
            if item.matricula ==  matricula:
                return item
        