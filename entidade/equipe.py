from entidade.curso import Curso


class Equipe():
    def __init__(self, nome: str, curso: Curso, codigo: int, alunos: list) -> None:
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise TypeError('Equipe.nome deve ser do tipo "str"')
        if isinstance(curso, Curso):
            self.__curso = curso
        else:
            raise TypeError('Equipe.curso deve ser do tipo "Curso"')
        if isinstance(codigo, int):
            self.__codigo = codigo
        else:
            raise TypeError('Equipe.codigo deve ser do tipo "int"')
        self.__alunos = alunos

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def curso(self) -> Curso:
        return self.__curso

    @curso.setter
    def curso(self, curso: Curso):
        self.__curso = curso

    @property
    def alunos(self): #-> list[Aluno]:
        return self.__alunos

    def incluir_aluno(self, aluno): #(self, aluno: Aluno):
        #if isinstance(aluno, Aluno):
        #    self.__alunos.append(aluno)
        #else:
        #    raise TypeError('Equipe.alunos só inclui objetos do tipo "Aluno"')
        self.__alunos.append(aluno)

    def excluir_aluno(self, aluno): #(self, aluno: Aluno)
        #if not isinstance(aluno, Aluno):
        #    raise TypeError('Equipe.alunos só possui objetos do tipo "Aluno"')
        #else:
        #    self.__alunos.remove(aluno)
        self.__alunos.remove(aluno)
