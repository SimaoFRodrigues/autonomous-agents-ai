from ecr.acao import Accao
from sae.agente.movimento import Movimento # Classe que nos dará os métodos para factorização

"""Esta classe, juntamente com Rodar e Avancar, são um exemplo de fatorização
 porque reutilizam código e apenas alteram o que muda no método"""
class Mover(Movimento, Accao):
    """Representa uma ação de movimento orientado.

    Esta ação desloca o agente segundo uma direção explícita, permitindo
    movimentos direcionais controlados.
    """

    def __init__(self, direccao):
        """Representa um movimento na direcao indicada.

        :param direccao: direção para onde o agente se deve mover
        :type direccao: Direccao
        """
        super.__init__(direccao, 1) # o segundo parâmetro é o passo, neste caso 1