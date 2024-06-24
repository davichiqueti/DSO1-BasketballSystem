from tela.tela_base import TelaBase
from datetime import datetime
import PySimpleGUI as sg

class TelaAlunos(TelaBase):
    def __init__(self):
        super().__init__()
        self.__window = None
        self.init_opcoes()

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values


    def mostrar_opcoes(self):
        self.init_opcoes()
        button, values = self.open()

        if values['1']:
            opcao_escolhida = 1
        if values['2']:
            opcao_escolhida = 2
        if values['3']:
            opcao_escolhida = 3
        if values['4']:
            opcao_escolhida = 4
        if values['0'] or button in (None, 'Cancelar'):
            opcao_escolhida = 0

        self.close()
        return opcao_escolhida

    # representando os componentes da tela
    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- Alunos ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir Aluno', "RD1", key='1')],
            [sg.Radio('Alterar Aluno', "RD1", key='2')],
            [sg.Radio('Excluir Aluno', "RD1", key='3')],
            [sg.Radio('Listar Alunos', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
        ]

        self.__window = sg.Window('Alunos').Layout(layout)

    def incluir_aluno(self):
        dados_inclusão_aluno = {}
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS ALUNO ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='Nome')],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='CPF')],
            [sg.Text('Data de Nascimento:', size=(15, 1)), sg.InputText('', key='Data de Nascimento')],
            [sg.Text('Estado:', size=(15, 1)), sg.InputText('', key='Estado')],
            [sg.Text('Cidade:', size=(15, 1)), sg.InputText('', key='Cidade')],
            [sg.Text('Bairro:', size=(15, 1)), sg.InputText('', key='Bairro')],
            [sg.Text('Matricula:', size=(15, 1)), sg.InputText('', key='Matricula')],
            [sg.Text('Codigo do Curso:', size=(15, 1)), sg.InputText('', key='Codigo do Curso')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Criação de Alunos').Layout(layout)

        button, values = self.open()
        nome = values['Nome']
        cpf = values['CPF']
        data_nascimento = values['Data de Nascimento']
        estado = values['Estado']
        cidade = values['Cidade']
        bairro = values['Bairro']
        matricula = values['Matricula']
        codigo_curso = values['Codigo do Curso']
        self.close()

        while True:
            if self.verificar_string_alpha(nome) and 4 <= len(nome) <= 60:
                break
            else:
                print("nome está incorreto, por favor informe um nome válido")
                input("Aperte enter para continuar")

        while True:
            if len(cpf) == 11 and cpf.isnumeric():
                break
            else:
                print("CPF está incorreto, por favor informe um CPF válido")
                input("Aperte ENTER para continuar.")

        while True:
            try:
                data_nascimento = datetime.strptime(
                    data_nascimento, "%d/%m/%Y").date()
                break
            except ValueError:
                print(
                    "Data de nascimento está incorreta, por favor informe uma data no modelo dd/mm/aaaa.")
                input("Aperte ENTER para continuar.")

        while True:
            if self.verificar_string_alpha(estado) and 2 <= len(estado) <= 18:
                break
            else:
                print("O estado informado está incorreto.")
                input("Aperte ENTER para continuar.")

        while True:
            if self.verificar_string_alpha(cidade) and 3 <= len(cidade) <= 60:
                break
            else:
                print("A cidade informada é inválida.")
                input("Aperte ENTER para continuar.")

        while True:
            if any(caractere.isalpha() for caractere in bairro) and 4 <= len(bairro) <= 60:
                break
            else:
                print("O bairro informado é inválido.")
                input("Aperte ENTER para continuar.")

        while True:
            if matricula.isnumeric() and len(matricula) == 8:
                break
            else:
                print("A matricula informada é inválida.")
                input("Aperte ENTER para continuar.")

        while True:
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
        print("-------- Insira o CPF do aluno que deseja alterar --------")

        while True:
            cpf_alteracao = input("cpf: ")
            if len(cpf_alteracao) == 11 and cpf_alteracao.isdigit():
                break
            else:
                print("CPF está incorreto, por favor informe um CPF válido")
                input("Aperte ENTER para continuar.")

        self.limpar_tela()
        print('-------- Informe os dados para alteração --------')

        while True:
            cpf = input("cpf: ")
            if len(cpf) == 11 and cpf.isnumeric():
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
                data_nascimento = datetime.strptime(
                    data_nascimento, "%d/%m/%Y").date()
                break
            except ValueError:
                print(
                    "Data de nascimento está incorreta, por favor informe uma data no modelo dd/mm/aaaa.")
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

        # retornando a informação para o controlador
        dados_aluno_alteracao = {
            "CPF alteracao": cpf_alteracao,
            "Nome": nome,
            "CPF": cpf,
            "Data de nascimento": data_nascimento,
            "Estado": estado,
            "Cidade": cidade,
            "Bairro": bairro,
            "matricula": matricula,
            "codigo_curso": codigo_curso
        }
        return dados_aluno_alteracao

    def excluir_aluno(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- EXCLUIR ALUNO ----------', font=("Helvica", 25))],
            [sg.Text('Matricula:', size=(15, 1)), sg.InputText('', key='Matricula')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Exclusão de Alunos').Layout(layout)
        button, values = self.open()
        matricula = values['Matricula']
        self.close()
        
        while True:
            if matricula.isnumeric() and len(matricula) == 8:
                matricula_exclusao = matricula
                break
            else:
                self.mostra_mensagem("Matricula inválida, por favor informe uma matricula válida.")
                self.excluir_aluno()

        return matricula_exclusao

    def listar_alunos(self, dados_alunos: list):
        string_alunos = ""

        for novo_aluno in dados_alunos:
            for dado in novo_aluno:
                nome = novo_aluno["Nome"]
                cpf = novo_aluno["CPF"]
                data_nascimento = novo_aluno["Data de Nascimento"]
                estado = novo_aluno["estado"]
                cidade = novo_aluno["cidade"]
                bairro = novo_aluno["bairro"]
                matricula = novo_aluno["matricula"]
                curso = novo_aluno["curso"]

                string_alunos = string_alunos + "Nome do Aluno: " + nome + '\n'
                string_alunos = string_alunos + "CPF: " + cpf + '\n'
                string_alunos = string_alunos + "Data de Nascimento: " + data_nascimento + '\n'
                string_alunos = string_alunos + "Estado: " + estado + '\n'
                string_alunos = string_alunos + "Cidade: " + cidade + '\n'
                string_alunos = string_alunos + "Bairro: " + bairro + '\n'
                string_alunos = string_alunos + "Matricula: " + matricula + '\n'
                string_alunos = string_alunos + "Curso: " + curso + '\n'
            
            sg.Popup('-------- LISTA DE ALUNOS ----------', string_alunos)
