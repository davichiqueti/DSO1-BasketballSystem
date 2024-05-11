from tela.tela_sistema import TelaSistema
from controle.controlador_cursos import ControladorCursos
from controle.controlador_equipes import ControladorEquipes


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_cursos = None
        self.__controlador_equipes = None

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

    def mostrar_opcoes(self):
        opcoes = {
            '1': 'Módulo de Cursos',
            '2': 'Módulo de Equipes',
            '10': 'Sair'
        }
        opcao_escolhida = str()
        while True:
            opcao_escolhida = self.tela_sistema.mostrar_opcoes(opcoes)
            match opcao_escolhida:
                case '1': self.controlador_cursos.mostrar_opcoes()
                case '2': self.controlador_equipes.mostrar_opcoes()
                case '10': break
                case _: self.tela_sistema.mostrar_mensagem('Opção Escolhida Não Existe')
