from entidade.arbitro import Arbitro
from tela.tela_arbitros import TelaArbitros
from DAOs.arbitro_dao import ArbitroDAO

class ControladorArbitros():
    def __init__(self, controlador_sistema):
        self.__tela_arbitros = TelaArbitros()
        self.__arbitroDAO = ArbitroDAO()
        self.__controlador_sistema = controlador_sistema

    def incluir_arbitro(self):
        info_arbitro = self.__tela_arbitros.incluir_arbitro()
        novo_arbitro = Arbitro(info_arbitro['Nome'], 
                                info_arbitro['CPF'],
                                info_arbitro["Data de nascimento"], 
                                info_arbitro['Estado'], 
                                info_arbitro['Cidade'],
                                info_arbitro['Bairro'],
                                info_arbitro["Numero de partidas"]
                               )
        for arbitro_cadastrado in self.__arbitroDAO.get_all():
            if arbitro_cadastrado.cpf == novo_arbitro.cpf:
                self.__tela_arbitros.mostra_mensagem("Arbitro já cadastrado!")
                return self.incluir_arbitro()

        self.__arbitroDAO.add(novo_arbitro)
        return self.__tela_arbitros.mostra_mensagem("Novo arbitro adicionado!")
        
        

    def alterar_arbitro(self):
        if len(self.__arbitroDAO.get_all()) != 0:
            dados_arbitro_alteracao = self.__tela_arbitros.alterar_arbitro()
            cpf_alteracao = dados_arbitro_alteracao["CPF alteracao"]
            novo_arbitro = self.pesquisar_arbitros_por_cpf(cpf_alteracao)

            #verifica se o CPF atual realmente está vinculado a um arbitro na lista
            #for item in self.__arbitros:
                #if item.cpf == cpf_alteracao:
                   # novo_arbitro = item

            #verifica se o CPF novo já está sendo usado
            for arbitros_existentes in self.__arbitroDAO.get_all():
                    if dados_arbitro_alteracao["CPF"] == arbitros_existentes.cpf:
                        return self.__tela_arbitros.mostra_mensagem("O CPF informado já está cadastrado no sistema, insira um CPF válido.")
                
            if novo_arbitro in self.__arbitroDAO.get_all():
                novo_arbitro.nome = dados_arbitro_alteracao["Nome"]
                novo_arbitro.cpf = dados_arbitro_alteracao["CPF"]
                novo_arbitro.data_nascimento = dados_arbitro_alteracao["Data de nascimento"]
                novo_arbitro.endereco.estado = dados_arbitro_alteracao["Estado"]
                novo_arbitro.endereco.cidade = dados_arbitro_alteracao["Cidade"]
                novo_arbitro.endereco.bairro = dados_arbitro_alteracao["Bairro"]
                novo_arbitro.numero_partidas = dados_arbitro_alteracao["Numero de Partidas"]
                return self.__tela_arbitros.mostra_mensagem(f"Cadastro do arbitro {novo_arbitro.nome}, {novo_arbitro.cpf}, numero de partidas {novo_arbitro.numero_partidas}, endereço: {novo_arbitro.endereco.estado}, {novo_arbitro.endereco.cidade}, {novo_arbitro.endereco.bairro} alterado.")
            
            else:
                self.__tela_arbitros.mostra_mensagem("CPF informado não corresponde a nenhum arbitro.")
                return self.alterar_arbitro()
            
        else:
            return self.__tela_arbitros.mostra_mensagem("Nenhum arbitro cadastrado no sistema.")



    def excluir_arbitro(self):
        if len(self.__arbitroDAO.get_all()) == 0:
            return self.__tela_arbitros.mostra_mensagem("Nenhum arbitro cadastrado no sistema.")
        cpf = self.__tela_arbitros.selecionar_arbitro()

        arbitro_exclusao = self.pesquisar_arbitros_por_cpf(cpf)
        if arbitro_exclusao is None:
            return self.__tela_arbitros.mostra_mensagem("CPF não corresponde a um arbitro cadastrado.")
        
        self.__arbitroDAO.remove(arbitro_exclusao)
        return self.__tela_arbitros.mostra_mensagem("Arbitro foi removido")
            



    def listar_arbitros(self):
        if len(self.__arbitroDAO.get_all()) == 0:
            return self.__tela_arbitros.mostra_mensagem("\nAinda não temos arbitros cadastrados.\n")
        
        dados_arbitros = list()
        for novo_arbitro in (self.__arbitroDAO.get_all()):
            dados_arbitros_dict = dict()
            dados_arbitros_dict = {
                "Nome": novo_arbitro.nome,
                "CPF": novo_arbitro.cpf,
                "numero_partidas": novo_arbitro.numero_partidas
            }
            dados_arbitros.append(dados_arbitros_dict)

        return self.__tela_arbitros.listar_arbitros(dados_arbitros)


    def pesquisar_arbitros_por_cpf(self, cpf: str) -> Arbitro:
        for item in (self.__arbitroDAO.get_all()):
            if item.cpf == cpf:
                return item
        return None
            

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_arbitro,
            2: self.alterar_arbitro, 
            3: self.excluir_arbitro, 
            4: self.listar_arbitros, 
            0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_arbitros.mostrar_opcoes()]()
