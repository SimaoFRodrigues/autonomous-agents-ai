from lib.pee.melhor_prim.heuristica import Heuristica

class HeuristicaContagem(Heuristica):
    def __init__(self, valor_final):
        self.__valor_final =  valor_final

    def h(self, estado):
        """Este método cria a heurística de contagem e permite perceber quão perto está
        o valor inicial do final através da diferença"""
        return abs(self.__valor_final - estado.contagem)