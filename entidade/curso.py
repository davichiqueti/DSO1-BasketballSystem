

class Curso:
    def __init__(self, codigo: int, nome: str):
        if isinstance(codigo, int):
            self.__codigo = codigo
        else:
            raise TypeError('Curso.codigo deve ser do tipo "int"')
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise TypeError('Curso.nome deve ser do tipo "str"')

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo
        else:
            raise TypeError('Curso.codigo deve ser do tipo "int"')

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise TypeError('Curso.nome deve ser do tipo "str"')
