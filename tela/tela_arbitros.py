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


        while True:
            nome = input("Nome: ") 
            if self.verificar_string_alpha(nome) and 4 <= len(nome) <= 60:
                break
            else:
                print("nome está incorreto, por favor informe um nome válido")
                input("Aperte enter para continuar")


        while True:
            cpf = input("CPF: ")
            if len(cpf) == 11 and cpf.isdigit():
                break
            else:    
                print("CPF está incorreto, por favor informe um CPF válido")
                input("Aperte ENTER para continuar.")


        while True:
            data_nascimento = input("Data de nascimento: ")
            try:
                data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
                break
            except ValueError:
                print("formato de data informado está incorreto, por favor, informar no formato dd/mm/aaaa")
        

        while True:
            estado = input("Estado: ")
            if self.verificar_string_alpha(estado) and 2 <= len(estado) <= 18:
                break
            else:
                print("O estado informado está incorreto.")
                input("Aperte ENTER para continuar.")


        while True:
            cidade = input("Cidade: ")
            if self.verificar_string_alpha(cidade) and 3 <= len(cidade) <= 60:
                break
            else:
                print("A cidade informada é inválida.")
                input("Aperte ENTER para continuar.")


        while True:
            bairro = input("Bairro: ")
            if self.verificar_string_alpha(bairro) and 4 <= len(bairro) <= 60:
                break
            else:
                print("O bairro informado é inválido.")
                input("Aperte ENTER para continuar.")


        while True:
            numero_partidas = input("Numero de partidas: ")
            if numero_partidas.isnumeric() and len(numero_partidas) <= 4:
                break
            else:
                print("O número de partidas informado é inválida.")
                input("Aperte ENTER para continuar.")  

        dados_arbitro_inclusao = {
                                    "Nome": nome,
                                    "CPF": cpf,
                                    "Data de nascimento": data_nascimento,
                                    "Estado": estado,
                                    "Cidade": cidade,
                                    "Bairro": bairro,
                                    "Numero de partidas": int(numero_partidas)
                                }
        return dados_arbitro_inclusao      



    def alterar_arbitro(self):


        self.limpar_tela()
        print()
        print('-------- Informe o CPF atual do arbitro para fazer a alteração --------')

        while True:
            cpf = input("CPF: ")
            if len(cpf) == 11 and cpf.isdigit():
                break
            else:    
                print("CPF está incorreto, por favor informe um CPF válido")
                input("Aperte ENTER para continuar.")
            
        cpf_alteracao = cpf
        self.limpar_tela()

        print('-------- Informe os dados para alteração de um arbitro já cadastrado --------')


        while True:
            cpf = input("CPF: ")
            if len(cpf) == 11 and cpf.isdigit():
                break
            else:    
                print("CPF está incorreto, por favor informe um CPF válido")
                input("Aperte ENTER para continuar.")


        while True:
            nome = input("Nome: ") 
            if self.verificar_string_alpha(nome) and 4 <= len(nome) <= 60:
                break
            else:
                print("nome está incorreto, por favor informe um nome válido")
                input("Aperte enter para continuar")

        while True:
            data_nascimento = input("Data de nascimento: ")
            try:
                data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
                break
            except ValueError:
                print("Data de nascimento está incorreta, por favor informe uma data no modelo dd/mm/aaaa.")
                input("Aperte ENTER para continuar.")            



        while True:
            estado = input("Estado: ")
            if self.verificar_string_alpha(estado) and 2 <= len(estado) <= 18:
                break
            else:
                print("O estado informado está incorreto.")
                input("Aperte ENTER para continuar.")

        while True:
            cidade = input("Cidade: ")
            if self.verificar_string_alpha(cidade) and 3 <= len(cidade) <= 60:
                break
            else:
                print("A cidade informada é inválida.")
                input("Aperte ENTER para continuar.")


        while True:
            bairro = input("Bairro: ")
            if self.verificar_string_alpha(bairro) and 4 <= len(bairro) <= 60:
                break
            else:
                print("O bairro informado é inválido.")
                input("Aperte ENTER para continuar.")


        while True:
            numero_partidas = input("Numero de Partidas: ")
            if numero_partidas.isnumeric() and len(numero_partidas) <= 4:
                break
            else:
                print("O número de partidas informado é inválida.")
                input("Aperte ENTER para continuar.")  


        dados_arbitro_alteracao = {
            "CPF alteracao" : cpf_alteracao,
            "Nome" : nome,
            "CPF" : cpf,
            "Data de nascimento" : data_nascimento,
            "Estado" : estado,
            "Cidade" : cidade,
            "Bairro" : bairro,
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
        for i in range(len(dados_arbitros)):
            dados_arbitros_dict = dados_arbitros[i]
            nome = dados_arbitros_dict["Nome"]
            cpf = dados_arbitros_dict["CPF"]
            data_nascimento = dados_arbitros_dict["Data de Nascimento"]
            estado = dados_arbitros_dict["estado"]
            cidade = dados_arbitros_dict["cidade"]
            bairro = dados_arbitros_dict["bairro"]
            numero_partidas = dados_arbitros_dict["numero partidas"]
            print(f"Nome: {nome}")
            print(f"CPF: {cpf}")
            print(f"Data de nascimento: {data_nascimento}")
            print(f"Estado: {estado}")
            print(f"Cidade: {cidade}")
            print(f"Bairro: {bairro}")
            print(f"Número de partidas: {numero_partidas}")
            print()
        self.esperar_resposta()
