from DAOs.dao import DAO
from entidade.campeonato import Campeonato

class CampeonatoDAO(DAO):
    def __init__(self):
        super().__init__('campeonato.pkl')

    def add(self, campeonato: Campeonato):
            super().add(campeonato.codigo_campeonato, campeonato)

    def update(self, campeonato: Campeonato):
        if((campeonato is not None) and isinstance(campeonato, Campeonato) and isinstance(campeonato.codigo, int)):
            super().update(campeonato.codigo_campeonato, campeonato)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:Campeonato):
        if(isinstance(key, Campeonato)):
            return super().remove(key)
