from entidade.arbitro import Arbitro
from entidade.equipe import Equipe
from datetime import date


class Partida:
    def __init__(
        self,
        codigo: int,
        data: date,
        arbitro: Arbitro,
        equipes: list[Equipe],
        pontuacao: dict = {},
    ):
        if isinstance(codigo, int):
            self.__codigo = codigo
        else:
            raise TypeError('Partida.codigo deve ser do tipo "int"')
        if isinstance(data, date):
            self.__data = data
        else:
            raise TypeError('Partida.data deve ser do tipo "Date"')
        # Tratamento para a lista de equipes da partida
        if isinstance(equipes, list):
            self.__equipes = equipes
        else:
            raise TypeError('Partida.equipes deve ser do tipo "list"')
        # Tratamento para a pontuação
        if isinstance(pontuacao, dict):
            self.__pontuacao = pontuacao
        else:
            raise TypeError('Partida.pontuacao deve ser do tipo "dict"')

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo
        else:
            raise TypeError('Partida.codigo deve ser do tipo "int"')

    @property
    def data(self) -> date:
        return self.__data

    @data.setter
    def data(self, data: date):
        if isinstance(data, date):
            self.__data = data
        else:
            raise TypeError('Partida.data deve ser do tipo "Date"')

    @property
    def pontuacao(self) -> dict:
        return self.__pontuacao

    @pontuacao.setter
    def pontuacao(self, pontuacao: dict):
        if isinstance(pontuacao, dict):
            self.__pontuacao = pontuacao
        else:
            raise TypeError('Partida.pontuacao deve ser do tipo "dict"')

    @property
    def equipes(self) -> list[Equipe]:
        return self.__equipes
