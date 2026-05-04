from .avaliador_heur import AvaliadorHeur

class AvaliadorSof(AvaliadorHeur):
    """
    O AvaliadorSof avalia a prioridade com f(n) = h(n) para a procura sôfrega.
    
    Esta classe herda de AvaliadorHeur reutilizando tudo e apenas implementando a 
    prioridade() sobreescrevendo com a procura sôfrega, sendo este o exemplo de polimorfismo.
    """
    def prioridade(self, no):
        """Retorna a função f(n) = h(n) - apenas a estimativa heurística"""
        return self.heuristica.h(no.estado) # f(n) = h(n)