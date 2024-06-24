from DAO import DAO
from entidade.campeonato import Campeonato

#cada entidade terá uma classe dessa, implementação bem simples.
class CampeonatoDAO(DAO):
    def __init__(self):
        super().__init__('campeonato.pkl')

    def add(self, campeonato: Campeonato):
            super().add(campeonato.codigo, Campeonato)

    def update(self, campeonato: Campeonato):
        if((campeonato is not None) and isinstance(campeonato, Campeonato) and isinstance(campeonato.codigo, int)):
            super().update(campeonato.codigo, campeonato)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)
