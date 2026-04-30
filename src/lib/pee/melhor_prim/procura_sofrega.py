from lib.pee.melhor_prim.procura_informada import ProcuraInformada
from lib.pee.melhor_prim.aval.avaliador_sof import AvaliadorSof

class ProcuraSofrega(ProcuraInformada):
    """
    A Procura sôfrega é um método de procura, variante da procura melhor-primeiro, com 
    f(n) = h(n). Esta procura tem uma menor complexidade, soluções sub-ótimas e não tem 
    em conta o custo do percurso já explorado.
    
    A classe herda de ProcuraInformada, e usa polimorfismo tendo a mesma interface, com 
    comportamentos diferentes. Além disso, avaliadorSof encapsula a fórmula f(n) = h(n) 
    e a procura nunca vê o cálculo interno.
    """
    def __init__(self):
        """
        Inicializa com AvaliadorSof para f(n) = h(n), em que f(n) é baseada nos tipos de 
        funções de avaliação de custo, g(n) e h(n), e h(n) é a estimativa de custo de n 
        até ao objetivo
        """
        super().__init__(AvaliadorSof())