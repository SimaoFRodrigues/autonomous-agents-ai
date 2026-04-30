from abc import ABC, abstractmethod
"""Define a interface de controlo responsável por decidir ações do agente."""

class Controlo(ABC):
    @abstractmethod
    def processar(self,percepcao,acao):
        """Processa perceções e determina a próxima ação.
        """
        raise NotImplementedError
    