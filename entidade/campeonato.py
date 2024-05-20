from entidade.equipe import Equipe
from entidade.partida import Partida


class Campeonato:
    def __init__(self, codigo: int, descricao: str, equipes: list[Equipe]):
        self.__partidas = list()
        self.__pontuacao = dict()
        self.__codigo = codigo
        if isinstance(descricao, str):
            self.__descricao = descricao
        else:
            raise TypeError('Campeonato.descricao deve ser do tipo "str"')
        # Tratamento das equipes
        if not isinstance(equipes, list):
            raise TypeError('Campeonato.equipes deve ser do tipo "list"')
        for item in equipes:
            if not isinstance(item, Equipe):
                raise TypeError('Campeonato.equipes só pode conter elementos do tipo "Equipe"')
        self.__equipes = equipes

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        if isinstance(descricao, str):
            self.__descricao = descricao
        else:
            raise TypeError('Campeonato.descricao deve ser do tipo "str"')       

    @property
    def equipes(self) -> list[Equipe]:
        return self.__equipes

    @property
    def partidas(self) -> list[Partida]:
        return self.__partidas

    def incluir_partida(self, partida: Partida):
        if isinstance(partida, Partida):
            self.partidas.append(partida)
        else:
            raise TypeError('Campeonato.partidas só pode conter elementos do tipo "Partida"')

    def excluir_partida(self, partida: Partida):
        if not isinstance(partida, Partida):
            raise TypeError('Remoção inválida. Campeonato.partidas só cóntem elementos do tipo "Partida"')
        elif partida not in self.partidas:
            raise ValueError('Campeonato.partidas não contém a partida a ser removida')
        else:
            self.partidas.remove(partida)

    @property
    def pontuacao(self) -> dict[Equipe, int]:
        return self.__pontuacao
