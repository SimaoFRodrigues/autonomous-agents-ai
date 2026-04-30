from .avaliador_heur import AvaliadorHeur

class AvaliadorAA(AvaliadorHeur):
    """
    Este avaliador avalia a prioridade com f(n) = g(n) + h(n) para a procura A*.
    
    AvaliadorAA herda de AvaliadorHeur reutilizando tudo e apenas implementando a 
    prioridade() sobreescrevendo a com o cálculo, sendo este o exemplo de polimorfismo.
    """
    def prioridade(self, no):
        """
        Retorna f(n) = g(n) + h(n) - combina custo real e estimativa
        """
        return no.custo + self.heuristica.h(no.estado) # f(n) = g(n) + h(n)