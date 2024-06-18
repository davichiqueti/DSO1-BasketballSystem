from abc import ABC, abstractmethod
import os
from unidecode import unidecode



class TelaBase(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def limpar_tela(self):
        os.system('cls' if os.name=='nt' else 'clear')

    def esperar_resposta(self):
        """Espera o usúario apertar `Enter` para continuar o funcionamento"""
        input('[Aperte Enter para continuar]\n')

    def confirmar_acao(self, mensagem) -> bool:
        print(f'\n[Mensagem do Sistema]: {mensagem}')
        resposta = input(f'[CONFIRMAR AÇÃO (S/Sim ou N/Não)]:')
        resposta = unidecode(resposta).lower().strip()
        if resposta in {'s', 'sim'}:
            return True
        elif resposta in {'n', 'nao'}:
            return False
        else:
            print('\n[Mensagem do Sistema]: Resposta inválida')
            return self.confirmar_acao(mensagem)

    def verificar_string_alpha(self, variavel) -> bool:
        if isinstance(variavel, str):
            variavel = variavel.split()
            for caracter in variavel:
                if not caracter.isalpha():
                    return False
            return True
