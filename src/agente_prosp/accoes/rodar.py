from ecr.accao import Accao
from sae.agente.movimento import Movimento # Classe que nos dará os métodos para factorização

"""Esta classe, juntamente com Avancar e Mover, são um exemplo de fatorização
 porque reutilizam código e apenas alteram o que muda no método"""
class Rodar(Movimento, Accao):
    """Representa a ação de rotação do agente.

    Esta ação altera a orientação do agente sem deslocar a sua posição.
    """

    def __init__(self, direccao):
        """Inicializa a ação `Rodar` para uma direção específica.

        :param direccao: direção de rotação pretendida
        :type direccao: Direccao
        """
        super().__init__(direccao, 0) # como o passo é '0' o agente não avança e fica a rodar no mesmo sítio 