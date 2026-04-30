from lib.pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim
from lib.pee.melhor_prim.aval.avaliador_custo_unif import AvaliadorCustoUnif

class ProcuraCustoUnif(ProcuraMelhorPrim):
    """
    A procura de custo uniforme é um método de procura, variante da procura melhor-primeiro, 
    com f(n) = g(n). Explora primeiro nós com menor custo acumulado. Garante solução ótima. 
    Implementação por diferenças através da injeção de AvaliadorCustoUnif.
    """
    def __init__(self):
        """
        Inicializa com AvaliadorCustoUnif para f(n) = g(n), em que f(n) é baseada 
        nos tipos de funções de avaliação de custo, g(n) e h(n), e g(n) é o custo 
        do percurso até n.
        """
        super().__init__(AvaliadorCustoUnif())