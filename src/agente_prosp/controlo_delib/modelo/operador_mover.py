from agente_prosp.accoes.mover import Mover

class OperadorMover:
    """
     classe OperadorMover vai fazer as simulações necessárias para gerar o próximo estado.
    """
    def __init__(self, modelo_mundo, direcao):
        self.__modelo_mundo = modelo_mundo
        self.__ang = direcao.value
        self.__acao = Mover(direcao)

    def aplicar(self, estado):
        """
        Aplica e retorna um estado
        """

    def custo(self, estado, estado_suc):
        """
        Retorna o custo de passagem do estado atual para o 
        estado sucessor
        """

    @property
    def acao(self):
        """
        Getter da variável que contém a ação Mover
        """
        return self.__acao
    
    @property
    def ang(self):
        """
        Getter da variável que contém o valor do ângulo
        """
        return self.__ang
    
    def __repr__(self):
        return "OperadorMover(%s)" %self.acao
    