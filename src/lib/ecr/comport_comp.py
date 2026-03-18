from abc import abstractmethod
from .comportamento import Comportamento

class ComportComp(Comportamento):
    """Representa um comportamento composto.

    Um comportamento composto junta vários comportamentos simples. Cada um é
    ativado para a mesma perceção e pode devolver uma ação. No fim, o conjunto
    de ações produzido é analisado para escolher a ação final.

    Esta abordagem permite organizar o controlo do agente de forma modular,
    separando comportamentos especializados e centralizando apenas a decisão
    final sobre qual ação deve prevalecer.
    """

    def __init__(self, comportamentos):
        """Guarda os comportamentos internos do comportamento composto.

        Cada elemento da lista representa um comportamento autónomo, capaz de
        analisar a perceção e propor uma ação.

        """
        self.__comportamentos = comportamentos

    @abstractmethod    
    def activar(self, percepcao):
        """Ativa os comportamentos internos e seleciona uma ação final.

        Cada comportamento é ativado com a mesma perceção. As ações válidas
        devolvidas por esses comportamentos são reunidas numa lista e depois
        passadas ao método `selecionar_acao`.

        O objetivo não é executar todas as ações, mas sim comparar as ações
        candidatas produzidas pelos vários comportamentos e escolher a mais
        adequada para a situação atual.
        """
        acoes = []

        # Ativa cada comportamento com a mesma perceção e guarda apenas as
        # ações efetivamente produzidas.
        for comp in self.__comportamentos:
            acao = comp.activar(percepcao)
            if acao is not None:
                acoes.append(acao)

        # Se existirem ações candidatas, delega a escolha final no método de
        # seleção definido pela subclasse.
        if acoes:
            return self.selecionar_acao(acoes)
        return None
    
    @abstractmethod    
    def selecionar_acao(self, acoes):
        """Seleciona a ação final a partir da lista de ações produzidas.

        Este método isola a política de decisão. Diferentes subclasses podem
        implementar critérios distintos, como prioridade máxima, primeira ação
        válida ou outro mecanismo de arbitragem.
        """
        raise NotImplementedError