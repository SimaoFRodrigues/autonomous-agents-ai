from ecr.accao import Accao
from sae.agente.movimento import Movimento # Classe que nos dará os métodos para factorização

"""Esta classe, juntamente com Mover e Rodar, são um exemplo de fatorização
 porque reutilizam código e apenas alteram o que muda no método"""
class Avancar(Movimento, Accao):
    """Representa a ação de avanço na direção atual do agente.

    Esta ação corresponde a uma deslocação para a frente, mantendo a direção
    atual do agente.
    """

    def __init__(self):
        """Inicializa a ação `Avancar`.

        Não requer parâmetros adicionais porque o avanço depende do estado
        atual do agente (posição e orientação).
        """
        super().__init__(None) # None porque é na direção do agente 