from ..planeador import Planeador
from .mod_prob.problema_plan import ProblemaPlan
from .mod_prob.heur_dist import HeurDist
from .plano_pee import PlanoPEE
from pee.melhor_prim.procura_aa import ProcuraAA


class PlaneadorPEE(Planeador):
    """
    O PlaneadorPEE é uma concretização de Planeador baseada na procura em espaço de estados.
    A classe usa o mecanismo de Procura A* (heurística admissível) para encontrar uma sequência de passos 
    desde o estado inicial até ao objetivo, e devolve no fim um PlanoPEE com a solução encontrada.
    """
    def __init__(self):
        self.__mec_pee = ProcuraAA() # mecanismo de Procura A* (heurística admissível)

    def planear(self, modelo_plan, objetivos):
        """
        O método apesar de receber uma lista de objetivos, este método apenas precisa de 1, 
        e para isso usamos o objetivo do índice 0. Este retorna um plano de procura em espaço 
        de estados.
        """
        objetivo = objetivos[0]
        problema = ProblemaPlan(modelo_plan, objetivo)
        heuristica = HeurDist(objetivo)
        solucao = self.__mec_pee.procurar(problema, heuristica)
        return PlanoPEE(solucao)