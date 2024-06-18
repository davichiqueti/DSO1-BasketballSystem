
class key_nao_encontrada_exception(Exception):
    # exception para keys não encontradas
    def __init__(self, mensagem="Cadastro não localizado."):
        super().__init__(mensagem)
