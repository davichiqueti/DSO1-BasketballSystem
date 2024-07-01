from DAOs.dao import DAO
from entidade.aluno import Aluno

#cada entidade terá uma classe dessa, implementação bem simples.
class AlunoDAO(DAO):
    def __init__(self):
        super().__init__('alunos.pkl')

    def add(self, aluno: Aluno):
        super().add(aluno.cpf, aluno)

    def update(self, aluno: Aluno):
        if((aluno is not None) and isinstance(aluno, Aluno) and isinstance(aluno.cpf, int)):
            super().update(aluno.cpf, aluno)

    def get(self, key:Aluno):
        if isinstance(key, Aluno):
            return super().get(key)

    def remove(self , aluno: Aluno):
        return super().remove(aluno)