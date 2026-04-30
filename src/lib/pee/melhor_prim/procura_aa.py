from lib.pee.melhor_prim.procura_informada import ProcuraInformada
from lib.pee.melhor_prim.aval.avaliador_aa import AvaliadorAA

class ProcuraAA(ProcuraInformada):
    """
    A procura A* (heurística admissível) com f(n) = g(n) + h(n), garante que 
    as soluções são ótimas e usa o menor custo computacional possível. Esta usa 
    a heurística admissível (otimista) que indica que 0 ≤ h(n) ≤ h*(n), onde a 
    estimativa de custo é sempre inferior ou igual ao custo mínimo. A procura A*
    é o melhor equilíbrio entre precisão e custo computacional.
    """
    def __init__(self):
        """
        Inicializa com AvaliadorAA para f(n) = g(n) + h(n), calculando o custo 
        acumulado até ao nó n mais o custo estimado até ao objetivo
        """
        super().__init__(AvaliadorAA())