
class ArbitroDuplicado(Exception):
    #exception para inputs invalidos
    def __init__(self, arbitro):    
        self.mensagem = f"O aluno {arbitro.nome} já está cadastrado."
        super().__init__(self.mensagem)