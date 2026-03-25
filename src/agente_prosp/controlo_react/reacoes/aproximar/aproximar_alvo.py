from ecr.prioridade import Prioridade

class AproximarAlvo(Prioridade):
    """
    O aproximar alvo é um comportamento composto do tipo prioridade que tem internamente várias 
    instâncias de AproximarDir (outros comportamentos), que quando deteta um alvo na direcao 
    indicada, dispara um estímulo alvo nessa direção. 
    """
    raise NotImplementedError