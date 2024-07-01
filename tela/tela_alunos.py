import PySimpleGUI as sg
from datetime import datetime


class TelaAlunos():
    def __init__(self):
        self.__window = None
        self.init_opcoes()

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
            [sg.Text('-------- ALUNOS ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir Aluno', "RD1", key='1')],
            [sg.Radio('Alterar Aluno', "RD1", key='2')],
            [sg.Radio('Excluir Aluno', "RD1", key='3')],
            [sg.Radio('Listar Alunos', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window('Alunos').Layout(layout)

    def incluir_aluno(self) -> dict:
        dados_inclusao_aluno = {}
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS ALUNO ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='n')],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Text('Data de Nascimento:', size=(15, 1)), sg.InputText('', key='dn')],
            [sg.Text('Estado:', size=(15, 1)), sg.InputText('', key='e')],
            [sg.Text('Cidade:', size=(15, 1)), sg.InputText('', key='c')],
            [sg.Text('Bairro:', size=(15, 1)), sg.InputText('', key='b')],
            [sg.Text('Matricula:', size=(15, 1)), sg.InputText('', key='m')],
            [sg.Text('Codigo do Curso:', size=(15, 1)), sg.InputText('', key='cc')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Gestão de Campeonato de Basquete').Layout(layout)

        button, values = self.open()
        nome = values['n']
        cpf = values['cpf']
        data_nascimento = values['dn']
        estado = values['e']
        cidade = values['c']
        bairro = values['b']
        matricula = values['m']
        codigo_curso = values['cc']

        self.close()

        while True:
            if self.verificar_string_alpha(nome) and 4 <= len(nome) <= 60:
                break
            else:
                self.mostra_mensagem("nome está incorreto, por favor informe um nome válido")
                return self.incluir_aluno()

        while True:
            if len(cpf) == 11 and cpf.isnumeric():
                break
            else:
                self.mostra_mensagem("CPF está incorreto, por favor informe um CPF válido")
                return self.incluir_aluno()

        while True:
            try:
                data_nascimento = datetime.strptime(
                    data_nascimento, "%d/%m/%Y").date()
                break
            except ValueError:
                self.mostra_mensagem("Data de nascimento está incorreta, por favor informe uma data no modelo dd/mm/aaaa.")
                return self.incluir_aluno()

        while True:
            if self.verificar_string_alpha(estado) and 2 <= len(estado) <= 18:
                break
            else:
                self.mostra_mensagem("O estado informado está incorreto.")
                return self.incluir_aluno()

        while True:
            if self.verificar_string_alpha(cidade) and 3 <= len(cidade) <= 60:
                break
            else:
                self.mostra_mensagem("A cidade informada é inválida.")
                return self.incluir_aluno()

        while True:
            if any(caractere.isalpha() for caractere in bairro) and 4 <= len(bairro) <= 60:
                break
            else:
                self.mostra_mensagem("O bairro informado é inválido.")
                return self.incluir_aluno()

        while True:
            if matricula.isnumeric() and len(matricula) == 8:
                break
            else:
                self.mostra_mensagem("A matricula informada é inválida.")
                return self.incluir_aluno()

        while True:
            if codigo_curso.isnumeric():
                codigo_curso = int(codigo_curso)
                break
            else:
                self.mostra_mensagem("O código do curso informado é inválida.")
                return self.incluir_aluno()

        dados_inclusao_aluno= {
            "Nome": nome,
            "CPF": cpf,
            "Data de nascimento": data_nascimento,
            "Estado": estado,
            "Cidade": cidade,
            "Bairro": bairro,
            "Matricula": matricula,
            "codigo do curso": codigo_curso
        }

        return dados_inclusao_aluno

    def alterar_aluno(self) -> dict:
        dados_aluno_alteracao = dict()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- Dados Aluno ----------', font=("Helvica", 25))],
        [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
        [sg.Text('Data de Nascimento:', size=(15, 1)), sg.InputText('', key='data_nascimento')],
        [sg.Text('Estado:', size=(15, 1)), sg.InputText('', key='estado')],
        [sg.Text('Cidade:', size=(15, 1)), sg.InputText('', key='cidade')],
        [sg.Text('Bairro:', size=(15, 1)), sg.InputText('', key='bairro')],
        [sg.Text('Matricula:', size=(15, 1)), sg.InputText('', key='matricula')],
        [sg.Text('Código do Curso:', size=(15, 1)), sg.InputText('', key='codigo_curso')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window('Sistema de livros').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        data_nascimento = values['data_nascimento']
        estado = values['estado']
        cidade = values['cidade']
        bairro = values['bairro']
        matricula = values['matricula']
        codigo_curso = values['codigo_curso']

        self.close()

        # retornando a informação para o controlador
        dados_aluno_alteracao = {
            "Nome": nome,
            "Data de nascimento": data_nascimento,
            "Estado": estado,
            "Cidade": cidade,
            "Bairro": bairro,
            "matricula": matricula,
            "codigo_curso": codigo_curso
        }
        return dados_aluno_alteracao

    def selecionar_aluno(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- Selecionar Aluno ----------', font=("Helvica", 25))],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Exclusão de Alunos').Layout(layout)
        button, values = self.open()
        cpf = str(values['cpf'])
        self.close()
        
        while True:
            if cpf.isnumeric() and len(cpf) == 11:
                cpf_selecionado = cpf
                break
            else:
                self.mostra_mensagem("CPF inválido, por favor informe uma CPF válido.")
                self.init_opcoes()

        return cpf_selecionado



    def excluir_aluno(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- EXCLUIR ALUNO ----------', font=("Helvica", 25))],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Exclusão de Alunos').Layout(layout)
        button, values = self.open()
        cpf = values['cpf']
        self.close()
        
        while True:
            if cpf.isnumeric() and len(cpf) == 11:
                cpf_exclusao = cpf
                break
            else:
                self.mostra_mensagem("CPF inválido, por favor informe uma CPF válido.")
                self.init_opcoes()

        return cpf_exclusao

    def listar_alunos(self, dados_alunos):
        string_alunos = ""
        for novo_aluno in dados_alunos:
            nome = str(novo_aluno.get('Nome', ''))
            cpf = str(novo_aluno.get('CPF', ''))
            Data_nascimento = str(novo_aluno.get('Data de Nascimento', ''))
            matricula = str(novo_aluno.get('matricula', ''))

            print(f"Nome: {nome}, CPF: {cpf}, Data de Nascimento: {Data_nascimento}, Matricula: {matricula}")

            string_alunos += "Nome do Aluno: " + nome + '\n'
            string_alunos += "CPF: " + cpf + '\n'
            string_alunos += "Data de Nascimento: " + Data_nascimento + '\n'
            string_alunos += "Matricula: " + matricula + '\n\n'

        sg.Popup('-------- LISTA DE ALUNOS ----------', string_alunos)




    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
    

    def verificar_string_alpha(self, variavel) -> bool:
        if isinstance(variavel, str):
            variavel = variavel.split()
            for caracter in variavel:
                if not caracter.isalpha():
                    return False
            return True