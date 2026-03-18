class PercepcaoJogo():
    """Representa a perceção do agente no contexto do jogo.

    A perceção funciona como intermediário entre o ambiente e o controlo. Em
    vez de o controlo depender diretamente do evento bruto observado, trabalha
    sobre um objeto próprio, mais adequado ao ciclo interno do agente.
    """

    def __init__(self, evento):
        """Inicializa a perceção com o evento recebido do ambiente.

        O evento observado fica encapsulado para poder ser lido por outros
        componentes sem acoplamento direto ao ambiente.
        """
        self.__evento = evento

    @property
    def evento(self):
        """Devolve o evento encapsulado nesta perceção.

        Este acesso permite ao controlo analisar a situação atual e escolher a
        transição ou ação mais adequada.
        """
        return self.__evento