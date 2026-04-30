from abc import abstractmethod
from pee.mec_proc.procura_grafo import ProcuraGrafo
from .fronteira_prioridade import FronteiraPrioridade

""""""
class ProcuraMelhorPrim(ProcuraGrafo):
    def __init__(self, avaliador):
        super().__init__(FronteiraPrioridade(avaliador))
        self._avaliador = avaliador # o avaliador permite avaliar a prioridade

    def _manter(self, no):
        """
        Este método retorna True ou False se mantém não nos explorados ou se o custo 
        do novo nó for menor que o no que ja existe associado a esse estado explorado
        """
        return super()._manter(no) or no.custo < self._explorados[no.estado].custo