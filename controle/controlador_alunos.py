from entidade.aluno import Aluno
from tela.tela_alunos import TelaAlunos
from DAOs.aluno_dao import AlunoDAO
from exceptions.sem_registro_exception import SemRegistroException


class ControladorAlunos():
    def __init__(self, controlador_sistema):
        self.__tela_alunos = TelaAlunos()
        self.__alunoDAO = AlunoDAO()
        self.__controlador_sistema = controlador_sistema

    def listar_aluno(self):
        dados_listagem_alunos = []
        alunos = self.__alunoDAO.get_all()

        try:
            if len(alunos) == 0:
                raise SemRegistroException()
        except SemRegistroException as e:
            return self.__tela_alunos.mostra_mensagem(e)
        
        for aluno in alunos:
            dados_listagem_alunos.append({"Nome": aluno.nome, "CPF": aluno.cpf, "Data de Nascimento": aluno.data_nascimento, "matricula": aluno.matricula})

        return self.__tela_alunos.listar_alunos(dados_listagem_alunos)

# inclusão OK!
    
    def incluir_aluno(self):
        dados = self.__tela_alunos.incluir_aluno()
        curso = self.__controlador_sistema.controlador_cursos.pesquisar_curso_por_codigo(int(dados['codigo do curso']))
        cpf = dados['CPF']


        #tratamento de exceção
        # Verificando duplicidade de códigos
        if curso is None:
            self.__tela_alunos.mostra_mensagem('Este código já existe!')
            return self.incluir_aluno()
        # Verificando duplicidade de nomes
        for aluno in self.__alunoDAO.get_all():
            if aluno.cpf == cpf:
                self.__tela_alunos.mostra_mensagem('Aluno com este CPF já existe!')
                return self.incluir_aluno()
            

        # Adicionando o curso à lista de cursos
        novo_aluno = Aluno(dados['Nome'], dados['CPF'], dados['Data de nascimento'], dados['Estado'], dados['Cidade'], dados['Bairro'], dados['Matricula'], curso)
        self.__alunoDAO.add(novo_aluno)
        self.__tela_alunos.mostra_mensagem(f'Curso {novo_aluno.nome} cadastrado com sucesso!')
                    


# Alteração
# Se alterar o CPF, vai dar erro no sistema!

    def alterar_aluno(self):
        cpf_selecionado = self.__tela_alunos.selecionar_aluno()
        if len(self.__alunoDAO.get_all()) == 0:
            self.__tela_alunos.mostra_mensagem("Sem aluno cadastrado.")
        # recebe o dicionario de alteracao
        dados_aluno_alteracao = self.__tela_alunos.alterar_aluno()


        for aluno in self.__alunoDAO.get_all():
            if aluno.cpf == cpf_selecionado:
                pass
            else:
                raise SemRegistroException
        # encontra o indice do curso na lista de objetos
        codigo_curso = dados_aluno_alteracao["codigo_curso"]
        curso_alteracao = self.__controlador_sistema.controlador_cursos.pesquisar_curso_por_codigo(codigo_curso)

        # verificacao codigo do curso
        if curso_alteracao is None:
            self.__tela_alunos.mostra_mensagem("Curso informado não encontrado.")
        

        # se o CPF antigo informado for encontrado na lista de objetos de alunos, o mesmo pode ser alterado
        novo_aluno = None
        for aluno in self.__alunoDAO.get_all():
            if cpf_selecionado == aluno.cpf:
                novo_aluno = aluno

        # verifica se o CPF novo já está sendo usado
        for alunos_existentes in self.__alunoDAO.get_all():
            cpf = alunos_existentes.cpf
            if dados_aluno_alteracao["CPF"] == cpf:
                self.__tela_alunos.mostra_mensagem("CPF informado não encontrado.")

        
            if novo_aluno in self.__alunoDAO.get_all():
                # alteracao
                novo_aluno.nome = dados_aluno_alteracao["Nome"]
                novo_aluno.data_nascimento = dados_aluno_alteracao["Data de nascimento"]
                novo_aluno.endereco.estado = dados_aluno_alteracao["Estado"]
                novo_aluno.endereco.cidade = dados_aluno_alteracao["Cidade"]
                novo_aluno.endereco.bairro = dados_aluno_alteracao["Bairro"]
                novo_aluno.matricula = dados_aluno_alteracao["matricula"]
                novo_aluno.curso = curso_alteracao
                self.__alunoDAO.update(novo_aluno)
                return self.__tela_alunos.mostra_mensagem(f"O cadastro do aluno: {novo_aluno.nome}, CPF: {novo_aluno.cpf} . Foi alterado com sucesso!")


# Exclusão: Ok
    def excluir_aluno(self):
        self.listar_aluno()
        cpf_exclusao = self.__tela_alunos.selecionar_aluno()
        aluno_exclusao = self.pesquisar_aluno_por_cpf(cpf_exclusao)

        if aluno_exclusao is None:
            self.__tela_alunos.mostra_mensagem("ATENCAO: Aluno não existente")
        else:
            print(aluno_exclusao.cpf)
            print(aluno_exclusao.nome)
            self.__alunoDAO.remove(aluno_exclusao.cpf)
            self.listar_aluno()
            self.__tela_alunos.mostra_mensagem("Aluno excluído com sucesso!")   
            self.retornar()


    def pesquisar_aluno_por_cpf(self, cpf:str) -> Aluno:
        for aluno in self.__alunoDAO.get_all():
            if aluno.cpf == cpf:
                return aluno

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_aluno,
            2: self.alterar_aluno,
            3: self.excluir_aluno,
            4: self.listar_aluno,
            0: self.retornar
        }
    
        continua = True
        while continua:
            lista_opcoes[self.__tela_alunos.mostrar_opcoes()]()
