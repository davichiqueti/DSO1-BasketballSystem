from datetime import datetime
import PySimpleGUI as sg


class TelaEquipes():
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
        if values['5']:
            opcao_escolhida = 5
        if values['0'] or button in (None, 'Cancelar'):
            opcao_escolhida = 0

        self.close()
        return opcao_escolhida
    

    # representando os componentes da tela
    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- Equipes ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir Equipes', "RD1", key='1')],
            [sg.Radio('Excluir Equipes', "RD1", key='2')],
            [sg.Radio('Listar Equipes', "RD1", key='3')],
            [sg.Radio('Incluir Aluno em Equipes', "RD1", key='4')],
            [sg.Radio('Excluir Aluno em Equipes', "RD1", key='5')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
        ]
        self.__window = sg.Window('Sistema de livros').Layout(layout)

    def incluir_equipe(self):
        dados_inclusão_equipes = {}
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS EQUIPES ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='Nome')],
            [sg.Text('Codigo:', size=(15, 1)), sg.InputText('', key='Codigo')],
            [sg.Text('Código do Curso:', size=(15, 1)), sg.InputText('', key='Codigo_curso')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Criação de Equipes').Layout(layout)

        button, values = self.open()
        nome = values['Nome']
        codigo = values['Codigo']
        codigo_curso = values['Codigo_curso']
        self.close()

        try:
            if not (2 <= len(values['Nome']) <= 60):
                self.mostra_mensagem('O nome da equipe deve ter entre 2 a 60 caracteres')
                return self.incluir_equipe()
        except Exception:
            sg.popup_error('O nome da equipe deve ter entre 2 a 60 caracteres')
        
        try:
            if not (2 <= len(values['Nome']) <= 60):
                self.mostra_mensagem('O código deve ser um número inteiro')
                return self.incluir_equipe()
        except Exception:
            sg.popup_error('O código deve ser um número inteiro')
        
        try:
            if not values['Codigo_curso'].isnumeric():
                self.mostra_mensagem('O código do curso deve ser um número inteiro')
                return self.incluir_equipe()
        except Exception:
            sg.popup_error('O código do curso deve ser um número inteiro')
        
        dados_inclusão_equipes = {
            'nome': nome.upper(),
            'codigo': int(codigo),
            'codigo_curso': int(codigo_curso),
    }
        return dados_inclusão_equipes




    def selecionar_equipe(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR EQUIPE ----------', font=("Helvica", 25))],
            [sg.Text('Digite o código da equipe que deseja selecionar:', size=(50, 1))],
            [sg.Text('Código:', size=(15, 1)), sg.InputText('', key='Codigo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
        ]
        self.__window = sg.Window('Seleção de Equipe').Layout(layout)

        button, values = self.open()
        codigo = int(values['Codigo'])
        self.close()

        return int(codigo)

    def listar_equipes(self, dados_equipes):
        string_todos_cursos = ""


        for dado in dados_equipes:
            codigo = str(dado.get('codigo', ''))
            nome = str(dado.get('nome', ''))
            nome_curso = str(dado.get('nome_curso', ''))
            lista_alunos = dado.get('alunos', [])
            
    
            print(f"Código: {codigo}, Nome: {nome}, Curso: {nome_curso},")
    
    
            string_todos_cursos += "Código: " + codigo + '\n'
            string_todos_cursos += "Nome: " + nome + '\n'
            string_todos_cursos += "Nome do Curso: " + nome_curso + '\n'
            if len(lista_alunos) == 0:
                string_todos_cursos += "Alunos: sem alunos cadastrados." + '\n\n'
            else:
                string_todos_cursos += "Alunos: " + '\n'
                for aluno in lista_alunos:
                    string_todos_cursos += "Nome: " + aluno + '\n'
                string_todos_cursos += '\n'
    
        sg.Popup('-------- LISTA DE CURSOS ----------', string_todos_cursos)


    def inclui_aluno_equipe(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- INCLUSÃO DE ALUNO EM EQUIPE ----------', font=("Helvica", 25))],
            [sg.Text('Digite o código da equipe:', size=(50, 1))],
            [sg.Text('Código:', size=(15, 1)), sg.InputText('', key='Codigo')],
            [sg.Text('Digite o CPF do aluno:', size=(50, 1))],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf_aluno')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
        ]
        self.__window = sg.Window('Inclusão de Aluno em Equipe').Layout(layout)

        button, values = self.open()
        codigo = values['Codigo']
        cpf_aluno = values['cpf_aluno']
        self.close()

        lista_inclusao = (int(codigo), str(cpf_aluno))

        return lista_inclusao
    



    def exclui_aluno_equipe(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- EXCLUSÃO DE ALUNO EM EQUIPE ----------', font=("Helvica", 25))],
            [sg.Text('Digite o código da equipe:', size=(50, 1))],
            [sg.Text('Código:', size=(15, 1)), sg.InputText('', key='Codigo')],
            [sg.Text('Digite o CPF do aluno:', size=(50, 1))],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf_aluno')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
        ]
        self.__window = sg.Window('Inclusão de Aluno em Equipe').Layout(layout)

        button, values = self.open()
        codigo = values['Codigo']
        cpf_aluno = values['cpf_aluno']
        self.close()

        lista_exclusao = (int(codigo), str(cpf_aluno))

        return lista_exclusao

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values