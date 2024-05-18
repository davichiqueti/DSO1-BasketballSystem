from tela.tela_base import TelaBase


class TelaEquipes(TelaBase):
    def __init__(self):
        super().__init__()

    def mostrar_opcoes(self, opcoes: dict) -> str:
        self.limpar_tela()
        print('--- MÓDULO DE EQUIPES ---')
        print('\nOpções disponíveis:')
        for codigo, acao in opcoes.items():
            print(f'{codigo} - {acao}')
        opcao_escolhida = input('\nSelecione uma opção: ')
        return opcao_escolhida

    def listar_equipes(self, dados_equipes: list[dict]):
        self.limpar_tela()
        print('--- LISTAGEM DE EQUIPES ---\n')
        for equipe in dados_equipes:
            nome = equipe["nome"]
            codigo = equipe["codigo"]
            nome_curso = equipe["nome_curso"]
            print(f"- EQUIPE: {nome}  CÓDIGO: {codigo} CURSO: {nome_curso}")
        print('\n')
        self.esperar_resposta()

    def incluir_equipe(self, minimo_de_membros: int) -> dict:
        self.limpar_tela()
        print('--- CADASTRO DE EQUIPE ---\n')
        nome = input('Nome da equipe: ')
        if not (2 <= len(nome) <= 60):
            self.mostrar_mensagem('O nome da equipe deve ter entre 2 a 60 caracteres')
            return self.incluir_equipe()
        codigo = input('Código da equipe: ').strip()
        if not codigo.isnumeric():
            self.mostrar_mensagem('O código deve ser um número inteiro')
            return self.incluir_equipe()
        codigo_curso = input('Código do curso: ').strip()
        if not codigo.isnumeric():
            self.mostrar_mensagem('Só existem cadastros de curso com códigos númericos')
            return self.incluir_equipe()
        # Tratamento para os alunos das equipes
        print(f'ALUNOS DA EQUIPE (Ao menos {minimo_de_membros})')
        codigos_alunos = list()
        while True:
            codigo_aluno = input(f'Código do {len(codigos_alunos) + 1}° aluno: ').strip()
            if not codigo_aluno.isnumeric():
                self.mostrar_mensagem('Só existem cadastros de alunos com códigos númericos')
            codigo_aluno = int(codigo_aluno)
            if codigo_aluno in codigos_alunos:
                self.mostrar_mensagem('Este código de aluno já foi inserido na lista')
            codigos_alunos.append(codigo_aluno)
            if len(codigos_alunos) == 5:
                self.mostrar_mensagem('Mínimo de membros alcançado')
            if len(codigos_alunos) >= minimo_de_membros:
                cadastro_adicional = self.confirmar_acao('Cadastrar um membro adicional?')
                if not cadastro_adicional:
                    break
        return {
            'nome': nome.upper(),
            'codigo': int(codigo),
            'codigo_curso': int(codigo_curso),
            'codigos_alunos': codigos_alunos
        }

    def excluir_equipe(self) -> int:
        self.limpar_tela()
        print('--- EXCLUIR EQUIPE ---\n')
        codigo = input('Código da equipe a ser exclúida: ')
        if not codigo.isnumeric():
            self.mostrar_mensagem('Tentativa de exclusão por código não númerico')
            return self.excluir_equipe()
        return int(codigo)

    def alterar_equipe(self) -> dict:
        self.limpar_tela()
        dados_retorno = dict()
        print('--- ALTERAR EQUIPE ---\n')
        # Tratamento para o código a ser alterado
        codigo_antigo = input('Código da equipe a ser alterada: ')
        if not codigo_antigo.isnumeric():
            self.mostrar_mensagem('Tentativa de alteração por código não númerico')
            return self.alterar_equipe()
        dados_retorno["codigo_antigo"] = int(codigo_antigo)
        # Tratamento para o novo código (Se for inserido)
        novo_codigo = input('Novo código: ')
        if novo_codigo and not novo_codigo.isspace():
            if not novo_codigo.isnumeric():
                self.mostrar_mensagem('O novo código deve ser um inteiro')
                return self.alterar_equipe()
            dados_retorno["novo_codigo"] = int(novo_codigo)
        # Tratamento para o código do novo curso da equipe(Se for inserido)
        codigo_novo_curso = input('Código do novo curso: ')
        if codigo_novo_curso and not codigo_novo_curso.isspace():
            if not codigo_novo_curso.isnumeric():
                self.mostrar_mensagem('O código do novo curso deve ser um inteiro')
                return self.alterar_equipe()
            dados_retorno["codigo_novo_curso"] = int(codigo_novo_curso)
        # Tratamento para o novo nome (Se for inserido)
        novo_nome = input('Novo nome da equipe: ')
        if novo_nome and not novo_nome.isspace():
            if not (5 <= len(novo_nome) <= 60):
                self.mostrar_mensagem('O novo nome da equipe deve ter entre 5 a 60 caracteres')
                return self.alterar_equipe()
            dados_retorno["novo_nome"] = novo_nome.upper()
        return dados_retorno
