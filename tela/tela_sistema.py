import PySimpleGUI as sg


class TelaSistema():
    def __init__(self):
        self.__window = None
        self.init_components()

#retorna opção para o controlador sistema
    def tela_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()
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
        if values['6']:
            opcao_escolhida = 6
        if values['0'] or button in (None, 'Cancelar'):
            opcao_escolhida = 0
        
        self.close()
        return opcao_escolhida

    # Definições da parte visual do sistema
    def init_components(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Bem vindo!',font=("Helvetica", 25))],
            [sg.Text('SISTEMA DE CAMPEONATOS DE BASQUETE',font=("Helvetica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvetica", 15))],
            [sg.Radio('Módulo de Aluno', "RD1", key='1')],
            [sg.Radio('Módulo de Cursos', "RD1", key='2')],
            [sg.Radio('Módulo de Árbitro', "RD1", key='3')],
            [sg.Radio('Módulo de Campeonatos', "RD1", key='4')],
            [sg.Radio('Módulo de Equipes', "RD1", key='5')],
            [sg.Radio('Módulo de Partidas', "RD1", key='6')],
            [sg.Radio('Encerrar Sistema', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Gestão de Campeonato de Basquete').Layout(layout)

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values