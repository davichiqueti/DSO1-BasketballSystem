from tela.tela_sistema import TelaSistema
from controle.controlador_cursos import ControladorCursos
from controle.controlador_equipes import ControladorEquipes
from controle.controlador_arbitros import ControladorArbitros
from controle.controlador_alunos import ControladorAlunos
from controle.controlador_partidas import ControladorPartidas


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_cursos = None
        self.__controlador_equipes = None
        self.__controlador_arbitros = None
        self.__controlador_alunos = None
        self.__controlador_partidas = None

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
            raise TypeError('ControladorSistema.controlador_arbitros deve ser do tipo "ControladorArbitros"')

    @property
    def controlador_partidas(self):
        return self.__controlador_partidas
    
    @controlador_partidas.setter
    def controlador_partidas(self, controlador_partidas: ControladorPartidas):
        if isinstance(controlador_partidas, ControladorPartidas):
            self.__controlador_partidas = controlador_partidas
        else:
            raise TypeError('ControladorSistema.controlador_partidas deve ser do tipo "ControladorPartidas"')

    @property
    def controlador_alunos(self):
        return self.__controlador_alunos

    @controlador_alunos.setter
    def controlador_alunos(self, controlador_alunos: ControladorAlunos):
        if isinstance(controlador_alunos, ControladorAlunos):
            self.__controlador_alunos = controlador_alunos
        else:
            raise TypeError("ControladorSistema.__controlador_alunos deve ser do tipo 'ControladorAlunos'.")

    @property
    def controlador_alunos(self):
        return self.__controlador_alunos

    @controlador_alunos.setter
    def controlador_alunos(self, controlador_alunos: ControladorAlunos):
        if isinstance(controlador_alunos, ControladorAlunos):
            self.__controlador_alunos = controlador_alunos
        else:
            raise TypeError("ControladorSistema.__controlador_alunos deve ser do tipo 'ControladorAlunos'.")

    def mostrar_opcoes(self):
        opcoes = {
            '1': 'Módulo de Cursos',
            '2': 'Módulo de Equipes',
            '3': 'Módulo de Arbitros',
            '4': 'Módulo de Alunos',
            '5': 'Módulo de Partidas',
            '10': 'Sair'
        }
        opcao_escolhida = str()
        while True:
            opcao_escolhida = self.tela_sistema.mostrar_opcoes(opcoes)
            match opcao_escolhida:
                case '1': self.controlador_cursos.mostrar_opcoes()
                case '2': self.controlador_equipes.mostrar_opcoes()
                case '3': self.controlador_arbitros.mostrar_opcoes()
                case '4': self.controlador_alunos.mostrar_opcoes()
                case '5': self.controlador_partidas.mostrar_opcoes()
                case '10': break
                case _: self.tela_sistema.mostrar_mensagem('Opção Escolhida Não Existe')
