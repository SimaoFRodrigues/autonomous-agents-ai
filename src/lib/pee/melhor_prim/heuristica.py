from abc import ABC, abstractmethod

class Heuristica(ABC):
    """
    A Heuristica é uma classe abstrata para a função heurística. A mesma define o 
    contrato para estimar o custo desde estado n até objetivo.
    
    As classes concretas herdam de Heuristica (ex: HeuristicaContagem) e cada subclasse 
    tem de implementar h(estado) de forma específica. Quanto ao polimorfismo, o método 
    h() pode ser usado  em HeuristicaContagem com a distância euclidiana ou a de manhattan,
    mostrando que a mesma interface, pode ter múltiplas implementações conforme problema.
    
    Quanto ao encapsulamento o @abstractmethod h(estado) força as subclasses a 
    implementa-lo. A procura não conhece detalhes e se mudar a heurística, a procura 
    não muda porque a lógica da heurística é isolada.
    """
    @abstractmethod
    def h(self, estado):
        """Calcula estimativa heurística do custo de estado até objetivo"""