from datetime import datetime
from tela.tela_base import TelaBase
import time



class TelaArbitros(TelaBase):
    def __init__(self):
        super(). __init__()

    def tela_opcoes(self):
        self.limpar_tela()
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
    def incluir_arbitro(self):
        self.limpar_tela()
        print("-------- Dados do Arbitro --------")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        while True:
            data_nascimento = input("Data de nascimento: ")
            try:
                data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
                break
            except ValueError:
                print("formato de data informado está incorreto, por favor, informar no formato dd/mm/aaaa")
        estado = input("Estado: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        numero_partidas = input("Número de partidas: ")

        dados_arbitro_inclusao = {"Nome": nome,
                "CPF": cpf,
                "Data de nascimento": data_nascimento,
                "Bairro": bairro,
                "Cidade": cidade,
                "Estado": estado,
                "Numero de partidas": int(numero_partidas)
                }
        return dados_arbitro_inclusao      



    def alterar_arbitro(self):
        self.limpar_tela()
        print()
        print('-------- Informe o CPF atual do arbitro para fazer a alteração --------')
        cpf = input("CPF: ")
            
        if len(cpf) != 11 or not cpf.isdigit() or not isinstance(cpf, str):
            print("cpf informado não encontrado.")
            return self.alterar_arbitro()
        else:
            cpf_alteracao = cpf
            self.limpar_tela()
            print('-------- Informe os dados para alteração de um arbitro já cadastrado --------')
            cpf = input("CPF: ")
            nome = input("Nome: ")
            data_nascimento = input("Data de nascimento: ")
            estado = input("Estado: ")
            bairro = input("Bairro: ")
            cidade = input("Cidade: ")
            numero_partidas = input("Numero de Partidas: ")  


            dados_arbitro_alteracao = {
                "CPF alteracao" : cpf_alteracao,
                "Nome" : nome,
                "CPF" : cpf,
                "Data de nascimento" : data_nascimento,
                "Bairro" : bairro,
                "Cidade" : cidade,
                "Estado" : estado,
                "Numero de Partidas" : numero_partidas
            }
            return dados_arbitro_alteracao


    
    def excluir_arbitro(self) -> str:
        self.limpar_tela()
        print('-------- Informe o CPF para exclusão --------')
        cpf = input("CPF: ")
        if isinstance(cpf, str) and len(cpf) == 11 and cpf.isnumeric():
            cpf_exclusao = cpf
            return cpf_exclusao
        else:
            print("cpf informado não encontrado.")
            return self.excluir_arbitro()
        


    def listar_arbitros(self, dados_arbitros: list):
        self.limpar_tela()
        print('-------- Listagem de Arbitros --------')
        for arbitro in dados_arbitros:
            nome = arbitro["Nome"]
            cpf = arbitro["CPF"]
            data_nascimento = arbitro["Data de Nascimento"]
            bairro = arbitro["estado"]
            cidade = arbitro["cidade"]
            estado = arbitro["bairro"]
            numero_partidas = arbitro["numero partidas"]
            print(f"Nome: {nome}")
            print(f"CPF: {cpf}")
            print(f"Data de nascimento: {data_nascimento}")
            print(f"Bairro: {bairro}")
            print(f"Cidade: {cidade}")
            print(f"Estado: {estado}")
            print(f"Número de partidas: {numero_partidas}")
            print()
        self.esperar_resposta()
    


        


