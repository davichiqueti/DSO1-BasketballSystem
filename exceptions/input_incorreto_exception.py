
class InputIncorreto(Exception):
#exception para inputs invalidos
    def __init__(self, mensagem = "Input incorreto."):
        super().__init__(mensagem)