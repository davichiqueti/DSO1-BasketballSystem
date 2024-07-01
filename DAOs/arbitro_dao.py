from DAOs.dao import DAO
from entidade.arbitro import Arbitro

#cada entidade terá uma classe dessa, implementação bem simples.
class ArbitroDAO(DAO):
    def __init__(self):
        super().__init__('arbitros.pkl')

    def add(self, arbitro: Arbitro):
        super().add(arbitro.cpf, arbitro)

    def update(self, arbitro: Arbitro):
        if((arbitro is not None) and isinstance(arbitro, Arbitro) and isinstance(arbitro.cpf, int)):
            super().update(arbitro.cpf, arbitro)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: Arbitro):
        return super().remove(key)
