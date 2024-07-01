from entidade.partida import Partida
from tela.tela_partidas import TelaPartidas
from DAOs.partida_dao import PartidaDAO
import random
from exceptions.sem_registro_exception import SemRegistroException



class ControladorPartidas:
    def __init__(self, controlador_sistema):
        self.__partida_dao = PartidaDAO()
        self.__tela_partidas = TelaPartidas()
        self.__controlador_sistema = controlador_sistema

    def retornar(self):
        self.__controlador_sistema.abre_tela()


 

        #Metodos de Partida

    def listar_partidas(self):
        dados_partidas = []
        partidas = self.__partida_dao.get_all()
        try:
            if len(partidas) == 0:
                raise SemRegistroException()
        except SemRegistroException as e:
            return self.__tela_partidas.mostra_mensagem(e)
        
        for item in partidas:
            nome_equipe1 = self.__controlador_sistema.controlador_equipes.Retorna_nome_equipe_por_codigo(item.equipe1)
            nome_equipe2 = self.__controlador_sistema.controlador_equipes.Retorna_nome_equipe_por_codigo(item.equipe2)
            arbitro_nome = self.__controlador_sistema.controlador_arbitros.pesquisar_arbitros_por_cpf(item.cpf_arbitro).nome

            dados_partidas.append({
                "codigo": item.codigo, 
                "arbitro": arbitro_nome, 
                "equipe1": nome_equipe1, 
                "equipe2": nome_equipe2
                })
        
        return self.__tela_partidas.listar_partidas(dados_partidas)

    def incluir_partida(self):
        self.__controlador_sistema.controlador_equipes.listar_equipes()
        dados_partida = self.__tela_partidas.incluir_partida()
        codigo = int(dados_partida['1'])
        cpf_arbitro = dados_partida['2']
        codigo_equipe1 = int(dados_partida['3'])
        codigo_equipe2 = int(dados_partida['4'])

        equipe1 = self.__controlador_sistema.controlador_equipes.pesquisar_equipe_por_codigo(codigo_equipe1)
        equipe2 = self.__controlador_sistema.controlador_equipes.pesquisar_equipe_por_codigo(codigo_equipe2)
        arbitro = self.__controlador_sistema.controlador_arbitros.pesquisar_arbitros_por_cpf(cpf_arbitro)
        if equipe1 is None:
            return self.__tela_partidas.mostra_mensagem("Equipe 1 não encontrada.")
        if equipe2 is None:
            return self.__tela_partidas.mostra_mensagem("Equipe 2 não encontrada.")
        if arbitro is None:
            return self.__tela_partidas.mostra_mensagem("Arbitro não encontrado.")

        nova_partida = Partida(codigo, cpf_arbitro, codigo_equipe1, codigo_equipe2)
        for partida in self.__partida_dao.get_all():
            if partida.codigo == nova_partida.codigo:
                return self.__tela_partidas.mostra_mensagem("Essa partida já foi adicionada ao campeonato!")
            
        self.__partida_dao.add(nova_partida)
        return self.__tela_partidas.mostra_mensagem(f"Partida {nova_partida.codigo} foi incluida.")
            
#exclusão: ok
    def excluir_partida(self):
        self.listar_partidas()
        if len(self.__partida_dao.get_all()) == 0:
            return self.__tela_partidas.mostra_mensagem('Nenhum curso cadastrado')
        codigo_partida = self.__tela_partidas.selecionar_partida()
        partida = self.pesquisar_partida_por_codigo(int(codigo_partida))
        if partida is None:
            self.__tela_partidas.mostra_mensagem(
                f'Curso com código "{codigo_partida}" não encontrado'
            )
        else:
            self.__partida_dao.remove(partida.codigo)
            self.__tela_partidas.mostra_mensagem('Partida excluída')

        
    def pesquisar_partida_por_codigo(self, codigo: int) -> Partida:
        for partida in self.__partida_dao.get_all():
            if partida.codigo == codigo:
                if isinstance(partida, Partida):
                    return partida

    def abre_tela(self):
        lista_opcoes = {
            1: self.listar_partidas,
            2: self.incluir_partida,
            3: self.excluir_partida,
            0: self.retornar
        }
        continua = True
        while continua:
            lista_opcoes[self.__tela_partidas.mostrar_opcoes()]()