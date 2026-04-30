from abc import abstractmethod
from .procura_melhor_prim import ProcuraMelhorPrim

class ProcuraInformada(ProcuraMelhorPrim):
    """
    A Procura informada com exploração seletiva usa a heurística h(n).
    Esta é uma classe base abstrata para ProcuraAA e ProcuraSofrega.
    
    Quanto à herança como estende ProcuraMelhorPrim, adicionando método procurar() que
    recebe heurística como parâmetro. Subclasses herdam este comportamento. Através do 
    polimorfismo as subclasses (ProcuraAA, ProcuraSofrega) usam diferentes avaliadores. 
    Quanto ao encapsulamento a classe injeta a heurística no avaliador através do setter.
    """
    def procurar(self, problema, heuristica):
        """
        Este método executa a procura informada injetando a heurística no avaliador
        """
        self._avaliador.heuristica = heuristica
        return super().procurar(problema)