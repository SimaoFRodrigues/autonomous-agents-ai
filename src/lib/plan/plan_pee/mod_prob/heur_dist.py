from pee.melhor_prim.heuristica import Heuristica
import math

class HeurDist(Heuristica):
    """
    A HeurDist é uma heurística baseada na distância entre o estado atual e o estado objetivo.
    Esta heurística estima o custo restante até ao objetivo através da distância geométrica
    entre as posições dos dois estados.
    """

    def __init__(self, estado_final):
        super().__init__()
        self.__estado_final = estado_final

    def h(self, estado):
        """
        Este método faz parte do contrato de uma Heuristica e retorna um valor double 
        referente ao custo estimado da heurística do estado até ao objetivo.
        """
        pos_atual = estado.posicao
        pos_final = self.__estado_final.posicao
        return math.dist(pos_atual, pos_final)

