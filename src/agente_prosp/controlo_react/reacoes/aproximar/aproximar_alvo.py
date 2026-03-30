from ecr.prioridade import Prioridade
from .aproximar_dir import AproximarDir
from sae import Direccao

class AproximarAlvo(Prioridade):
    """
    O aproximar alvo é um comportamento composto do tipo prioridade que tem internamente várias 
    instâncias de AproximarDir (outros comportamentos), que quando deteta um alvo na direcao 
    indicada, dispara um estímulo alvo nessa direção. 

    Definicao de uma lista por intenção, ou seja, indicando a regra de construção dos elementos da lista
    """
    def __init__(self):
        """ A forma abaixo seria um exemplo de como poderia ser adicionada cada uma das direções:
        super().__init__([
            AproximarDir(Direccao.NORTE), 
            AproximarDir(Direccao.SUL),
            AproximarDir(Direccao.ESTE),
            AproximarDir(Direccao.OESTE)
            ])

            Em vez disso, vamos fazer a definição de uma lista por intenção, ou seja, indicando
            a regra de construção dos elementos da lista. Isto permite que possamos aumentar a 
            lista sem trocar este código.
        """
        super().__init__([AproximarDir(direccao) for direccao in Direccao]) 