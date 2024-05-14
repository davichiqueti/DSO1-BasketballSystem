from datetime import datetime
from tela.tela_base import TelaBase
import time

class TelaArbitros(TelaBase):
    def __init__(self):
        super(). __init__()

    def tela_opcoes(self):
        
        print("--------Arbitros--------")
        print("Escolha uma opção:")
        print("1 - Incluir Arbitro")
        print("2 - Alterar Arbitro")
        print("3 - Excluir Arbitro")
        print("4 - Listar Arbitro")
        print("10 - Retornar")

        opcao = int(input("Escolha uma opcao: "))
        return opcao

#pega os dados do arbitro pela tela
    def pega_dados_arbitro(self):
        print("-------- Dados Arbitro --------")
        nome = input("Nome: ") 
        cpf = input("cpf: ")
        while True:
            data_nascimento = input("Data de nascimento: ")
            try:
                data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
                break
            except ValueError:
                print("formato de data informado está incorreto, por favor, informar no formato dd/mm/aaaa")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        numero_partidas = input("Número de partidas: ")

        return {"Nome": nome,
                "CPF": cpf,
                "Data de nascimento": data_nascimento,
                "Bairro": bairro,
                "Cidade": cidade,
                "Estado": estado,
                "Numero de partidas": int(numero_partidas)
                }

    def mostrar_mensagem(self, msg:str):
        if isinstance(msg, str):
            print(msg)
        
    def pega_cpf_arbitro(self):
        self.limpar_tela()
        print('-------- Informe os dados para fazer a alteração --------')
        cpf = input("CPF: ")
        if isinstance(cpf, str) and len(cpf) == 11 and cpf.isnumeric():
            return cpf
        else:
            self.mostrar_mensagem("cpf informado não encontrado.")
            time.sleep(3)
            return self.alterar_arbitro()
        
    
    def alterar_arbitro(self):
        self.limpar_tela()
        print('-------- Informe os dados para alteração de um arbitro já cadastrado --------')
        nome = input("Nome: ")
        if isinstance(nome, str) and len(nome) >= 4 and len(nome) <= 61 and nome.isalpha():
            nome_alteracao = nome
        else:
            self.mostrar_mensagem("nome informado não encontrado.")
            time.sleep(3)
            return self.alterar_arbitro()
        cpf = input("CPF: ")
        if isinstance(cpf, str) and len(cpf) == 11 and cpf.isnumeric():
            cpf_alteracao = cpf
        else:
            self.mostrar_mensagem("cpf informado não encontrado.")
            time.sleep(3)
            return self.alterar_arbitro()
        data_nascimento = input("Data de nascimento: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        numero_partidas = input("Numero de Partidas: ")        
        dados_arbitro_alteracao = {
            "CPF" : cpf_alteracao,
            "Nome" : nome_alteracao,
            "Data de nascimento" : data_nascimento,
            "Bairro" : bairro,
            "Cidade" : cidade,
            "Estado" : estado,
            "Numero de Partidas" : numero_partidas
        }
        return dados_arbitro_alteracao

    
    def excluir_arbitro(self):
        self.limpar_tela()
        print('-------- Informe o CPF para exclusão --------')
        cpf = input("CPF: ")
        if isinstance(cpf, str) and len(cpf) == 11 and cpf.isnumeric():
            cpf_exclusao = cpf
        else:
            self.mostrar_mensagem("cpf informado não encontrado.")
            time.sleep(3)
            return self.excluir_arbitro()
        nome = input("Nome: ")
        if isinstance(nome, str) and len(nome) > 4 and len(nome)< 61 and nome.isalpha():
            nome_exclusao = nome
        else:
            self.mostrar_mensagem("cpf informado não encontrado.")
            time.sleep(3)
            return self.excluir_arbitro()
        dados_arbitro_exclusao = {
            "CPF" : cpf_exclusao,
            "Nome" : nome_exclusao
        }
        return dados_arbitro_exclusao

    def listar_arbitros(self, cpf):
        print('-------- Consultar abritro por CPF --------')
        cpf = input("CPF: ")
        input()
        if isinstance(cpf, str):
            return {
                "CPF: ": cpf
            }
            
        else:
            self.mostrar_mensagem("cpf informado não encontrado.")

        


