from DAOs.dao import DAO
from entidade.equipe import Equipe

#cada entidade terá uma classe dessa, implementação bem simples.
class EquipeDAO(DAO):
    def __init__(self):
        super().__init__('equipe.pkl')

    def add(self, equipe: Equipe):
        super().add(equipe.codigo, equipe)

    def update(self, equipe: Equipe):
        if((equipe is not None) and isinstance(equipe, Equipe) and isinstance(equipe.codigo, int)):
            super().update(equipe.codigo, equipe)

    def get(self, key:Equipe):
        if isinstance(key, Equipe):
            return super().get(key)

    def remove(self, equipe: Equipe):
        return super().remove(equipe)
