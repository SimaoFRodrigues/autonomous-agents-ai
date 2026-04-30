from mod.estado import Estado

"""
Estado do problema de contagem.

Este estado representa o valor atual da contagem e serve para o mecanismo de procura 
comparar, alterar e memorizar ao longo do problema.
"""
class EstadoContagem(Estado):

    def __init__(self, contagem):
        """
        O construtor do EstadoContagem recebe apenas o valor da contagem.
        """
        self.__contagem = contagem 


    @property
    def contagem(self):
        """
        Este método de propriedade read-only devolve o valor atual da contagem de forma 
        a que a procura e os operadores leiam o estado sem o alterar, mantendo o encapsulamento.
        """
        return self.__contagem
    
    def id_valor(self):
        """
        Este método identifica o estado pelo próprio valor da contagem.
        """
        return self.__contagem


    