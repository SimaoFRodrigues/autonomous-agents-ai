from abc import ABC, abstractmethod

class Operador(ABC):
    """
    Interface referente ao operador de transição de estado, que representa uma ação.

    Operadores representam ações que produzem transformações de estado. Estes abstraem 
    as transformações que podem ocorrer no estado do problema.
    """

    @abstractmethod
    def aplicar(estado):
        """
        Método que permite alicar um operador a um estado
        """
    @abstractmethod
    def custo(self, estado, estado_suc):
        """
        Método que retorna o custo da operação entre o estado atual e o estado sucessor. 
        Este método valor do tipo double.

        Neste caso, o custo refere-se aos recursos necessários para a transição de estado,
        e esse custo faz parte da atividade de avaliação de opções, que está inserida dentro 
        do processo de raciocínio automático.
        """