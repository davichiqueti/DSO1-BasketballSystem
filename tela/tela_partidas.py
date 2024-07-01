import PySimpleGUI as sg
from datetime import datetime, date


class TelaPartidas():
    def __init__(self):
        self.__window = None
        self.init_opcoes()

        #Listagem

    def mostrar_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao_escolhida = 1
        if values['2']:
            opcao_escolhida = 2
        if values['3']:
            opcao_escolhida = 3
        if values['0'] or button in (None, 'Cancelar'):
            opcao_escolhida = 0
        self.close()
        return opcao_escolhida

    # representando os componentes da tela
    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- PARTIDAS ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Listar Partidas', "RD1", key='1')],
            [sg.Radio('Incluir Partidas', "RD1", key='2')],
            [sg.Radio('Excluir Partidas', "RD1", key='3')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
        ]
        self.__window = sg.Window('Partidas').Layout(layout)



    def listar_partidas(self, dados_partidas):
        string_todas_partidas = ""
        for dado in dados_partidas:
            codigo = str(dado.get('codigo', ''))
            nome_arbitro = str(dado.get('arbitro', ''))
            nome_equipe1 = str(dado.get('equipe1', ''))
            nome_equipe2 = str(dado.get('equipe2', ''))


            print(f"Código: {codigo}, Equipes: {nome_equipe1} e {nome_equipe2}, {nome_arbitro}")

            string_todas_partidas += "Código da Partida: " + codigo + '\n'
            string_todas_partidas += "Nome do Arbitro: " + nome_arbitro + '\n'
            string_todas_partidas += "Equipes: " + nome_equipe1 + "  VS  " + nome_equipe2 + '\n\n'

        sg.Popup('-------- Lista de Partidas ----------', string_todas_partidas)

    def incluir_partida(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- Dados Partidas ----------', font=("Helvica", 25))],
        [sg.Text('Codigo:', size=(15, 1)), sg.InputText('', key='1')],
        [sg.Text('CPF do Arbitro:', size=(15, 1)), sg.InputText('', key='2')],
        [sg.Text('Código da Equipe 1:', size=(15, 1)), sg.InputText('', key='3')],
        [sg.Text('Código da Equipe 2:', size=(15, 1)), sg.InputText('', key='4')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de partidas').Layout(layout)

        button, values = self.open()

        codigo = int(values['1'])
        cpf_arbitro = values['2']
        equipe1 = int(values['3'])
        equipe2 = int(values['4'])
        self.close()
        while True:
            if len(cpf_arbitro) != 11:
                self.mostra_mensagem('O CPF deve ser um número válido.')
                return self.mostrar_opcoes()
            else:
                break

        dicionario_incluir_partida = {
                                    '1': codigo,
                                    '2': cpf_arbitro,
                                    '3': equipe1,
                                    '4': equipe2
        }
        
        return dicionario_incluir_partida
    

    def selecionar_partida(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- Dados Cursos ----------', font=("Helvica", 25))],
        [sg.Text('Codigo da Partida:', size=(15, 1)), sg.InputText('', key='codigo')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de basquete').Layout(layout)

        button, values = self.open()
        codigo = int(values['codigo'])
        self.close()

        while True:
            if not codigo != int:
                self.mostra_mensagem('O código deve ser um número inteiro')
                return self.mostrar_opcoes()
            else:
                break

        return codigo
        

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
    