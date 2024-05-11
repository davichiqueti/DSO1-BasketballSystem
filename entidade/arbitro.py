from entidade.pessoa import Pessoa
from datetime import date


class Arbitro(Pessoa):
    def __init__(self,
                 nome: str,
                 cpf: str,
                 data_nascimento: date,
                 estado: str,
                 cidade: str,
                 bairro: str,
                 numero_partidas: int
                 ):
        super().__init__(nome, cpf, data_nascimento, estado, cidade, bairro)
        if isinstance(numero_partidas, int):
            self.__numero_partidas = numero_partidas
        else:
            raise TypeError ("Arbitro.numero_partidas deve ser do tipo 'int'")
    @property
    def numero_partidas(self):
        return self.__numero_partidas

    @numero_partidas.setter
    def numero_partidas(self, numero_partidas: int):
        self.__numero_partidas = numero_partidas
