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
        if len(self.__arbitroDAO.get_all()) == 0:
            return self.__tela_arbitros.mostra_mensagem("Nenhum arbitro cadastrado no sistema.")
        else:
            self.listar_arbitros()
            dados_arbitro_alteracao = self.__tela_arbitros.alterar_arbitro()
            cpf_alteracao = dados_arbitro_alteracao["CPF"]
            arbitro_alteracao = self.pesquisar_arbitros_por_cpf(str(cpf_alteracao))

            
            for arbitros_existentes in self.__arbitroDAO.get_all():
                    if cpf_alteracao == arbitros_existentes.cpf:
                        return self.__tela_arbitros.mostra_mensagem("O CPF informado já está cadastrado no sistema, insira um CPF válido.")
                
            arbitro_alteracao.nome = dados_arbitro_alteracao["Nome"]
            arbitro_alteracao.data_nascimento = dados_arbitro_alteracao["Data de nascimento"]
            arbitro_alteracao.endereco.estado = dados_arbitro_alteracao["Estado"]
            arbitro_alteracao.endereco.cidade = dados_arbitro_alteracao["Cidade"]
            arbitro_alteracao.endereco.bairro = dados_arbitro_alteracao["Bairro"]
            arbitro_alteracao.numero_partidas = dados_arbitro_alteracao["Numero de Partidas"]
            self.__arbitroDAO.update(arbitro_alteracao)
            self.__tela_arbitros.mostra_mensagem('Arbitro alterado')
            return self.listar_arbitros()
     


    def excluir_arbitro(self):
        if len(self.__arbitroDAO.get_all()) == 0:
            return self.__tela_arbitros.mostra_mensagem("Nenhum arbitro cadastrado no sistema.")
        cpf = self.__tela_arbitros.selecionar_arbitro()

        arbitro_exclusao = self.pesquisar_arbitros_por_cpf(cpf)
        self.__arbitroDAO.remove(cpf)
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
                if isinstance(item, Arbitro):
                    return item
            

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
