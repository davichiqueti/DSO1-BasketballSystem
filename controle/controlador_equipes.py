from entidade.equipe import Equipe
from tela.tela_equipes import TelaEquipes


MINIMO_DE_MEMBROS_EQUIPE = 1

class ControladorEquipes:
    def __init__(self):
        self.__equipes = list()
        self.__tela_equipes = TelaEquipes()
        self.__controlador_sistema = None

    @property
    def equipes(self) -> list[Equipe]:
        return self.__equipes

    @property
    def tela_equipes(self) -> TelaEquipes:
        return self.__tela_equipes

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @controlador_sistema.setter
    def controlador_sistema(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema

    def mostrar_opcoes(self):
        condicao_para_uso_1 = (len(self.controlador_sistema.controlador_cursos.cursos) > 0)
        condicao_para_uso_2 = (len(self.controlador_sistema.controlador_alunos.alunos) >= MINIMO_DE_MEMBROS_EQUIPE)
        if not (condicao_para_uso_1 and condicao_para_uso_2):
            return self.tela_equipes.mostrar_mensagem(
                f'Ao menos 1 curso e {MINIMO_DE_MEMBROS_EQUIPE} alunos cadastrados são necessários para utilizar o módulo de equipes'
            )
        opcoes = {
            '1': 'Listar Equipes',
            '2': 'Incluir Equipe',
            '3': 'Alterar Equipe',
            '4': 'Excluir Equipe',
            '10': 'Sair'
        }
        while True:
            opcao_escolhida = self.tela_equipes.mostrar_opcoes(opcoes)
            match opcao_escolhida:
                case '1': self.listar_equipes()
                case '2': self.incluir_equipe()
                case '3': self.alterar_equipe()
                case '4': self.excluir_equipe()
                case '10': break
                case _: self.tela_equipes.mostrar_mensagem('Opção Escolhida Não Existe')

    def listar_equipes(self):
        if len(self.equipes) == 0:
            return self.tela_equipes.mostrar_mensagem('Nenhuma Equipe cadastrada')
        dados_equipes = list()
        for equipe in self.equipes:
            dados_equipes.append({
                'codigo': equipe.codigo,
                'nome': equipe.nome,
                'nome_curso': equipe.curso.nome,
                'alunos': equipe.alunos
            })
        self.tela_equipes.listar_equipes(dados_equipes)

    def incluir_equipe(self) -> bool:
        dados = self.tela_equipes.incluir_equipe(MINIMO_DE_MEMBROS_EQUIPE)
        nome = dados['nome']
        codigo = dados['codigo']
        codigo_curso = dados['codigo_curso']
        # Verificando duplicidade de códigos
        if self.pesquisar_equipe_por_codigo(codigo) != None:
            self.tela_equipes.mostrar_mensagem('Uma equipe com este código já existe!')
            return False
        # Verificando existencia do curso
        indice_curso = self.controlador_sistema.controlador_cursos.pesquisar_curso_por_codigo(codigo_curso)
        if indice_curso == None:
            self.tela_equipes.mostrar_mensagem('Não existe curso com este código!')
            return False
        curso = self.controlador_sistema.controlador_cursos.cursos[indice_curso]
        # Tratamento para os alunos
        alunos = list()
        for matricula in dados['codigos_alunos']:
            # Verificando se o aluno está cadastrado
            indice_aluno = self.controlador_sistema.controlador_alunos.pesquisar_aluno_por_matricula(matricula)
            if indice_aluno is None:
                self.tela_equipes.mostrar_mensagem(f'Não existe aluno de com matrícula "{matricula}"!')
                return False
            # Verificando se o aluno já faz parte de uma equipe
            aluno = self.controlador_sistema.controlador_alunos.alunos[indice_aluno]
            for equipe in self.equipes:
                if aluno in equipe.alunos:
                    confirmacao_alterar_equipe = self.tela_equipes.confirmar_acao(
                        f'O aluno {aluno.nome} de mátricula {matricula} já faz parte da equipe {equipe.nome}\nAltualizar a equipe do aluno para equipe atual?'
                    )
                    if confirmacao_alterar_equipe:
                        equipe.alunos.remove(aluno)
                        alunos.append(aluno)
                    break
            else:
                alunos.append(aluno)
        if alunos < MINIMO_DE_MEMBROS_EQUIPE:
            self.tela_equipes.mostrar_mensagem(f'Cadastro da equipe cancelado. Número de alunos menor que {MINIMO_DE_MEMBROS_EQUIPE}')
        # Cadastrando a equipe
        nova_equipe = Equipe(nome, curso, codigo, alunos)
        self.equipes.append(nova_equipe)
        self.tela_equipes.mostrar_mensagem('Equipe cadastrada com sucesso')
        return True

    def excluir_equipe(self):
        if len(self.equipes) == 0:
            return self.tela_equipes.mostrar_mensagem('Nenhuma equipe cadastrada')
        codigo = self.tela_equipes.excluir_equipe()
        indice_equipe = self.pesquisar_equipe_por_codigo(codigo)
        if indice_equipe == None:
            self.tela_equipes.mostrar_mensagem(
                f'Equipe com código "{codigo}" não encontrada'
            )
        equipe = self.equipes[indice_equipe]
        confirmacao = self.tela_equipes.confirmar_acao(
            f'Deseja realmente excluir a equipe {equipe.nome}?'
        )
        if confirmacao:
            self.equipes.pop(indice_equipe)
            self.tela_equipes.mostrar_mensagem('Equipe excluída')
        else:
            self.tela_equipes.mostrar_mensagem('Exclusão cancelada')

    def alterar_equipe(self):
        if len(self.equipes) == 0:
            return self.tela_equipes.mostrar_mensagem('Nenhuma equipe cadastrada')
        dados = self.tela_equipes.alterar_equipe()
        codigo_antigo = dados['codigo_antigo']
        indice_equipe = self.pesquisar_equipe_por_codigo(codigo_antigo)
        if indice_equipe == None:
            self.tela_equipes.mostrar_mensagem(
                f'Equipe com código "{codigo_antigo}" não encontrado'
            )
        equipe = self.equipes[indice_equipe]
        confirmacao = self.tela_equipes.confirmar_acao(
            f'Deseja realmente alterar a equipe {equipe.nome}?'
        )
        if confirmacao:
            # Atualizando dados que foram retornados pela interface
            equipe.codigo = dados.get('novo_codigo', equipe.codigo)
            equipe.nome = dados.get('novo_nome', equipe.nome)
            codigo_novo_curso = dados.get('codigo_novo_curso')
            if codigo_novo_curso:
                indice_curso = self.controlador_sistema.controlador_cursos.pesquisar_curso_por_codigo(codigo_novo_curso)
                if indice_curso is None:
                    self.tela_equipes.mostrar_mensagem('Não existe curso o novo código informado!')
                    return self.alterar_equipe()
                equipe.curso = self.controlador_sistema.controlador_cursos.cursos[indice_curso]
            # Retornando uma mensagem de sucesso para o usuário
            self.tela_equipes.mostrar_mensagem('Equipe alterada')
        else:
            self.tela_equipes.mostrar_mensagem('Alteração cancelada')

    def pesquisar_equipe_por_codigo(self, codigo: int) -> int:
        """
        Retorna o índice do equipe com o código informado.\n  
        Se nenhuma equipe possuir o código informado retorna `None`
        """
        for i in range(len(self.equipes)):
            if self.equipes[i].codigo == codigo:
                return i
