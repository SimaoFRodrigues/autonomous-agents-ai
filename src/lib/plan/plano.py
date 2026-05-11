from abc import ABC, abstractmethod

class Plano(ABC):
    """
    A classe Plano é uma sequência organizada de ações que indica o que o agente deve 
    fazer para passar do estado inicial até ao objetivo. Ou seja, funciona como um caminho de 
    ações que controla o agente até atingir o objetivo final.
    """

    @abstractmethod
    def obter_acao(self, estado):
        """
        Método que retorna o Operador relativo ao passo, tendo em conta o estado (a implementar 
        pelas classes fichas que utilizem Plano).
        """
    
    @abstractmethod
    def mostrar(self, vista):
        """
        Método que mostra o plano obtido, a implementar pelas classes fichas que utilizem Plano
        devido a ser um método abstrato.
        """