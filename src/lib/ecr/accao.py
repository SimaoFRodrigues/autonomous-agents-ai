# Este import permitemudar o nome da classe Accao para AccaoAgente
from agente.acao import Accao as AccaoAgente

class Accao(AccaoAgente):
    """Representa uma ação no ciclo de controlo do agente.

    A ação é o resultado final do processamento reativo. Depois da perceção
    ser analisada e de uma resposta ser ativada, é esta entidade que descreve
    o que o agente vai efetivamente executar.
    """

    def __init__(self):
        """Inicializa a ação com uma prioridade.

        Nesta implementação a ação começa com prioridade `0.0`, podendo esse
        valor ser alterado mais tarde por outros componentes do sistema.
        """
        self.prioridade = float(0)

    @property
    def prioridade(self):
        """Obtém a prioridade associada à ação.

        Este valor representa a importância relativa da ação face a outras
        ações candidatas.
        """
        return self.__prioridade


    @prioridade.setter
    def prioridade(self, nova_prioridade):
        """Atualiza a prioridade da ação.

        A alteração da prioridade permite adaptar a ação ao contexto atual,
        por exemplo quando a intensidade de um estímulo deve influenciar a
        escolha final.
        """
        self.__prioridade = nova_prioridade