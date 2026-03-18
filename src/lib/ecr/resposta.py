class Resposta:
    """Representa a resposta associada a um estímulo.

    A resposta contém a lógica associada a um estímulo. Quando a
    intensidade desse estímulo justificar, a resposta define
    que ação deve ser produzida.

    Em termos de responsabilidade, esta classe faz a transição entre a fase
    de interpretação do ambiente e a fase de decisão. Ou seja, recebe informação
    já avaliada e transforma-a numa ação.
    """

    def __init__(self, accao):
        """Inicializa a resposta com a ação associada.

        A ação associada funciona como base para a decisão desta resposta.
        Dependendo da implementação, pode ser devolvida diretamente ou
        ser ajustada antes de ser retornada.
        """
        self._accao = accao
    
    def activar(self, intensidade):
        """Ativa a resposta e devolve a ação correspondente.

        A lógica deste método permite obter a ação associada a esta
        resposta e, caso exista, ajustar a sua prioridade com base na
        intensidade recebida. Desta forma, a força do estímulo influencia a
        importância da ação produzida.
        """

        # Obtém a ação definida para esta resposta e, se existir, adapta a
        # prioridade dessa ação ao nível de ativação recebido.
        if self._obter_accao is not None:
            self._acao.prioridade(intensidade)
            return self._accao
        

    def _obter_accao(self, percepcao):
        """Obtém a ação associada a esta resposta.

        Este método separa a lógica da ação do processo
        principal.
        """
        return self._accao