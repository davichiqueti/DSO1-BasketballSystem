from tela.tela_base import TelaBase
import PySimpleGUI as sg


class TelaCursos(TelaBase):
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
            [sg.Text('-------- CURSOS ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir Curso', "RD1", key='1')],
            [sg.Radio('Alterar Curso', "RD1", key='2')],
            [sg.Radio('Excluir Curso', "RD1", key='3')],
            [sg.Radio('Listar Curso', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
        ]

        self.__window = sg.Window('Cursos').Layout(layout)


    def listar_cursos(self, dados_cursos: list[dict]):
        self.limpar_tela()
        print('--- LISTAGEM DE CURSOS ---\n')
        for curso in dados_cursos:
            codigo = curso["codigo"]
            nome = curso["nome"]
            print(f"- NOME: {nome}  CÓDIGO: {codigo}")
        print('\n')
        self.esperar_resposta()

    def incluir_curso(self) -> dict:
        self.limpar_tela()
        print('--- CADASTRO DE CURSO ---\n')
        codigo = input('Código do curso: ')
        if not codigo.isnumeric():
            self.mostra_mensagem('O código deve ser um número inteiro')
            return self.incluir_curso()
        nome = input('Nome do curso: ')
        if not (5 <= len(nome) <= 60):
            self.mostra_mensagem('O nome do curso deve ter entre 5 a 60 caracteres')
            return self.incluir_curso()
        return {
            'codigo': int(codigo),
            'nome': nome.upper().strip()
        }

    def excluir_curso(self) -> int:
        self.limpar_tela()
        print('--- EXCLUIR CURSO ---\n')
        codigo = input('Código do curso a ser exclúido: ')
        if not codigo.isnumeric():
            self.mostra_mensagem('Tentativa de exclusão por código não númerico')
            return self.excluir_curso()
        return int(codigo)

    def alterar_curso(self) -> dict:
        self.limpar_tela()
        dados_retorno = dict()
        print('--- ALTERAR CURSO ---\n')
        # Tratamento para o código do curso a ser alterado
        codigo_antigo = input('Código do curso a ser alterado: ')
        if not codigo_antigo.isnumeric():
            self.mostra_mensagem('Tentativa de alteração por código não númerico')
            return self.alterar_curso()
        dados_retorno["codigo_antigo"] = int(codigo_antigo)
        # Tratamento para o novo código (Se for inserido)
        novo_codigo = input('Novo código: ')
        if novo_codigo and not novo_codigo.isspace():
            if not novo_codigo.isnumeric():
                self.mostra_mensagem('O novo código deve ser um inteiro')
                return self.alterar_curso()
            dados_retorno["novo_codigo"] = int(novo_codigo)
        # Tratamento para o novo nome (Se for inserido)
        novo_nome = input('Novo nome: ')
        if novo_nome and not novo_nome.isspace():
            if not (5 <= len(novo_nome) <= 60):
                self.mostra_mensagem('O novo nome do curso deve ter entre 5 a 60 caracteres')
                return self.alterar_curso()
            dados_retorno["novo_nome"] = novo_nome.upper()
        return dados_retorno
