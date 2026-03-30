from ecr.reaccao import Reaccao

from .estimulo_obst import EstimuloObst
from .resposta_evitar import RespostaEvitar

class EvitarObst(Reaccao):
    """Esta classe implementa a classe Reaccao e o objetivo do comportamento evitar obstáculo é verificar se há algum nível hierarquico 
    acima de si, senão retorna a sua ação
    """
    def __init__(self):
        super().__init__(EstimuloObst(), RespostaEvitar())