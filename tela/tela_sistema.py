from tela.tela_base import TelaBase
import PySimpleGUI as sg


class TelaSistema(TelaBase):
    def __init__(self):
        super().__init__()
        self.__window = None
        self.tela_opcoes()

    def close(self):
        self.__window.close()

#retorna opção para o controlador sistema
    def tela_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()
        if values['1']:
            opcao_escolhida = 1
        elif values['2']:
            opcao_escolhida = 2
        elif values['3']:
            opcao_escolhida = 3
        elif values['4']:
            opcao_escolhida = 4
        elif values['5']:
            opcao_escolhida = 5
        elif values['6']:
            opcao_escolhida = 6
        elif values['0'] or button in (None, 'Cancelar'):
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
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Gestão de Campeonato de Basquete').Layout(layout)
