from tela.tela_sistema import TelaSistema
from controle.controlador_cursos import ControladorCursos
from controle.controlador_equipes import ControladorEquipes
from controle.controlador_arbitros import ControladorArbitros
from controle.controlador_alunos import ControladorAlunos
from controle.controlador_partidas import ControladorPartidas
from controle.controlador_campeonatos import ControladorCampeonatos


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_cursos = ControladorCursos(self)
        self.__controlador_equipes = ControladorEquipes(self)
        self.__controlador_arbitros = ControladorArbitros(self)
        self.__controlador_alunos = ControladorAlunos(self)
        self.__controlador_partidas = ControladorPartidas(self)
        self.__controlador_campeonatos = ControladorCampeonatos(self)

    @property
    def tela_sistema(self) -> TelaSistema:
        return self.__tela_sistema

    @property
    def controlador_cursos(self) -> ControladorCursos:
        return self.__controlador_cursos

    @property
    def controlador_equipes(self) -> ControladorEquipes:
        return self.__controlador_equipes

    @property
    def controlador_arbitros(self) -> ControladorArbitros:
        return self.__controlador_arbitros

    @property
    def controlador_partidas(self) -> ControladorPartidas:
        return self.__controlador_partidas

    @property
    def controlador_alunos(self) -> ControladorAlunos:
        return self.__controlador_alunos

    @property
    def controlador_campeonatos(self) -> ControladorCampeonatos:
        return self.__controlador_campeonatos

    def inicializa_sistema(self):
        self.abre_tela()
    
    def cadastra_aluno(self):
        self.__controlador_alunos.abre_tela()
    
    def cadastra_curso(self):
        self.__controlador_cursos.abre_tela()

    def cadastra_arbitro(self):
        self.__controlador_arbitros.abre_tela()
    
    def cadastra_campeonato(self):
        self.__controlador_campeonatos.abre_tela()
    
    def cadastra_equipe(self):
        self.__controlador_equipes.abre_tela()
    
    def cadastra_partida(self):
        self.__controlador_partidas.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {
                        1: self.cadastra_aluno, 
                        2: self.cadastra_curso, 
                        3: self.cadastra_arbitro,
                        4: self.cadastra_campeonato, 
                        5: self.cadastra_equipe, 
                        6: self.cadastra_partida, 
                        0: self.encerra_sistema
                        }

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()