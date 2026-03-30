from ecr.reaccao import Reaccao

from .estimulo_alvo import EstimuloAlvo
from .resposta_mover import RespostaMover
# Reacao
class AproximarDir(Reaccao):
    """Para esta classe é apenas necessário invocar o construtor da classe Reaccao, 
    que recebe um estimulo e uma resposta como parÂmetros e ambas as classes recebem uma distÂncia.
    
    Esta classe é outro bom exemplo de reutilização de classes e acoplamento, um conceito da programação orientada a objetos.
    """
    def __init__(self, direcao):
        super().__init__(EstimuloAlvo(direcao), RespostaMover(direcao))