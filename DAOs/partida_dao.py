from DAO import DAO
from entidade.partida import Partida

#cada entidade terá uma classe dessa, implementação bem simples.
class PartidaDAO(DAO):
    def __init__(self):
        super().__init__('partida.pkl')

    def add(self, partida: Partida):
            super().add(partida.codigo, Partida)

    def update(self, partida: Partida):
        if((partida is not None) and isinstance(partida, Partida) and isinstance(partida.codigo, int)):
            super().update(partida.codigo, partida)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)
