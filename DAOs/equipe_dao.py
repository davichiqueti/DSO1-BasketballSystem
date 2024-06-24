from DAO import DAO
from entidade.equipe import Equipe

#cada entidade terá uma classe dessa, implementação bem simples.
class EquipeDAO(DAO):
    def __init__(self):
        super().__init__('equipe.pkl')

    def add(self, equipe: Equipe):
            super().add(equipe.codigo, Equipe)

    def update(self, equipe: Equipe):
        if((equipe is not None) and isinstance(equipe, Equipe) and isinstance(equipe.codigo, int)):
            super().update(equipe.codigo, equipe)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)
