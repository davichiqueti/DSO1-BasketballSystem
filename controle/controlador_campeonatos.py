from entidade.campeonato import Campeonato
from tela.tela_campeonatos import TelaCampeonatos



class ControladorCampeonatos:
    def __init__(self):
        self.__campeonatos = []
        self.__tela_campeonatos = TelaCampeonatos()
        self.__controlador_sistema = None


    @property
    def campeonatos(self) -> list[Campeonato]:
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
        codigo_camp = dict_incluir_campeonato["codigo_campeonato"]
        descricao = dict_incluir_campeonato["descricao_campeonato"]
        camp_equipes = list()
        lista_de_codigo = dict_incluir_campeonato["lista_de_codigo"]

        #verifica se campeonato já está cadastrado
        for campeonato in self.__campeonatos:
            if campeonato.codigo == codigo_camp:
                return self.tela_campeonatos.mostrar_mensagem("O codigo informado já está cadastrado.")
            
            
        for item in lista_de_codigo:
            equipe = self.controlador_sistema.controlador_equipes.pesquisar_equipe_por_codigo(item)
            if equipe is None:
                self.tela_campeonatos.mostrar_mensagem(f'Equipe com código "{item}" não encontrado')
            else:
                if equipe.codigo not in camp_equipes:
                    camp_equipes.append(equipe)
                else:
                    return self.__tela_campeonatos.mostrar_mensagem("A equipe já está cadastrada no campeonato.")
            
    
        novo_campeonato = Campeonato(codigo_camp, descricao, camp_equipes)
        if isinstance(novo_campeonato, Campeonato):
            self.__campeonatos.append(novo_campeonato)
            self.tela_campeonatos.mostrar_mensagem(f"Campeonato {novo_campeonato.codigo} incluido.")
            for item in novo_campeonato.equipes:
                self.tela_campeonatos.mostrar_mensagem(f"Equipe {item.codigo} cadastrada.")
            return self.tela_campeonatos.mostrar_mensagem("cadastro finalizado.")
        else:
            return self.tela_campeonatos.mostrar_mensagem(f"Campeonato {novo_campeonato.codigo}, {novo_campeonato.descricao} está incorreto")




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
            return self.tela_campeonatos.mostrar_mensagem(f"A partida com código {nova_partida.codigo} foi incluida no campeonato {campeonato.codigo}.")
          




    def alterar_campeonato(self):
        if len(self.__campeonatos) == 0:
            return self.tela_campeonatos.mostrar_mensagem("\nAinda não temos campeonatos cadastrados.\n")
        dict_alterar_campeonato = self.tela_campeonatos.alterar_campeonato()
        #verifica se campeonato existe na lista
        codigo = dict_alterar_campeonato["codigo_campeonato_alteracao"]
        for camp in self.__campeonatos:
            if camp.codigo == codigo:
                campeonato_alteracao = camp
                break
            else:
                self.tela_campeonatos.mostrar_mensagem("Código de Campeonato para alteração é inválido.")
                return self.tela_campeonatos.alterar_campeonato()

        descricao_nova = dict_alterar_campeonato["descricao_campeonato_novo"]
        campeonato_alteracao.descricao = descricao_nova
        return self.tela_campeonatos.mostrar_mensagem(f"Campeonato com código {codigo} foi alterada.")
                    




    def excluir_campeonato(self):
        if len(self.__campeonatos) == 0:
            return self.tela_campeonatos.mostrar_mensagem("\nAinda não temos campeonatos cadastrados.\n")
        codigo_campeonato_exclusao  = self.tela_campeonatos.excluir_campeonato()
        for campeonato in self.__campeonatos:
            if campeonato.codigo == codigo_campeonato_exclusao:
                campeonato_ex = campeonato
                if self.tela_campeonatos.confirmar_acao(f"Tem certeza que deseja excluir o campeonato com código {campeonato_ex.codigo}?"):
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
                "codigo_campeonato": campeonato.codigo,
                "descricao": campeonato.descricao,
                "equipes": campeonato.equipes
            }
            dados_campeonatos.append(dados_campeonatos_dict)
        return self.tela_campeonatos.listar_campeonatos(dados_campeonatos)

    def exibir_relatorios_campeonato(self):
        # Selecionando campeonato para exibir os relátorios
        dados_campeonatos = [{'descricao': campeonato.descricao, 'codigo': campeonato.codigo} for campeonato in self.campeonatos]
        codigo_campeonato = self.tela_campeonatos.selecionar_campeonato(dados_campeonatos)
        indice_campeonato = self.pesquisar_campeonato_por_codigo(codigo_campeonato)
        campeonato = self.campeonatos[indice_campeonato]
        # Gerando relátorios do campeonato
        podio_campeonato = [{"nome": equipe.nome, "codigo": equipe.codigo, "pontos": pontos} for equipe, pontos in campeonato.pontuacao.items()]
        podio_campeonato = sorted(podio_campeonato, key=lambda x: x["pontos"], reverse=True)
        pontos_totais_equipe = dict()
        pontos_totais_jogador = dict()
        for partida in campeonato.partidas:
            for equipe, pontuacao in partida.pontuacao.items():
                pontos_totais_equipe[equipe] = pontos_totais_equipe.get(equipe, 0) + pontuacao["total"]
                for jogador, pontos in pontuacao['pontuacao_individual'].items():
                    pontos_totais_jogador[jogador] = pontos_totais_jogador.get(jogador, 0) + pontos
        pontos_totais_equipe = [{'nome': equipe.nome, 'codigo': equipe.codigo, 'pontos': pontos} for equipe, pontos in pontos_totais_equipe.items()]
        pontos_totais_equipe = sorted(pontos_totais_equipe, key=lambda x: x["pontos"], reverse=True)[:5]
        pontos_totais_jogador = [{'nome': jogador.nome, 'matricula': jogador.matricula, 'pontos': pontos} for jogador, pontos in pontos_totais_jogador.items()]
        pontos_totais_jogador = sorted(pontos_totais_jogador, key=lambda x: x["pontos"], reverse=True)[:5]
        # Retornando dados dos relátorios processados para a tela
        dados_relatorios = {
            'descricao_campeonato': campeonato.descricao,
            'podio': podio_campeonato,
            'equipes_mais_pontos': pontos_totais_equipe,
            'alunos_mais_pontos': pontos_totais_jogador
        }
        self.tela_campeonatos.exibir_relatorios_campeonato(dados_relatorios)

    def pesquisar_campeonato_por_codigo(self, codigo: int) -> int:
        for i in range(len(self.__campeonatos)):
            campeonato = self.campeonato[i]
            if campeonato.codigo == codigo:
                return i
    
