
class CPFInvalidoException(Exception):
    def __init__(self, CPF):    
        self.mensagem = f"O CPF {CPF} já está cadastrado."
        super().__init__(self.mensagem)