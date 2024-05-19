from entidade.campeonato import Campeonato
from tela.tela_campeonatos import TelaCampeonatos



class ControladorCampeonatos:
    def __init__(self):
        self.__campeonatos = []
        self.__tela_campeonatos = TelaCampeonatos()
        self.__controlador_sistema = None


    @property
    def campeonato(self):
        return self.__campeonato
        
    @campeonato.setter
    def campeonato(self, campeonato):
        self.__campeonato = campeonato

    @property
    def tela_campeonatos(self) -> TelaCampeonatos:
        return self.__tela_campeonatos

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @controlador_sistema.setter
    def controlador_sistema(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema

    def mostrar_opcoes(self):
        retorno = 0
        while True:
            retorno = self.tela_campeonatos.tela_opcoes()
            if retorno == 1:
                self.incluir_campeonato()
            elif retorno == 2:
                self.incluir_partida_campeonato()
            elif retorno == 3:
                self.alterar_campeonato()
            elif retorno == 4:
                self.excluir_campeonato()
            elif retorno == 5:
                self.listar_campeonato()
            elif retorno == 6:
                self.exibir_relatorios_campeonato()
            elif retorno == 10:
                break
            else:
                self.tela_campeonatos.mostrar_mensagem('Opção inválida.')

