from entidade.arbitro import Arbitro
from entidade.equipe import Equipe
from datetime import datetime


class Partida:
    def __init__(
        self,
        codigo: int,
        data: datetime,
        empate: bool,
        vencedor: Equipe | None,
        perdedor: Equipe | None,
        arbitro: Arbitro,
        equipes: list[Equipe],
        pontuacao: dict,
    ):
        # Tratamento para código
        if isinstance(codigo, int):
            self.__codigo = codigo
        else:
            raise TypeError('Partida.codigo deve ser do tipo "int"')
        # Tratamento para data
        if isinstance(data, datetime):
            self.__data = data
        else:
            raise TypeError('Partida.data deve ser do tipo "Date"')
        # Tratamento para vencedor, perdedor e empate
        if isinstance(empate, bool):
            self.__empate = empate
        else:
            raise TypeError('Partida.empate deve ser do tipo "bool"')
        if empate:
            if vencedor is None and perdedor is None:
                self.__vencedor = vencedor
                self.__perdedor = perdedor
            else:
                raise TypeError('Partida.vencedor e Partida.perdedor devem ser nulos em caso de empate')
        else:
            if isinstance(vencedor, Equipe) and isinstance(perdedor, Equipe):
                self.__vencedor = vencedor
                self.__perdedor = perdedor
            else:
                raise TypeError('Partida.vencedor e Partida.perdedor devem ser do tipo "Equipe"')
        # Tramento para arbitro
        if isinstance(arbitro, Arbitro):
            self.__arbitro = arbitro
        else:
            raise TypeError('Partida.arbitro deve ser do tipo "Arbitro"')
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
    def empate(self) -> bool:
        return self.__empate

    @property
    def vencedor(self) -> Equipe:
        return self.__vencedor

    @property
    def perdedor(self) -> Equipe:
        return self.__perdedor

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
    def data(self) -> datetime:
        return self.__data

    @data.setter
    def data(self, data: datetime):
        if isinstance(data, datetime):
            self.__data = data
        else:
            raise TypeError('Partida.data deve ser do tipo "Date"')

    @property
    def arbitro(self) -> Arbitro:
        return self.__arbitro

    @arbitro.setter
    def arbitro(self, arbitro: Arbitro) -> Arbitro:
        if isinstance(arbitro, Arbitro):
            self.__arbitro = arbitro
        else:
            raise TypeError('Partida.arbitro deve ser do tipo "Arbitro"')

    @property
    def pontuacao(self) -> dict[Equipe, int]:
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
