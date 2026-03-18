from abc import ABC, abstractmethod

from comport_comp import ComportComp

class Comportamento(ABC):
    """Classe base para os comportamentos do agente.

    Um comportamento define uma regra de atuação baseada na perceção atual do
    ambiente. O resultado dessa avaliação pode ser uma ação ou a ausência de
    ação, caso o comportamento não deva intervir naquele momento.Esta abstração
    permite tratar de forma uniforme comportamentos simples e comportamentos compostos.
    """

    def __init__(self):
        """Inicializa a estrutura comum de um comportamento.

        Nesta versão existe uma referência interna a um comportamento
        composto, o que permite integrar o comportamento numa estrutura mais
        complexa de composição.
        """
        self.__comportamentos = ComportComp()

    @abstractmethod
    def activar(self, percepcao):
        """Ativa o comportamento para a perceção recebida.

        Este método define o contrato principal da classe. Cada implementação
        concreta deve analisar a perceção e decidir se produz uma ação.
        """
        raise NotImplementedError

