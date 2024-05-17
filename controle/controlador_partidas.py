from entidade.partida import Partida
from tela.tela_partidas import TelaPartidas


class ControladorPartidas:
    def __init__(self) -> None:
        self.__partidas = list()
        self.__tela_partidas = TelaPartidas()
        self.__controlador_sistema = None

    @property
    def partidas(self) -> list[Partida]:
        return self.__partidas

    @property
    def tela_partidas(self) -> TelaPartidas:
        return self.__tela_partidas

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @controlador_sistema.setter
    def controlador_sistema(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema

    def mostrar_opcoes(self):
        opcoes = {
            '1': 'Listar Partidas',
            '2': 'Incluir Partida',
            #'3': 'Alterar Partida',
            #'4': 'Excluir Partida',
            '10': 'Sair'
        }
        opcao_escolhida = str()
        while True:
            opcao_escolhida = self.tela_partidas.mostrar_opcoes(opcoes)
            match opcao_escolhida:
                case '1': self.listar_partidas()
                case '2': self.incluir_partida()
                #case '3': self.alterar_partida()
                #case '4': self.excluir_partida()
                case '10': break
                case _: self.tela_partidas.mostrar_mensagem('Opção Escolhida Não Existe')

    def listar_partidas(self):
        if len(self.partidas) == 0:
            return self.tela_partidas.mostrar_mensagem('Nenhuma partida cadastrada')
        dados_partidas = list()
        for partida in self.partidas:
            dados_partidas.append({
                'codigo': partida.codigo,
                'data': partida.data,
                'pontuacao': partida.pontuacao,
                'equipes': partida.equipes
            })
        self.tela_partidas.listar_partidas(dados_partidas)

    def incluir_partida(self):
        dados = self.tela_partidas.incluir_partida()
        nova_partida = Partida(dados, dados)
        self.partidas.append(nova_partida)
        self.tela_partidas.mostrar_mensagem('Curso cadastrado com sucesso')

    def pesquisar_partida_por_codigo(self, codigo: int) -> int:
        """
        Retorna o índice do curso com o código informado.\n  
        Se nenhum curso possuir o código informado retorna `None`
        """
        for i in range(len(self.partidas)):
            if self.partidas[i].codigo == codigo:
                return i
