from abc import ABC, abstractmethod
import os


class TelaBase(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def limpar_tela(self):
        os.system('cls' if os.name=='nt' else 'clear')

    def mostrar_mensagem(self, mensagem: str):
        print('\n[Mensagem do Sistema]:', mensagem)
        self.esperar_resposta()

    def esperar_resposta(self):
        """Espera o usúario apertar `Enter` para continuar o funcionamento"""
        input('[Aperte Enter para continuar]\n')
