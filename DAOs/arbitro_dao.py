from DAOs.dao import DAO
from entidade.arbitro import Arbitro

#cada entidade terá uma classe dessa, implementação bem simples.
class ArbitroDAO(DAO):
    def __init__(self):
        super().__init__('arbitros.pkl')

    def add(self, arbitro: Arbitro):
        super().add(arbitro.cpf, arbitro)

    def update(self, key: Arbitro):
        super().update(key.cpf, key)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
