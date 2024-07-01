from DAOs.dao import DAO
from entidade.endereco import Endereco

#cada entidade terá uma classe dessa, implementação bem simples.
class EnderecoDAO(DAO):
    def __init__(self):
        super().__init__('endereco.pkl')

    def add(self, endereco: Endereco):
            super().add(endereco.bairro, endereco)

    def update(self, endereco: Endereco):
        if((endereco is not None) and isinstance(endereco, Endereco) and isinstance(endereco.bairro, str)):
            super().update(endereco.bairro, endereco)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)
