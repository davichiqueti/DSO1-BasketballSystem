from entidade.campeonato import Campeonato
from tela.tela_campeonatos import TelaCampeonatos
from DAOs.campeonato_dao import CampeonatoDAO
import random
from exceptions.sem_registro_exception import SemRegistroException



class ControladorCampeonatos:
    def __init__(self, controlador_sistema):
        self.__CampeonatoDAO = CampeonatoDAO()
        self.__tela_campeonatos = TelaCampeonatos()
        self.__controlador_sistema = controlador_sistema


    def retornar(self):
        self.__controlador_sistema.abre_tela()


    def criar_campeonato(self):
        self.listar_campeonatos()
        self.__controlador_sistema.controlador_partidas.listar_partidas()
        dados_camp = self.__tela_campeonatos.criar_campeonato()
        codigo_campeonato = int(dados_camp['codigo_campeonato'])
        codigo_partida = int(dados_camp['codigo_partida'])

        for camp in self.__CampeonatoDAO.get_all():
            if camp.codigo_campeonato == codigo_campeonato:
                return self.__tela_campeonatos.mostra_mensagem("Campeonato já cadastrado")
        
        partida = self.__controlador_sistema.controlador_partidas.pesquisar_partida_por_codigo(codigo_partida)
        pontuacao_equipe1 = random.randint(0, 150)  
        pontuacao_equipe2 = random.randint(0, 150)  

        nome_equipe1 = self.__controlador_sistema.controlador_equipes.pesquisar_equipe_por_codigo(partida.equipe1).nome
        nome_equipe2 = self.__controlador_sistema.controlador_equipes.pesquisar_equipe_por_codigo(partida.equipe2).nome

        if pontuacao_equipe1 > pontuacao_equipe2:
            vencedor = nome_equipe2
        elif pontuacao_equipe2 > pontuacao_equipe1:
            vencedor = nome_equipe1
        else:
            vencedor = "Empate"

        campeonato_novo = Campeonato(codigo_campeonato, partida, pontuacao_equipe1, pontuacao_equipe2, vencedor)
        self.__CampeonatoDAO.add(campeonato_novo)
        self.__tela_campeonatos.mostra_mensagem("Campeonato criado com sucesso")
        return 


    def listar_campeonatos(self):
        dados_campeonatos = []
        camp = self.__CampeonatoDAO.get_all()
        try:
            if len(camp) == 0:
                raise SemRegistroException()
        except SemRegistroException as e:
            return self.__tela_campeonatos.mostra_mensagem(e)
        
        for item in camp:
            nome_equipe1 = self.__controlador_sistema.controlador_equipes.pesquisar_equipe_por_codigo(item.partida.equipe1).nome
            nome_equipe2 = self.__controlador_sistema.controlador_equipes.pesquisar_equipe_por_codigo(item.partida.equipe2).nome
            dados_campeonatos.append({
                "codigo": item.codigo_campeonato, 
                "arbitro": item.partida.arbitro, 
                "equipe1": nome_equipe1, 
                "pontuacao_equipe1": item.pontuacao_equipe1,
                "equipe2": nome_equipe2,
                "pontuacao_equipe2": item.pontuacao_equipe2,
                "vencedor": item.vencedor
                })
        
        return self.__tela_campeonatos.listar_campeonato(dados_campeonatos)




    def pesquisar_campeonato_por_codigo(self, codigo: int) -> Campeonato:
        for campeonato in self.__CampeonatoDAO.get_all():
            if campeonato.codigo == codigo:
                if isinstance(campeonato, Campeonato):
                    return campeonato


    
    def abre_tela(self):
        lista_opcoes = {
            1: self.criar_campeonato,
            2: self.listar_campeonatos,
            0: self.retornar
        }

        continua = True
        while continua:
            lista_opcoes[self.__tela_campeonatos.mostrar_opcoes()]()
