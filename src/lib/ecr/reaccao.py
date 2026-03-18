from resposta import Resposta
from estimulo import Estimulo

class Reaccao:
    """Representa uma reação completa no ciclo reativo.

    A reação junta dois componentes, um Estimulo (que avalia a perceção) e uma Resposta (que define a ação).
    Assim, esta classe faz a ponte entre a deteção e a ação dentro do modelo estímulo-resposta-ação.

    Esta classe encapsula a decisão reativa. Cada reação corresponde a uma associação entre uma
    condição observada no ambiente e a atuação que o agente deve produzir.
    """

    def __init__(self, estimulo, resposta):
        """A reação fica responsável por coordenar os dois elementos centrais do
        processo reativo, medir a relevância de uma situação e produzir a
        resposta dessa situação.
        """
        self.__estimulo = Estimulo()
        self.__resposta = Resposta()
    
    def activar(self, percepcao):
        """Ativa a reação para a perceção recebida.

        O fluxo esperado é calcular a intensidade do estímulo para a perceção atual, 
        passar essa intensidade à resposta e obter a ação final.

        Assim, este método funciona para executar a reação, primeiro
        observa, depois avalia e no fim decide.
        """

        # Primeiro mede-se a relevância da situação atual através do estímulo.
        intensidade = self.__estimulo.detectar(percepcao)
        if intensidade > 0:
            # Se houver ativação, delega-se na resposta a construção da ação.
            accao = self.__resposta.activar(percepcao, intensidade)
        return accao