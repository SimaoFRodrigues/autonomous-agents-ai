from abc import ABC, abstractmethod

class ModeloPlan(ABC):
    """"""

    @abstractmethod
    def obter_estado(self):
        """
        O método retorna o estado atual do sistema.
        """

    @abstractmethod
    def obter_estados(self):
        """
        O método retorna a lista de estados válidos.
        """
        
    @abstractmethod
    def obter_operadores(self):
        """
        O método retorna a lista de operadores.
        """