from entidade.arbitro import Arbitro
from datetime import date
from tela.tela_arbitros import TelaArbitros
from controle.controlador_sistema import *
import time


class ControladorArbitros:
    def __init__(self):
        self.__lista_de_arbitros = []
        self.__tela_arbitros = TelaArbitros()
        self.__controlador_sistema = None

    @property
    def lista_de_arbitros(self):
        return self.__lista_de_arbitros
    
    @lista_de_arbitros.setter
    def lista_de_arbitros(self, lista_de_arbitros):
        self.__lista_de_arbitros = lista_de_arbitros

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
                self.tela_cursos.mostrar_mensagem('Opção inválida.')


    def incluir_arbitro(self):
        info_arbitro = self.__tela_arbitros.pega_dados_arbitro()
        novo_arbitro = Arbitro(info_arbitro['Nome'], info_arbitro['CPF'],
                               info_arbitro["Data de nascimento"], info_arbitro['Bairro'],
                               info_arbitro['Cidade'], info_arbitro['Estado'], info_arbitro["Numero de partidas"]
                               )
        for arbitro_cadastrado in self.__lista_de_arbitros:
            if arbitro_cadastrado.cpf == novo_arbitro.cpf:
                self.__tela_arbitros.mostrar_mensagem("Arbitro já cadastrado!")
                return self.incluir_arbitro()

        self.__lista_de_arbitros.append(novo_arbitro)
        self.__tela_arbitros.mostrar_mensagem("Novo arbitro adicionado!")
        return self.mostrar_opcoes()
        

    def alterar_arbitro(self):
        if len(self.__lista_de_arbitros) != 0:
            arbitro = self.pesquisar_arbitros_por_cpf()
            
            dados_arbitro_alteracao = self.tela_arbitros.alterar_arbitro()
            arbitro.nome = dados_arbitro_alteracao["Nome"]
            arbitro.data_nascimento = dados_arbitro_alteracao["Data de nascimento"]
            arbitro.bairro = dados_arbitro_alteracao["Bairro"]
            arbitro.cidade = dados_arbitro_alteracao["Cidade"]
            arbitro.estado = dados_arbitro_alteracao["Estado"]
            arbitro.numero_partidas = dados_arbitro_alteracao["Numero de Partidas"]
            self.tela_arbitros.mostrar_mensagem("Cadastro do arbitro alterado.")
            time.sleep(3)
        else:
            self.tela_arbitros.mostrar_mensagem("Arbitro não encontrado no sistema.")



    def excluir_arbitro(self):
        dados_arbitro = self.__tela_arbitros.excluir_arbitro()
        #arbitro_exclusao = Arbitro(info_arbitro['Nome'],  info_arbitro['CPF'],
         #                           info_arbitro["Data de nascimento"], info_arbitro['Bairro'],
          #                          info_arbitro['Cidade'], info_arbitro['Estado'],  info_arbitro["Numero de partidas"]
           #                         )
        if len(self.__lista_de_arbitros) != 0:
            for arbitro_cadastrado in self.__lista_de_arbitros:
                if arbitro_cadastrado.cpf == dados_arbitro["CPF"] and arbitro_cadastrado.nome == dados_arbitro["Nome"]:
                    self.__lista_de_arbitros.remove(arbitro_cadastrado)
                    return self.tela_arbitros.mostrar_mensagem("Arbitro removido")
                else:
                     return self.tela_arbitros.mostrar_mensagem("Dados incorretos.")
        else:            
            return self.tela_arbitros.mostrar_mensagem("Arbitro não está cadastrado.")

    def listar_arbitros(self):
        if len(self.__lista_de_arbitros) == 0:
            self.tela_arbitros.mostrar_mensagem("\nLista Vazia\n")
            time.sleep(3)

        for arbitros in self.__lista_de_arbitros:
            self.tela_arbitros.mostrar_mensagem(f'arbitro: {arbitros.nome},  {arbitros.cpf},  {arbitros.numero_partidas}')
            time.sleep(1)

    def pesquisar_arbitros_por_cpf(self):
        cpf = self.tela_arbitros.pega_cpf_arbitro()
        for item in self.__lista_de_arbitros:
            if item.cpf == cpf:
                return item

    def selecionar_arbitros_por_cpf(self, cpf: str):
        for i in range(len(self.__lista_de_arbitros)):
            arbitro = self.__lista_de_arbitros[i]
            if arbitro.codigo == cpf:
                return arbitro
