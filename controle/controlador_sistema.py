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
        self.__controlador_cursos = None
        self.__controlador_equipes = None
        self.__controlador_arbitros = None
        self.__controlador_alunos = None
        self.__controlador_partidas = None
        self.__controlador_campeonatos = None

    @property
    def tela_sistema(self) -> TelaSistema:
        return self.__tela_sistema

    @property
    def controlador_cursos(self) -> ControladorCursos:
        return self.__controlador_cursos

    @controlador_cursos.setter
    def controlador_cursos(self, controlador_cursos: ControladorCursos):
        if isinstance(controlador_cursos, ControladorCursos):
            self.__controlador_cursos = controlador_cursos
        else:
            raise TypeError(
                'ControladorSistema.controlador_cursos deve ser do tipo "ControladorCursos"'
            )

    @property
    def controlador_equipes(self) -> ControladorEquipes:
        return self.__controlador_equipes

    @controlador_equipes.setter
    def controlador_equipes(self, controlador_equipes: ControladorEquipes):
        if isinstance(controlador_equipes, ControladorEquipes):
            self.__controlador_equipes = controlador_equipes
        else:
            raise TypeError(
                'ControladorSistema.__controlador_equipes deve ser do tipo "ControladorEquipes"'
            )

    @property
    def controlador_arbitros(self):
        return self.__controlador_arbitros

    @controlador_arbitros.setter
    def controlador_arbitros(self, controlador_arbitros: ControladorArbitros):
        if isinstance(controlador_arbitros, ControladorArbitros):
            self.__controlador_arbitros = controlador_arbitros
        else:
            raise TypeError(
                'ControladorSistema.controlador_arbitros deve ser do tipo "ControladorArbitros"')

    @property
    def controlador_partidas(self):
        return self.__controlador_partidas

    @controlador_partidas.setter
    def controlador_partidas(self, controlador_partidas: ControladorPartidas):
        if isinstance(controlador_partidas, ControladorPartidas):
            self.__controlador_partidas = controlador_partidas
        else:
            raise TypeError(
                'ControladorSistema.controlador_partidas deve ser do tipo "ControladorPartidas"')

    @property
    def controlador_alunos(self):
        return self.__controlador_alunos

    @controlador_alunos.setter
    def controlador_alunos(self, controlador_alunos: ControladorAlunos):
        if isinstance(controlador_alunos, ControladorAlunos):
            self.__controlador_alunos = controlador_alunos
        else:
            raise TypeError(
                "ControladorSistema.__controlador_alunos deve ser do tipo 'ControladorAlunos'.")

    @property
    def controlador_campeonatos(self):
        return self.__controlador_campeonatos

    @controlador_campeonatos.setter
    def controlador_campeonatos(self, controlador_campeonatos: ControladorCampeonatos):
        if isinstance(controlador_campeonatos, ControladorCampeonatos):
            self.__controlador_campeonatos = controlador_campeonatos
        else:
            raise TypeError(
                "ControladorSistema.__controlador_campeonatos deve ser do tipo 'ControladorCampeonatos'.")

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_alunos(self):
        self.__controlador_alunos.abre_tela()

    def cadastra_cursos(self):
        self.__controlador_cursos.abre_tela()

    def cadastra_arbitros(self):
        self.__controlador_arbitros.abre_tela()

    def cadastra_emprestimos(self):
        self.__controlador_campeonatos.abre_tela()

    def cadastra_equipes(self):
        self.__controlador_equipes.abre_tela()

    def cadastra_partidas(self):
        self.__controlador_partidas.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_alunos, 2: self.cadastra_cursos, 3: self.cadastra_arbitros,
                        4: self.cadastra_emprestimos, 5: self.cadastra_equipes, 6: self.cadastra_partidas, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()