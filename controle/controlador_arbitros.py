from entidade.arbitro import Arbitro
from datetime import date
from tela.tela_arbitros import TelaArbitros
from controle.controlador_sistema import *
import time


class ControladorArbitros:
    def __init__(self):
        self.__arbitros = []
        self.__tela_arbitros = TelaArbitros()
        self.__controlador_sistema = None


    @property
    def arbitros(self):
        return self.__arbitros


    @arbitros.setter
    def arbitros(self, arbitros):
        self.__arbitros = arbitros


    @property
    def tela_arbitros(self) -> TelaArbitros:
        return self.__tela_arbitros


    @property
    def controlador_sistema(self):
        return self.__controlador_sistema


    @controlador_sistema.setter
    def controlador_sistema(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema


    def mostrar_opcoes(self):
        retorno = 0
        while True:
            retorno = self.tela_arbitros.tela_opcoes()
            if retorno == 1:
                self.incluir_arbitro()
            elif retorno == 2:
                self.alterar_arbitro()
            elif retorno == 3:
                self.excluir_arbitro()
            elif retorno == 4:
                self.listar_arbitros()
            elif retorno == 10:
                break
            else:
                self.tela_arbitros.mostrar_mensagem('Opção inválida.')


    def incluir_arbitro(self):
        info_arbitro = self.__tela_arbitros.incluir_arbitro()
        novo_arbitro = Arbitro(info_arbitro['Nome'], info_arbitro['CPF'],
                               info_arbitro["Data de nascimento"], info_arbitro['Bairro'],
                               info_arbitro['Cidade'], info_arbitro['Estado'], info_arbitro["Numero de partidas"]
                               )
        for arbitro_cadastrado in self.__arbitros:
            if arbitro_cadastrado.cpf == novo_arbitro.cpf:
                self.__tela_arbitros.mostrar_mensagem("Arbitro já cadastrado!")
                return self.incluir_arbitro()

        self.__arbitros.append(novo_arbitro)
        self.__tela_arbitros.mostrar_mensagem("Novo arbitro adicionado!")
        return self.mostrar_opcoes()
        

    def alterar_arbitro(self):
        if len(self.__arbitros) != 0:
            dados_arbitro_alteracao = self.__tela_arbitros.alterar_arbitro()
            cpf_alteracao = dados_arbitro_alteracao["CPF alteracao"]
            arbitro = self.pesquisar_arbitros_por_cpf(cpf_alteracao)
            for abitros_existentes in self.__arbitros:
                    if dados_arbitro_alteracao["CPF"] == abitros_existentes.cpf:
                        return self.tela_arbitros.mostrar_mensagem("O CPF informado já está cadastrado no sistema, insira um CPF válido.")
                
            if arbitro in self.__arbitros:
                arbitro.nome = dados_arbitro_alteracao["Nome"]
                arbitro.cpf = dados_arbitro_alteracao["CPF"]
                arbitro.data_nascimento = dados_arbitro_alteracao["Data de nascimento"]
                arbitro.bairro = dados_arbitro_alteracao["Bairro"]
                arbitro.cidade = dados_arbitro_alteracao["Cidade"]
                arbitro.estado = dados_arbitro_alteracao["Estado"]
                arbitro.numero_partidas = dados_arbitro_alteracao["Numero de Partidas"]
                self.limpar_tela()
                return self.tela_arbitros.mostrar_mensagem("Cadastro do arbitro alterado.")
            else:
                self.limpar_tela()
                self.tela_arbitros.mostrar_mensagem("CPF informado não corresponde a nenhum arbitro.")
                return self.tela_arbitros.alterar_arbitro()
        else:
            self.tela_arbitros.mostrar_mensagem("Arbitro não encontrado no sistema.")
            return self.tela_arbitros.alterar_arbitro()

    def excluir_arbitro(self):
        if len(self.__arbitros) != 0:
            info_arbitro = self.__tela_arbitros.excluir_arbitro()
            arbitro_exclusao = self.pesquisar_arbitros_por_cpf(info_arbitro)

            if self.__tela_arbitros.confirmar_acao("Tem certeza que deseja excluir o arbitro?"):
                self.__arbitros.remove(arbitro_exclusao)
                return self.__tela_arbitros.mostrar_mensagem("Arbitro foi removido")
            else:
                return
        else:
            return self.tela_arbitros.mostrar_mensagem("Arbitro não está cadastrado.")



    def listar_arbitros(self):
        if len(self.__arbitros) == 0:
            return self.tela_arbitros.mostrar_mensagem("\nAinda não temos arbitros cadastrados.\n")
        dados_arbitros = list()
        for arbitro in self.arbitros:
            dados_arbitros_dict = {
                "Nome": arbitro.nome,
                "CPF": arbitro.cpf,
                "Data de Nascimento": arbitro.data_nascimento,
                "estado": arbitro.endereco.estado,
                "cidade": arbitro.endereco.cidade,
                "bairro": arbitro.endereco.bairro,
                "numero partidas": arbitro.numero_partidas
            }
            dados_arbitros.append(dados_arbitros_dict)

        return self.tela_arbitros.listar_arbitros(dados_arbitros)


    def pesquisar_arbitros_por_cpf(self, cpf: str) -> int:
        for item in self.__arbitros:
            if item.cpf == cpf:
                return item
