from abc import ABC, abstractmethod

"""Define a estrutura base de um agente com ciclo perceção-ação."""

class Agente(ABC):
    def __init__(self,controlo):
        """Guarda o mecanismo de controlo usado para decidir ações.
        """
        # alias protegido para acesso pelas subclasses (como no UML: #controlo)
        self._controlo = controlo

    @abstractmethod
    def _percepcionar(self):
        """Obtém a perceção atual do ambiente.
        """
        raise NotImplementedError

    @abstractmethod
    def _actuar(self,acao):
        """Executa no ambiente a ação decidida pelo controlo.
        """
        raise NotImplementedError
    
    def executar(self):
        """Executa um passo do ciclo perceção-ação do agente."""
        percepcao = self._percepcionar()
        acao = self._controlo.processar(percepcao)
        if acao is not None:
            self._actuar(acao)
        


