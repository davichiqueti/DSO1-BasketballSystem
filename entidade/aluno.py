from entidade.curso import Curso
from entidade.pessoa import Pessoa
from datetime import date

class Aluno(Pessoa):
    def __init__(self,
                 nome: str,
                 cpf: str,
                 data_nascimento: date,
                 estado: str,
                 cidade: str,
                 bairro: str,
                 matricula: str,
                 curso: Curso
                 ):
        super().__init__(nome, cpf, data_nascimento, estado, cidade, bairro)
        if isinstance(matricula, str):
            self.__matricula = matricula
        else:
            raise TypeError ("Aluno.matricula deve ser do tipo 'str'.")
        if isinstance(curso, Curso):
            self.__curso = curso
        else:
            raise TypeError ("Aluno.curso deve ser do tipo 'curso'.")

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula: str):
        self.__matricula = matricula

    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, curso: Curso):
        self.__curso = curso
