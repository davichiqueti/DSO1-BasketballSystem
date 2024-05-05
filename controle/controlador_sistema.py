from controle.controlador_cursos import ControladorCursos
from tela.tela_sistema import TelaSistema
from tela.tela_cursos import TelaCursos


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_cursos = ControladorCursos()
        self.__tela_cursos = TelaCursos()
        self.__controlador_cursos.tela_cursos = self.__tela_cursos
        self.__tela_cursos.controlador_cursos = self.__controlador_cursos

    @property
    def tela_sistema(self) -> TelaSistema:
        return self.__tela_sistema

    @property
    def controlador_cursos(self) -> ControladorCursos:
        return self.__controlador_cursos

    def mostrar_opcoes(self):
        opcoes = {
            '1': 'Módulo de Cursos',
            '10': 'Sair'
        }
        opcao_escolhida = str()
        while True:
            opcao_escolhida = self.tela_sistema.mostrar_opcoes(opcoes)
            match opcao_escolhida:
                case '1': self.controlador_cursos.mostrar_opcoes()
                case '10': break
                case _: self.tela_sistema.mostrar_mensagem('Opção Escolhida Não Existe')
