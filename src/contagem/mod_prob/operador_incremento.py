from lib.mod.operador import Operador
from .estado_contagem import EstadoContagem

"""
Operador do problema de contagem.

Cada instância representa um incremento possível que aplicamos ao valor atual.
Para ser observável o efeito do custo na procura, o custo dos operadores será o 
quadrado do incremento. Este operador usa a interface abstrata Operador e é usado
pelo problema para criar sucessores na expansão dos nós.
"""
class OperadorIncremento(Operador):
    """
    Operador que acrescenta um valor fixo à contagem atual.
    """
    def __init__(self, incremento):
        """
        O construtor do OperadorIncremento recebe apenas o valor de incremento.
        """
        self.__incremento = incremento # valor de incremento

    @property
    def incremento(self):
        """
        Método de propriedade read-only que devolve o incremento associado ao operador,
        essa informação derá usada para descrever o conjunto de ações possíveis a partir
        de cada estado.
        """
        return self.__incremento
    
    def aplicar(self, estado):
        """
        Aplica o incremento ao estado recebido e devolve um novo EstadoContagem. Aqui há uso 
        de polimorfismo porque a procura chama aplicar() sem saber qual é o incremento, apenas 
        que tem um novo estado sucessor.
        """
        return EstadoContagem(estado.contagem + self.__incremento)
    
    def custo(self, estado, estado_suc):
        """
        Método que devolve o custo da ação, que é o quadrado do incremento.
        """
        return self.__incremento**2
    

   