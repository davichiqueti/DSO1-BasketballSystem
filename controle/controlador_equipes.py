from entidade.equipe import Equipe
from tela.tela_equipes import TelaEquipes


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
        opcoes = {
            '1': 'Listar Equipes',
            '2': 'Incluir Equipe',
            # '3': 'Alterar Equipe',
            # '4': 'Excluir Equipe',
            '10': 'Sair'
        }
        while True:
            opcao_escolhida = self.tela_equipes.mostrar_opcoes(opcoes)
            match opcao_escolhida:
                case '1': self.listar_equipes()
                case '2': self.incluir_equipe()
                # case '3': self.alterar_curso()
                # case '4': self.excluir_curso()
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
                'curso': equipe.curso,
                'alunos': equipe.alunos
            })
        self.tela_equipes.listar_equipes(dados_equipes)

    def incluir_equipe(self):
        dados = self.tela_equipes.incluir_equipe()
        nome = dados['nome']
        codigo = dados['codigo']
        codigo_curso = dados['codigo_curso']
        # Verificando duplicidade de códigos
        if self.pesquisar_equipe_por_codigo(codigo) != None:
            self.tela_equipes.mostrar_mensagem(
                'Uma equipe com este código já existe!')
            return self.incluir_equipe()
        indice_curso = self.controlador_sistema.controlador_cursos.pesquisar_curso_por_codigo(codigo_curso)
        if indice_curso == None:
            self.tela_equipes.mostrar_mensagem(
                'Não existe curso com este código!')
            return self.incluir_equipe()
        curso = self.controlador_sistema.controlador_cursos.cursos[indice_curso]
        nova_equipe = Equipe(nome, curso, codigo, list())
        self.equipes.append(nova_equipe)
        self.tela_equipes.mostrar_mensagem('Equipe cadastrada com sucesso')

    def pesquisar_equipe_por_codigo(self, codigo: int) -> int:
        """
        Retorna o índice do equipe com o código informado.\n  
        Se nenhuma equipe possuir o código informado retorna `None`
        """
        for i in range(len(self.equipes)):
            if self.equipes[i].codigo == codigo:
                return i
