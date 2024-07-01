from entidade.equipe import Equipe
from entidade.partida import Partida


class Campeonato:
    def __init__(self, codigo_campeonato: int, partida: Partida, pontucao_equipe1: int, pontuacao_equipe2: int, vencedor: str):
        self.__partida = partida
        self.__codigo_campeonato = codigo_campeonato
        self.__vencedor = vencedor
        self.__pontuacao_equipe1 = pontucao_equipe1
        self.__pontuacao_equipe2 = pontuacao_equipe2

    @property
    def partida(self) -> Partida:
        return self.__partida
    
    @partida.setter
    def partida(self, partida: Partida):
        if isinstance(partida, Partida):
            self.__partida = partida
        else:
            raise TypeError('Campeonato.partida deve ser do tipo "Partida"')

    @property
    def codigo_campeonato(self) -> int:
        return self.__codigo_campeonato
    
    @property
    def vencedor(self) -> str:
        return self.__vencedor
    
    @property
    def pontuacao_equipe1(self) -> int:
        return self.__pontuacao_equipe1
    
    @property
    def pontuacao_equipe2(self) -> int:
        return self.__pontuacao_equipe2
