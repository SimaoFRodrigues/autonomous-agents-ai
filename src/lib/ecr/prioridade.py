class Prioridade:
    """Representa uma estratégia de seleção baseada em prioridade.

    No contexto deste trabalho, esta classe representa uma política de seleção
    para situações em que vários comportamentos produzem ações concorrentes.
    Em vez de usar níveis fixos de precedência, a decisão é tomada comparando o
    valor de prioridade associado a cada ação.

    Esta classe funciona como base para uma família de estratégias de seleção. A relação com o polimorfismo é central,
    o restante sistema pode trabalhar sempre com a mesma operação `selecionar_acao`.Isto significa que o mecanismo de 
    composição de comportamentos fica desacoplado. O `ComportComp` apenas entrega uma lista de ações, cabe à estratégia
    concreta decidir depois.
    """

    def selecionar_acao(self, accoes):
        """Seleciona uma ação a partir de uma lista segundo o valor de prioridade.
        A implementação concreta deve comparar as prioridades das ações
        recebidas e devolver a ação considerada mais importante no instante
        atual.
        """
        if not accoes:
            return None
        """Aqui, key é um parâmetro, que vai servir de critério pelo max para comparar as açoes da lista, 
        e lambda é a função anónima que diz qual a prioridade a extrair de cada ação 
        para que o max devolva a ação com o maior valor de prioridade.
        """
        return max(accoes, key=lambda acao: acao.prioridade)
