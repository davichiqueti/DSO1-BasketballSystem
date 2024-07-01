from datetime import datetime
import PySimpleGUI as sg

class TelaCampeonatos():
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
        if values['0'] or button in (None, 'Cancelar'):
            opcao_escolhida = 0

        self.close()
        return opcao_escolhida

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- Campeonatos de Basquete----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Criar um campeonato', "RD1", key='1')],
            [sg.Radio('Listar campeonatos', "RD1", key='2')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Campeonatos').Layout(layout)

    def criar_campeonato(self):
        dict_incluir_campeonato = {}
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS CAMPEONATO ----------', font=("Helvica", 25))],
            [sg.Text('Insira um código para esse campeonato:', size=(30, 1)), sg.InputText('', key='codigo_campeonato')],
            [sg.Text('Insira um código de partida existente:', size=(30, 1)), sg.InputText('', key='codigo_partida')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Criação de campeonato').Layout(layout)        

        button, values = self.open()
        codigo_campeonato = values['codigo_campeonato']
        codigo_partida = values['codigo_partida']
        self.close()

        while True:
            if codigo_campeonato.isnumeric():
                codigo_campeonato = int(codigo_campeonato)
                break
            else:    
                self.mostra_mensagem("Código de campeonato inválido, por favor informe um código válido")
                self.criar_campeonato()
        while True:
            if codigo_partida.isnumeric():
                codigo_partida = int(codigo_partida)
                break
            else:    
                self.mostra_mensagem("Código de partida inválido, por favor informe um código válido")
                self.criar_campeonato()


        dict_incluir_campeonato = {
            "codigo_campeonato" : codigo_campeonato,
            "codigo_partida" : codigo_partida,
            }
        return dict_incluir_campeonato




    def listar_campeonato(self, dados_campeonatos):
        string_todos_campeonatos = ""


        for dado in dados_campeonatos:
            codigo = str(dado.get('codigo', ''))
            nome_arbitro = str(dado.get('arbitro', ''))
            equipe1_nome = str(dado.get('equipe1', ''))
            pontuacao_equipe1 = dado.get('pontuacao_equipe1', '')
            equipe2_nome = str(dado.get('equipe2', ''))
            pontuacao_equipe2 = dado.get('pontuacao_equipe2', '')
            vencedor = dado.get('vencedor', '')

            
            print(f"Código: {codigo}, Nome arbitro: {nome_arbitro}, Equipe1: {equipe1_nome},")
            print(f"pontuacao equipe 1: {pontuacao_equipe1}, equipe2: {equipe2_nome}, pontuacao equipe 2: {pontuacao_equipe2},")
            print(f"Vencedor: {vencedor}")

    
            string_todos_campeonatos += "Código: " + codigo + '\n'
            string_todos_campeonatos += "CPF do arbitro: " + nome_arbitro + '\n'
            string_todos_campeonatos += "Nome da primeira equipe: " + equipe1_nome + '\n'
            string_todos_campeonatos += "Pontuacao da primeira equipe: " + str(pontuacao_equipe2) +  '\n'
            string_todos_campeonatos += "Nome da segunda equipe: " + equipe2_nome + '\n'
            string_todos_campeonatos += "Pontuacao da segunda equipe: " + str(pontuacao_equipe1) +  '\n\n'
            string_todos_campeonatos += "Vencedor dessa rodada: " + str(vencedor) + '\n\n\n'
    
        sg.Popup('-------- LISTA DE CAMPEONATOS ----------', string_todos_campeonatos)

        

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
