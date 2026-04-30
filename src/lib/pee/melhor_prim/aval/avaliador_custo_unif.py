class AvaliadorCustoUnif:
    """
    Esta classe avalia a prioridade com f(n) = g(n). Encapsula cálculo de 
    custo uniforme (f(n) = g(n)) então a procura não sabe da fórmula, e 
    além disso implementa interface implícita (método prioridade()) e pode
    ser usado onde qualquer avaliador é esperado (polimorfismo).
    """

    def prioridade(self, no):
        """Retorna custo até ao nó, f(n) = g(n)"""
        return no.custo # f(n) = g(n)