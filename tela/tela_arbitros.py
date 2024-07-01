from datetime import datetime
import PySimpleGUI as sg


class TelaArbitros():
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def mostrar_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            retorno = 1
        if values['2']:
            retorno = 2
        if values['3']:
            retorno = 3
        if values['4']:
            retorno = 4
        if values['0'] or button in (None, 'Cancelar'):
            retorno = 0
        self.close()
        return retorno

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- Arbitros ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir Arbitro', "RD1", key='1')],
            [sg.Radio('Alterar Arbitro', "RD1",  key='2')],
            [sg.Radio('Excluir Arbitro', "RD1", key='3')],
            [sg.Radio('Listar Arbitros', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Arbitros').Layout(layout)


# pega os dados do arbitro pela tela

    def incluir_arbitro(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS ARBITRO ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='Nome')],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='CPF')],
            [sg.Text('Data de Nascimento:', size=(15, 1)), sg.InputText('', key='Data de Nascimento')],
            [sg.Text('Estado:', size=(15, 1)), sg.InputText('', key='Estado')],
            [sg.Text('Cidade:', size=(15, 1)), sg.InputText('', key='Cidade')],
            [sg.Text('Bairro:', size=(15, 1)), sg.InputText('', key='Bairro')],
            [sg.Text('Numero de Partidas:', size=(15, 1)), sg.InputText('', key='Numero de Partidas')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Criação de Arbitro').Layout(layout)

        button, values = self.open()
        nome = values['Nome']
        cpf = values['CPF']
        data_nascimento = values['Data de Nascimento']
        estado = values['Estado']
        cidade = values['Cidade']
        bairro = values['Bairro']
        numero_partidas = values['Numero de Partidas']
        self.close()

        try:
            if len(nome) <= 60:
                pass
        except ValueError:
            self.mostra_mensagem("nome está incorreto, por favor informe um nome válido")

        while True:
            if len(str(cpf)) == 11 and str(cpf).isdigit():
                break
            else:
                self.mostra_mensagem("CPF está incorreto, por favor informe um CPF válido")

        while True:
            try:
                data_nascimento = datetime.strptime(
                    data_nascimento, "%d/%m/%Y").date()
                break
            except ValueError:
                self.mostra_mensagem("formato de data informado está incorreto, por favor, informar no formato dd/mm/aaaa")

        while True:
            if  len(estado) <= 18:
                break
            else:
                self.mostra_mensagem("O estado informado está incorreto.")


        while True:
            if len(cidade) <= 60:
                break
            else:
                self.mostra_mensagem("A cidade informada é inválida.")

        while True:
            if len(bairro) <= 60:
                break
            else:
                self.mostra_mensagem("O bairro informado é inválido.")

        while True:
            if numero_partidas.isnumeric() and len(numero_partidas) <= 4:
                break
            else:
                self.mostra_mensagem("O número de partidas informado é inválida.")
            

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
        cpf = self.selecionar_arbitro()
        while True:
            if len(str(cpf)) == 11 and str(cpf).isdigit():
                break
            else:
                self.mostra_mensagem("CPF está incorreto, por favor informe um CPF válido")
                return self.mostrar_opcoes()

        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- Alterar Arbitro ----------', font=("Helvica", 25))],
        [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='Nome')],
        [sg.Text('Data de Nascimento:', size=(15, 1)), sg.InputText('', key='data_nascimento')],
        [sg.Text('Estado:', size=(15, 1)), sg.InputText('', key='estado')],
        [sg.Text('Cidade:', size=(15, 1)), sg.InputText('', key='cidade')],
        [sg.Text('Bairro:', size=(15, 1)), sg.InputText('', key='bairro')],
        [sg.Text('Número de Partidas:', size=(15, 1)), sg.InputText('', key='numero_partidas')],


        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona curso').Layout(layout)

        button, values = self.open()
        nome = str(values['Nome'])
        data_nascimento = str(values['data_nascimento'])
        estado = str(values['estado'])
        cidade = str(values['cidade'])
        bairro = str(values['bairro'])
        numero_partidas = str(values['numero_partidas'])
        self.close()

        while True:
            if self.verificar_string_alpha(nome) and 4 <= len(nome) <= 60:
                break
            else:
                return self.mostra_mensagem("Nome inválido, por favor informe um nome válido")
                

        while True:
            try:
                data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
                break
            except ValueError:
                self.mostra_mensagem("formato de data informado está incorreto, por favor, informar no formato dd/mm/aaaa")
                break
        


        while True:
            if self.verificar_string_alpha(estado) and 2 <= len(estado) <= 18:
                break
            else:
                return self.mostra_mensagem("Estado inválido, por favor informe um estado válido")


        while True:
            if self.verificar_string_alpha(cidade) and 3 <= len(cidade) <= 60:
                break
            else:
                return self.mostra_mensagem("Cidade inválida, por favor informe uma cidade válida")


        while True:
            if self.verificar_string_alpha(bairro) and 4 <= len(bairro) <= 60:
                break
            else:
                return self.mostra_mensagem("Bairro inválido, por favor informe um bairro válido")


        while True:
            if numero_partidas.isnumeric() and len(numero_partidas) <= 4:
                break
            else:
                return self.mostra_mensagem("Número de partidas inválido, por favor informe um número de partidas válido")
                

        dados_arbitro_alteracao = {
            "Nome": nome,
            "CPF": cpf,
            "Data de nascimento": data_nascimento,
            "Estado": estado,
            "Cidade": cidade,
            "Bairro": bairro,
            "Numero de Partidas": numero_partidas
        }
        return dados_arbitro_alteracao


    def selecionar_arbitro(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- Selecionar Arbitros ----------', font=("Helvica", 25))],
        [sg.Text('Digite o CPF do arbitro que deseja selecionar:', font=("Helvica", 15))],
        [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]]
        self.__window = sg.Window('Seleciona arbitros').Layout(layout)

        button, values = self.open()
        cpf = str(values['cpf'])
        self.close()
        return cpf
    

    def listar_arbitros(self, dados_arbitros):
        string_todos_arbitros = ""
        for dado in dados_arbitros:
            string_todos_arbitros = string_todos_arbitros + "Nome do arbitro: " + str(dado["Nome"]) + '\n'
            string_todos_arbitros = string_todos_arbitros + "CPF do arbitro: " + str(dado["CPF"]) + '\n'
            string_todos_arbitros = string_todos_arbitros + "Número de partidas: " + str(dado["numero_partidas"]) + '\n\n'

        sg.Popup('-------- Lista de arbitros ----------', string_todos_arbitros)

    



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