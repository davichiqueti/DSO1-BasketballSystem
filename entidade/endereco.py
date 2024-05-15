

class Endereco:
    def __init__(self, estado: str, cidade: str, bairro: str):
        if isinstance(estado, str):
            self.__estado = estado
        else: 
            raise TypeError("Endereco.estado deve ser do tipo 'str'")
        if isinstance(cidade, str):
            self.__cidade = cidade
        else:
            raise TypeError("Endereco.cidade deve ser do tipo 'str'")
        if isinstance(bairro, str):
            self.__bairro = bairro
        else:
            raise TypeError("Endereco.bairro deve ser do tipo 'str'")

    @property   
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self, estado: str):
        self.__estado = estado

    @property
    def cidade(self):
        return self.__cidade
    
    @cidade.setter
    def cidade(self, cidade: str):
        self.__cidade = cidade
    
    @property
    def bairro(self):
        return self.__bairro
    
    @bairro.setter
    def bairro(self, bairro: str):
        self.__bairro = bairro

    

