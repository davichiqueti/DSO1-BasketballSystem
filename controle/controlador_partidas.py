from entidade.partida import Partida
from tela.tela_partidas import TelaPartidas


class ControladorPartidas:
    def __init__(self) -> None:
        self.__partidas = list()
        self.__tela_partidas = TelaPartidas()
        self.__controlador_sistema = None
        self.__ultimo_codigo_gerado = 0

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
            self.tela_partidas.mostrar_mensagem('Nenhuma partida registrada')
            return
        dados_partidas = list()
        for partida in self.partidas:
            dados_partida = {
                'codigo': partida.codigo,
                'data': partida.data,
                'pontuacao_equipes': {
                    equipe.nome: pontuacao for equipe, pontuacao in partida.pontuacao.items()
                }
            }
            dados_partidas.append(dados_partida)
        self.tela_partidas.listar_partidas(dados_partidas)

    def incluir_partida(self):
        if len(self.controlador_sistema.controlador_equipes.equipes) < 2:
            self.tela_partidas.mostrar_mensagem(
                'Para registrar uma partida, o sistema deve ter ao mínimo 2 equipes cadastradas'
            )
            return
        dados = self.tela_partidas.incluir_partida()
        # Carregando dados
        data = dados['data']
        codigo_partida = self.__ultimo_codigo_gerado + 1
        # Tratamento para as equipes da partida
        codigo_equipe_1 = dados['codigo_equipe_1']
        codigo_equipe_2 = dados['codigo_equipe_2']
        indice_equipe_1 = self.controlador_sistema.controlador_equipes.pesquisar_equipe_por_codigo(codigo_equipe_1)
        indice_equipe_2 = self.controlador_sistema.controlador_equipes.pesquisar_equipe_por_codigo(codigo_equipe_2)
        if indice_equipe_1 is None:
            self.tela_partidas.mostrar_mensagem(f'Equipe com código "{indice_equipe_1}" não encontrado')
            return self.incluir_partida()
        if indice_equipe_2 is None:
            self.tela_partidas.mostrar_mensagem(f'Equipe com código "{codigo_equipe_2}" não encontrado')
            return self.incluir_partida()
        equipe_1 = self.controlador_sistema.controlador_equipes.equipes[indice_equipe_1]
        equipe_2 = self.controlador_sistema.controlador_equipes.equipes[indice_equipe_1]
        pontuacao = {equipe_1: dados['pontuacao_equipe_1'], equipe_2: dados['pontuacao_equipe_2']}
        # Instanciando objeto e armazenando na lista
        nova_partida = Partida(codigo_partida, data, equipes=[equipe_1, equipe_2], pontuacao=pontuacao)
        self.partidas.append(nova_partida)
        self.tela_partidas.mostrar_mensagem('Partida registrada com sucesso')

    def pesquisar_partida_por_codigo(self, codigo: int) -> int:
        """
        Retorna o índice do curso com o código informado.\n  
        Se nenhum curso possuir o código informado retorna `None`
        """
        for i in range(len(self.partidas)):
            if self.partidas[i].codigo == codigo:
                return i
