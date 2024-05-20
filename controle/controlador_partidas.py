from entidade.partida import Partida
from tela.tela_partidas import TelaPartidas


class ControladorPartidas:
    def __init__(self) -> None:
        self.__partidas = list()
        self.__tela_partidas = TelaPartidas()
        self.__controlador_sistema = None
        self.__ultimo_codigo_gerado = 0

    @property
    def partidas(self) -> list[Partida]:
        return self.__partidas

    @property
    def tela_partidas(self) -> TelaPartidas:
        return self.__tela_partidas

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @controlador_sistema.setter
    def controlador_sistema(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema

    def mostrar_opcoes(self):
        opcoes = {
            '1': 'Listar Partidas',
            '2': 'Incluir Partida',
            '3': 'Alterar Partida',
            '4': 'Excluir Partida',
            '10': 'Sair'
        }
        opcao_escolhida = str()
        while True:
            opcao_escolhida = self.tela_partidas.mostrar_opcoes(opcoes)
            match opcao_escolhida:
                case '1': self.listar_partidas()
                case '2': self.incluir_partida()
                case '3': self.alterar_partida()
                case '4': self.excluir_partida()
                case '10': break
                case _: self.tela_partidas.mostrar_mensagem('Opção Escolhida Não Existe')

    def listar_partidas(self):
        if len(self.partidas) == 0:
            self.tela_partidas.mostrar_mensagem('Nenhuma partida registrada')
            return
        dados_partidas = list()
        for partida in self.partidas:
            dados_partida = {
                'codigo': partida.codigo,
                'data': partida.data,
                'arbitro': {'nome': partida.arbitro.nome, 'cpf': partida.arbitro.cpf},
                'pontuacao_equipes': {equipe.nome: pontuacao for equipe, pontuacao in partida.pontuacao.items()}
            }
            dados_partidas.append(dados_partida)
        self.tela_partidas.listar_partidas(dados_partidas)

    def incluir_partida(self):
        if len(self.controlador_sistema.controlador_equipes.equipes) < 2:
            self.tela_partidas.mostrar_mensagem(
                'Para registrar uma partida, o sistema deve ter ao mínimo 2 equipes cadastradas'
            )
            return
        dados = self.tela_partidas.incluir_partida()
        # Carregando dados
        data = dados['data']
        # Tratamento para o arbitro
        cpf_arbitro = dados['cpf_arbitro']
        arbitro = self.controlador_sistema.controlador_arbitros.pesquisar_arbitros_por_cpf(cpf_arbitro)
        if arbitro is None:
            self.tela_partidas.mostrar_mensagem(f'Arbitro com cpf "{cpf_arbitro}" não encontrado')
            return self.incluir_partida()
        # Tratamento para as equipes da partida
        codigo_equipe_1 = dados['codigo_equipe_1']
        codigo_equipe_2 = dados['codigo_equipe_2']
        equipe_1 = self.controlador_sistema.controlador_equipes.pesquisar_equipe_por_codigo(codigo_equipe_1)
        equipe_2 = self.controlador_sistema.controlador_equipes.pesquisar_equipe_por_codigo(codigo_equipe_2)
        if equipe_1 is None:
            self.tela_partidas.mostrar_mensagem(f'Equipe com código "{codigo_equipe_1}" não encontrado')
            return self.incluir_partida()
        if equipe_2 is None:
            self.tela_partidas.mostrar_mensagem(f'Equipe com código "{codigo_equipe_2}" não encontrado')
            return self.incluir_partida()
        dados_alunos_equipe_1 = [{'nome': aluno.nome, 'matricula': aluno.matricula} for aluno in equipe_1.alunos]
        dados_alunos_equipe_2 = [{'nome': aluno.nome, 'matricula': aluno.matricula} for aluno in equipe_2.alunos]
        pontuacao_equipe_1 = self.tela_partidas.alterar_pontuacao_equipe(equipe_1.nome, dados_alunos_equipe_1)
        pontuacao_equipe_2 = self.tela_partidas.alterar_pontuacao_equipe(equipe_2.nome, dados_alunos_equipe_2)
        pontuacao = {equipe_1: pontuacao_equipe_1, equipe_2: pontuacao_equipe_2}
        # Instanciando objeto e armazenando na lista
        self.__ultimo_codigo_gerado += 1
        nova_partida = Partida(
            codigo=self.__ultimo_codigo_gerado,
            data=data,
            arbitro=arbitro,
            equipes=[equipe_1, equipe_2],
            pontuacao=pontuacao
        )
        self.partidas.append(nova_partida)
        self.tela_partidas.mostrar_mensagem('Partida registrada com sucesso')

    def alterar_partida(self):
        if len(self.partidas) == 0:
            return self.tela_partidas.mostrar_mensagem('Nenhum curso cadastrado')
        dados = self.tela_partidas.alterar_partida()
        codigo_antigo = dados['codigo_antigo']
        indice_curso = self.pesquisar_curso_por_codigo(codigo_antigo)
        if indice_curso == None:
            self.tela_cursos.mostrar_mensagem(
                f'Curso com código "{codigo_antigo}" não encontrado'
            )
        curso = self.cursos[indice_curso]
        confirmacao = self.tela_cursos.confirmar_acao(
            f'Deseja realmente alterar o curso {curso.nome}?'
        )
        if confirmacao:
            # Atualizando dados do curso que foram retornados pela interface
            novo_codigo = dados.get('novo_codigo')
            if novo_codigo is not None:
                if novo_codigo != codigo_antigo and self.pesquisar_curso_por_codigo(novo_codigo) != None:
                    self.tela_cursos.mostrar_mensagem('Já existe um curso com este código!')
                    return self.alterar_curso()
                curso.codigo = novo_codigo
            curso.nome = dados.get('novo_nome', curso.nome)
            # Retornando uma mensagem de sucesso para o usuário
            self.tela_cursos.mostrar_mensagem('Curso alterado')
        else:
            self.tela_cursos.mostrar_mensagem('Alteração cancelada')

    def excluir_partida(self):
        if len(self.cursos) == 0:
            return self.tela_partidas.mostrar_mensagem('Nenhuma partida registrada')
        codigo = self.tela_partidas.excluir_partida()
        indice_partida = self.pesquisar_partida_por_codigo(codigo)
        if indice_partida == None:
            self.tela_partidas.mostrar_mensagem(
                f'Curso com código "{codigo}" não encontrado'
            )
        confirmacao = self.tela_partidas.confirmar_acao(
            f'Deseja realmente excluir a partida com código {codigo}?'
        )
        if confirmacao:
            self.partidas.pop(indice_partida)
            self.tela_partidas.mostrar_mensagem('Partida excluída')
        else:
            self.tela_partidas.mostrar_mensagem('Exclusão cancelada')

        
    def pesquisar_partida_por_codigo(self, codigo: int) -> int:
        """
        Retorna o índice do curso com o código informado.\n  
        Se nenhum curso possuir o código informado retorna `None`
        """
        for i in range(len(self.partidas)):
            if self.partidas[i].codigo == codigo:
                return i
