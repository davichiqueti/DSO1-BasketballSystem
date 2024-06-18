from DAO import DAO
from entidade.aluno import Aluno

class AlunoDAO(DAO):
    def __init__(self):
        super().__init__('aluno.pkl')

    def add(self, aluno: Aluno):
            super().add(aluno.matricula, aluno)

    def update(self, aluno: Aluno):
        if((aluno is not None) and isinstance(aluno, Aluno) and isinstance(aluno.matricula, int)):
            super().update(aluno.matricula, aluno)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)
