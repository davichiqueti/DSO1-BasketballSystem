
class SemRegistroException(Exception):
    #exception para listas vazias
    def __init__(self):    
        self.mensagem = "Não há registros no sistema."
        super().__init__(self.mensagem)