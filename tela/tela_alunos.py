from tela.tela_base import TelaBase
import time
from datetime import datetime


class TelaAlunos(TelaBase):
    def __init__(self):
        super(). __init__()

    def tela_opcoes(self):
        self.limpar_tela()
        print("--------Alunos-------")
        print("Ecolha uma das opções abaixo: ")
        print("1 - incluir aluno")
        print("2 - Alterar aluno")
        print("3 - Excluir aluno")
        print("4 - Listar alunos")
        print("10 - Sair")
        try: 
            opcao = int(input("Digite opção desejada: "))
            return opcao
        except:
            self.mostrar_mensagem("Tipo de dado inválido")
            self.tela_opcoes()

    def incluir_aluno(self):
        self.limpar_tela()
        print("--------Insira os dados do aluno--------")
        dados_inclusão_aluno = {}

        while True:
            nome = input("Nome: ") 
            if self.verificar_string_alpha(nome) and 4 <= len(nome) <= 60:
                break
            else:
                print("nome está incorreto, por favor informe um nome válido")
                input("Aperte enter para continuar")

        while True:
            cpf = input("cpf: ")
            if len(cpf) == 11:
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
            bairro = input("Bairro: ")
            if any(caractere.isalpha() for caractere in bairro) and 4 <= len(bairro) <= 60:
                break
            else:
                print("O bairro informado é inválido.")
                input("Aperte ENTER para continuar.")
        
        while True:
            cidade = input("Cidade: ")
            if self.verificar_string_alpha(cidade) and 3 <= len(cidade) <= 60:
                break
            else:
                print("A cidade informada é inválida.")
                input("Aperte ENTER para continuar.")
        
        while True:
            matricula = input("Matricula: ")
            if matricula.isnumeric() and len(matricula) == 8:
                break
            else:
                print("A matricula informada é inválida.")
                input("Aperte ENTER para continuar.")         

        while True:
            codigo_curso = input("Código do curso: ")
            if codigo_curso.isnumeric():
                codigo_curso = int(codigo_curso)
                break
            else:
                print("O código do curso informado é inválida.")
                input("Aperte ENTER para continuar.")  

        dados_inclusão_aluno = {
            "Nome": nome,
            "CPF": cpf,
            "Data de nascimento": data_nascimento,
            "Estado": estado,
            "Cidade": cidade,
            "Bairro": bairro,
            "Matricula": matricula,
            "codigo do curso": codigo_curso
            }

        return dados_inclusão_aluno

    def alterar_aluno(self):
        self.limpar_tela()
        print()
        print("--------Insira o CPF do aluno que deseja alterar--------")
        cpf_alteracao = input("CPF: ")
        if len(cpf_alteracao) != 11 or not cpf_alteracao.isdigit() or not isinstance(cpf_alteracao, str):
            print("cpf informado é inválido.")
            return self.alterar_aluno()
        
        self.limpar_tela()
        print('-------- Informe os dados para alteração de um aluno já cadastrado --------')
            
        cpf = input("CPF: ")
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento: ")
        estado = input("Estado: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        matricula = input("Matricula: ")  
        codigo_curso = input("Codigo do curso: ")
            
        dados_arbitro_alteracao = {
            "CPF alteracao" : cpf_alteracao,
            "Nome" : nome,
            "CPF" : cpf,
            "Data de nascimento" : data_nascimento,
            "Estado" : estado,
            "Bairro" : bairro,
            "Cidade" : cidade,
            "matricula" : matricula,
            "codigo do curso" : codigo_curso
        }
        return dados_arbitro_alteracao


    
    def excluir_aluno(self):
        self.limpar_tela()
        print("--------Exclusão do Cadastro de Aluno--------")
        dados_aluno_exclusao = {}
        matricula_aluno = input("Informe a matricula do aluno para exclusão: ")
        if matricula_aluno.isnumeric() and len(matricula_aluno) == 8:
            dados_aluno_exclusao = { "matricula" : matricula_aluno}   
            return dados_aluno_exclusao          
        else:
            print("Aluno não encontrado.")
            return self.excluir_aluno()



    def listar_aluno(self):
        self.limpar_tela()
        print("--------Lista de Alunos--------")
        self.__controlador_alunos.listar_aluno()
        self.mostrar_mensagem("Alunos Listados!")
        time.sleep(3)
