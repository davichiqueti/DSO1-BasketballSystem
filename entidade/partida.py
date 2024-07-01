from datetime import datetime


class Partida:
    def __init__(
        self,
        codigo: int,
        cpf_arbitro: str,
        equipe1: int,
        equipe2: int,
    ):
        # Tratamento para código
        if isinstance(codigo, int):
            self.__codigo = codigo
        else:
            raise TypeError('Partida.codigo deve ser do tipo "int"')
        # Tratamento para data

        if isinstance(cpf_arbitro, str):
            self.__cpf_arbitro = cpf_arbitro
        else:
            raise TypeError('Partida.cpf_arbitro deve ser do tipo "str"')
        # Tratamento para a lista de equipes da partida
        if isinstance(equipe1, int):
            self.__equipe1 = equipe1
        else:
            raise TypeError('Partida.equipes1 deve ser do tipo "int"')
        # Tratamento para a pontuação
        if isinstance(equipe2, int):
            self.__equipe2 = equipe2
        else:
            raise TypeError('Partida.equipes2 deve ser do tipo "int"')
        # Tratamento para a pontuação

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo
        else:
            raise TypeError('Partida.codigo deve ser do tipo "int"')

    @property
    def cpf_arbitro(self) -> str:
        return self.__cpf_arbitro

    @cpf_arbitro.setter
    def arbitro(self, cpf_arbitro: str):
        if isinstance(cpf_arbitro, str):
            self.__cpf_arbitro = cpf_arbitro
        else:
            raise TypeError('Partida.arbitro deve ser do tipo "Arbitro"')

    @property
    def equipe1(self) -> int:
        return self.__equipe1

    @property
    def equipe2(self) -> int:
        return self.__equipe2
    
    @equipe1.setter
    def equipe1(self, equipe1: int):
        if isinstance(equipe1, int):
            self.__equipe1 = equipe1
        else:
            raise TypeError("Partida.equipe1 deve ser do tipo str.")

    @equipe2.setter
    def equipe2(self, equipe2: int):
        if isinstance(equipe2, int):
            self.__equipe2 = equipe2
        else:
            raise TypeError("Partida.equipe2 deve ser do tipo str.")


