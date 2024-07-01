from entidade.equipe import Equipe
from DAOs.equipe_dao import EquipeDAO
from tela.tela_equipes import TelaEquipes
import PySimpleGUI as sg

class ControladorEquipes:
    def __init__(self, controlador_sistema):
        self.__equipeDAO = EquipeDAO()
        self.__tela_equipes = TelaEquipes()
        self.__controlador_sistema = controlador_sistema

    def listar_equipes(self):
        if len(self.__equipeDAO.get_all()) == 0:
            return self.__tela_equipes.mostra_mensagem('Nenhuma Equipe cadastrada')
        
        dados_equipes = list()
        for equipe in self.__equipeDAO.get_all():
            lista_equipes = list()
            for aluno in equipe.alunos:
                nome_aluno = str(aluno)
                lista_equipes.append(nome_aluno)

            dados_equipes.append({
                'codigo': equipe.codigo,
                'nome': equipe.nome,
                'nome_curso': equipe.curso.nome,
                'equipes': lista_equipes
            })
        self.__tela_equipes.listar_equipes(dados_equipes)

    def incluir_equipe(self) -> bool:
        dados = self.__tela_equipes.incluir_equipe()
        nome = dados['nome']
        codigo = dados['codigo']
        codigo_curso = dados['codigo_curso']
        # Verificando duplicidade de códigos
        if self.pesquisar_equipe_por_codigo(codigo) is not None:
            self.__tela_equipes.mostra_mensagem('Uma equipe com este código já existe!')
            return False
        # Verificando existencia do curso
        curso = self.__controlador_sistema.controlador_cursos.pesquisar_curso_por_codigo(codigo_curso)
        if curso is None:
            self.__tela_equipes.mostra_mensagem('Não existe curso com este código!')
            return False
        alunos = []

        # Cadastrando a equipe
        nova_equipe = Equipe(nome, curso, codigo, alunos)
        self.__equipeDAO.add(nova_equipe)
        self.__tela_equipes.mostra_mensagem('Equipe cadastrada com sucesso')
        return True

    def excluir_equipe(self):
        if len(self.__equipeDAO.get_all()) == 0:
            return self.__tela_equipes.mostra_mensagem('Nenhuma equipe cadastrada')
        codigo = self.__tela_equipes.selecionar_equipe()
        equipe = self.pesquisar_equipe_por_codigo(int(codigo))
        if equipe is None:
            self.__tela_equipes.mostra_mensagem(
                'Equipe com código não encontrada'
            )
        else:
            self.__equipeDAO.remove(equipe.codigo)
            self.__tela_equipes.mostra_mensagem('Equipe excluída com sucesso')


    def incluir_aluno_equipe(self):
        dados_inclusao = self.__tela_equipes.inclui_aluno_equipe()
        codigo_aluno_equipe = dados_inclusao[0]
        cpf_aluno =  dados_inclusao[1]

        equipe = self.pesquisar_equipe_por_codigo(codigo_aluno_equipe)
        

        if equipe is None:
            self.__tela_equipes.mostra_mensagem(f'Equipe com código "{codigo_aluno_equipe}" não encontrada')
            return
        
        if len(equipe.alunos) > 4:
            self.__tela_equipes.mostra_mensagem('Equipe já está cheia')
            return
        
        aluno = self.__controlador_sistema.controlador_alunos.pesquisar_aluno_por_cpf(str(cpf_aluno))
        equipe.alunos.append(aluno.nome)
        self.__equipeDAO.update(equipe.codigo)
        self.__tela_equipes.mostra_mensagem(f'Aluno {aluno.nome} adicionado com sucesso')
    
    def excluir_aluno_equipe(self):
        dados_exclusao = self.__tela_equipes.exclui_aluno_equipe()
        codigo_aluno_equipe = dados_exclusao[0]
        cpf_aluno =  dados_exclusao[1]

        equipe = self.pesquisar_equipe_por_codigo(codigo_aluno_equipe)
        

        if equipe is None:
            self.__tela_equipes.mostra_mensagem(f'Equipe com código "{codigo_aluno_equipe}" não encontrada')
            return
        
        if len(equipe.alunos) == 0:
            self.__tela_equipes.mostra_mensagem('Equipe está vazia.')
            return
        
        aluno = self.__controlador_sistema.controlador_alunos.pesquisar_aluno_por_cpf(str(cpf_aluno))

        if aluno is None:
            self.__tela_equipes.mostra_mensagem(f'Aluno com CPF "{cpf_aluno}" não encontrado')
            return
        
        equipe.alunos.remove(aluno.nome)
        self.__equipeDAO.update(equipe)
        self.__tela_equipes.mostra_mensagem(f'Aluno {aluno.nome} excluido com sucesso')
    



    def pesquisar_equipe_por_codigo(self, codigo: int) -> Equipe:
        for equipe in self.__equipeDAO.get_all():
            if equipe.codigo == codigo:
                return equipe
    
    def Retorna_nome_equipe_por_codigo(self, codigo: int) -> str:
        for equipe in self.__equipeDAO.get_all():
            if equipe.codigo == codigo:
                nome_equipe = equipe.nome
                return nome_equipe
        

    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_equipe,
            2: self.excluir_equipe,
            3: self.listar_equipes,
            4: self.incluir_aluno_equipe,
            5: self.excluir_aluno_equipe,
            0: self.retornar
        }

        continua = True
        while continua:
            lista_opcoes[self.__tela_equipes.mostrar_opcoes()]()
    
