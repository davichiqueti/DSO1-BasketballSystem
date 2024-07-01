import PySimpleGUI as sg


class TelaCursos():
    def __init__(self):
        self.__window = None
        self.init_opcoes()

                        #LISTAGEM

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
            [sg.Text('-------- CURSOS ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir Curso', "RD1", key='1')],
            [sg.Radio('Alterar Curso', "RD1", key='2')],
            [sg.Radio('Excluir Curso', "RD1", key='3')],
            [sg.Radio('Listar Cursos', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
        ]
        self.__window = sg.Window('Cursos').Layout(layout)


                        #METODOS

#listagem: ok!
    def listar_cursos(self, dados_cursos):
        string_todos_cursos = ""
        for dado in dados_cursos:
            codigo = str(dado.get('codigo', ''))
            nome = str(dado.get('nome', ''))

            print(f"Código: {codigo}, Nome: {nome}")

            string_todos_cursos += "Código do Curso: " + codigo + '\n'
            string_todos_cursos += "Nome do Curso: " + nome + '\n\n'

        sg.Popup('-------- LISTA DE CURSOS ----------', string_todos_cursos)


#inclusão: ok!
    def incluir_curso(self) -> dict:
        dicionario_incluir_curso = dict()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- Dados Cursos ----------', font=("Helvica", 25))],
        [sg.Text('Codigo:', size=(15, 1)), sg.InputText('', key='codigo')],
        [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema cursos').Layout(layout)

        button, values = self.open()
        codigo = int(values['codigo'])
        nome = values['nome']
        self.close()

        while True:
            if not codigo != int:
                self.mostra_mensagem('O código deve ser um número inteiro')
                return self.incluir_curso()
            
            dicionario_incluir_curso['Codigo'] = int(codigo)
            break
        
        while True:
            if not (5 <= len(nome) <= 60):
                self.mostra_mensagem('O nome do curso deve ter entre 5 a 60 caracteres')
                return self.incluir_curso()
            else:
                dicionario_incluir_curso['Nome'] = nome 
                break
        
        dicionario_incluir_curso = {
            'Codigo': codigo,
            'Nome': nome

        }
        return dicionario_incluir_curso



#exclusão: ok!
    
    def selecionar_curso(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- Selecionar Curso ----------', font=("Helvica", 25))],
        [sg.Text('-------- Por favor, digite o número que corresponde ao curso que deseja excluir ----------', font=("Helvica", 10))],
        [sg.Text('Codigo:', size=(15, 1)), sg.InputText('', key='codigo')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de livros').Layout(layout)

        button, values = self.open()
        codigo = int(values['codigo'])
        self.close()

        while True:
            if not codigo != int:
                self.mostra_mensagem('O código deve ser um número inteiro')
                return self.incluir_curso()
            else:
                break
        return codigo


#alteração: revisar
    def alterar_curso(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- Alterar Nome Curso ----------', font=("Helvica", 25))],
         [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='Nome')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona curso').Layout(layout)

        button, values = self.open()
        nome = str(values['Nome'])
        self.close()
        return nome


    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
