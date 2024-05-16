from abc import ABC, abstractmethod
from datetime import date
from entidade.endereco import Endereco


class Pessoa(ABC):
    def __init__(self, nome: str,
                 cpf: str, 
                 data_nascimento: date, 
                 estado: str, 
                 cidade: str, 
                 bairro: str):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise TypeError ("Pessoa.nome deve ser do tipo 'str'.")
        if isinstance(cpf, str):
            self.__cpf = cpf
        else:
            raise TypeError ("Pessoa.cpf deve ser do tipo 'str'.")
        if isinstance(data_nascimento, date):
            self.__data_nascimento = data_nascimento
        else:
            raise TypeError ("Pessoa.data_nascimento deve ser do tipo 'date'.")
        if isinstance(estado, str):
            self.__estado = estado
        else:
            raise TypeError ("Pessoa.estado deve ser do tipo 'str'.")
        if isinstance(cidade, str):            
            self.__cidade = cidade
        else:
            raise TypeError ("Pessoa.cidade deve ser do tipo 'str'.")
        if isinstance(bairro, str):
            self.__bairro = bairro
        else:
            raise TypeError ("Pessoa.bairro deve ser do tipo 'str'.")

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome 

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: date):
        self.__data_nascimento = data_nascimento
    
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
