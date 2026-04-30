class No:
    """As instâncias podem ser comparadas com o critério que quisermos"""
    def __init__(self, estado, operador=None, antecessor=None, custo=0.0):
        self.__estado = estado
        self.__operador = operador
        self.__antecessor = antecessor
        self.__custo = custo

        if antecessor:
            self.__profundidade = antecessor.profundidade + 1
        else:
            self.__profundidade = 0
        self.__prioridade = 0 # este atributo dá suporte à comparação de Nós
    
    @property
    def estado(self):
        """
        Método getter do atributo estado
        """
        return self.__estado
    
    @property
    def operador(self):
        """
        Método getter do atributo operador
        """
        return self.__operador
    
    @property
    def antecessor(self):
        """
        Método getter do atributo antecessor
        """
        return self.__antecessor
    
    @property
    def profundidade(self):
        """
        Método getter do atributo profundidade
        """
        return self.__profundidade
    
    @property
    def custo(self):
        """
        Método getter do atributo custo
        """
        return self.__custo
    
    @property
    def prioridade(self):
        """
        Método getter do atributo prioridade
        """
        return self.__prioridade
    
    @prioridade.setter
    def prioridade(self, nova_prioridade):
        """
        Método setter do atributo prioridade
        """
        self.__prioridade = nova_prioridade


    def __lt__(self, no):
        """
        Neste método interno (estereótipo de comparação de instâncias) as instâncias podem ser comparadas com o critério que quisermos, neste caso
        vamos comparar a prioridade das instâncias de No. 

        lt -> less than
        """