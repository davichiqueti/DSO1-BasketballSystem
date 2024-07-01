
class AlunoDuplicadoException(Exception):
    #exception para inputs invalidos
    def __init__(self, aluno):    
        self.mensagem = f"O aluno {aluno.nome} já está cadastrado."
        super().__init__(self.mensagem)