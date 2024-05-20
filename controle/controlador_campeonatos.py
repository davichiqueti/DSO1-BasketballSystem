from entidade.campeonato import Campeonato
from tela.tela_campeonatos import TelaCampeonatos
from controle.controlador_sistema import *
import time


class ControladorCampeonatos:
    def __init__(self):
        self.__campeonatos = []
        self.__tela_campeonatos = TelaCampeonatos()
        self.__controlador_sistema = None


    @property
    def campeonatos(self):
        return self.__campeonatos
        

    @campeonatos.setter
    def campeonatos(self, campeonatos):
        self.__campeonatos = campeonatos


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
                self.listar_campeonatos()
            elif retorno == 6:
                self.exibir_relatorios_campeonato()
            elif retorno == 10:
                break
            else:
                self.tela_campeonatos.mostrar_mensagem('Opção inválida.')





    def incluir_campeonato(self):
        dict_incluir_campeonato = self.tela_campeonatos.incluir_campeonato()
        codigo = dict_incluir_campeonato["codigo_campeonato"]
        equipes = dict_incluir_campeonato["lista_equipes"]
        descricao = dict_incluir_campeonato["descricao"]
        novo_campeonato = Campeonato(codigo, descricao, equipes)
        if isinstance(novo_campeonato, Campeonato):
            self.__campeonatos.append(Campeonato)





    def incluir_partida_campeonato(self):
        if len(self.__campeonatos) == 0:
            return self.tela_campeonatos.mostrar_mensagem("\nAinda não temos campeonatos cadastrados.\n")
        dict_retorno = self.tela_campeonatos.incluir_partida_campeonato()
        retorno = dict_retorno["codigo_campeonato"] 
        if retorno == 'incluir':
            return self.__controlador_sistema.controlador_partidas.incluir_partida()
        else:
            #definindo campeonato e partida
            codigo_campeonato = dict_retorno["codigo_campeonato"]
            indice_campeonato = self.pesquisar_campeonato_por_codigo(codigo_campeonato)
            if indice_campeonato != None:
                campeonato = self.__campeonatos[indice_campeonato]
            else:
                return self.tela_campeonatos.mostrar_mensagem("O codigo de campeonato não corresponde a nenhum campeonato cadastrado.")
            
            codigo_partida = dict_retorno["codigo_partida"]
            indice_partida = self.__controlador_sistema.controlador_partidas.pesquisar_partida_por_codigo(codigo_partida)
            if indice_partida != None:
                nova_partida = self.controlador_sistema.controlador_partidas.partidas[indice_partida]
            else:
                return self.tela_campeonatos.mostrar_mensagem("O codigo de partida não corresponde a nenhuma partida cadastrada.")
            #inclusão da partida
            for partidas in self.campeonato.partidas:
                if partidas.codigo == nova_partida.codigo:
                    return self.tela_campeonatos.mostrar_mensagem("O codigo de partida já está vinculado a uma partida existente nesse campeonato.")
            
            self.campeonato.partida.append(nova_partida)
            return self.tela_campeonatos.mostrar_mensagem(f"A partida com código {nova_partida.codigo} foi incluida no campeonato {campeonato.nome}, {campeonato.codigo}.")
          




    def alterar_campeonato(self):
        if len(self.__campeonatos) == 0:
            return self.tela_campeonatos.mostrar_mensagem("\nAinda não temos campeonatos cadastrados.\n")
        dict_alterar_campeonato = self.tela_campeonatos.alterar_campeonato()
        #verifica se campeonato existe na lista
        for camp in self.__campeonatos:
            if camp.codigo == dict_alterar_campeonato["codigo_campeonato"]:
                campeonato_alteracao = camp
                break
            else:
                self.tela_campeonatos.mostrar_mensagem("Código de Campeonato inválido.")
                time.sleep(2)
                return self.tela_campeonatos.alterar_campeonato()
        equipes_alterar = list()
        #verificacao equipes
        for item in dict_alterar_campeonato["codigos_alteracoes_equipes"]:
            for equipes in self.campeonato.equipe:
                if equipes.codigo == item:
                    equipes_alterar.append(equipes)
                else:
                    self.tela_campeonatos.mostrar_mensagem(f"Codigo de equipe número: {item} está incorreto")
                    time.sleep(2)
                    return self.tela_campeonatos.alterar_campeonato()
        campeonato_alteracao.codigo = dict_alterar_campeonato["codigo_campeonato"]
        for item in campeonato_alteracao.equipe:
            campeonato_alteracao.item = equipes_alterar[item]
                    




    def excluir_campeonato(self):
        if len(self.__campeonatos) == 0:
            return self.tela_campeonatos.mostrar_mensagem("\nAinda não temos campeonatos cadastrados.\n")
        info_campeonato = self.tela_campeonatos.excluir_campeonato()
        for campeonato in self.__campeonatos:
            if campeonato.codigo == campeonato.info_campeonato:
                campeonato_ex = campeonato
                if self.tela_campeonatos.confirmar_acao(f"Tem certeza que deseja excluir o campeonato com código {info_campeonato}?"):
                    self.__campeonatos.remove(campeonato_ex)
                    return self.tela_campeonatos.mostrar_mensagem(f"Campeonato excluido.")
        self.tela_campeonatos.mostrar_mensagem("O codigo informado não corresponde a nenhum campeonato cadastrado, por favor digite um código valido")
        self.tela_campeonatos.excluir_campeonato()





    def listar_campeonatos(self):
        if len(self.__campeonatos) == 0:
            return self.tela_campeonatos.mostrar_mensagem("\nAinda não temos campeonatos cadastrados.\n")
        dados_campeonatos = list()
        for campeonato in self.__campeonatos:
            dados_campeonatos_dict = {
                "Nome": campeonato.nome,
                "CPF": arbitro.cpf,
            }
            dados_campeonatos.append(dados_campeonatos_dict)
        return self.tela_campeonatos.listar_campeonatos(dados_campeonatos)
    
    def pesquisar_campeonato_por_codigo(self, codigo: int) -> int:
        for i in range(len(self.__campeonatos)):
            campeonato = self.campeonato[i]
            if campeonato.codigo == codigo:
                return i
    
