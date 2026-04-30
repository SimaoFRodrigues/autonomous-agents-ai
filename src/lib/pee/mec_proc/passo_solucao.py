class PassoSolucao:
    """
    Esta classe refere-se a um objeto imutável e sem comportamento associado. Quando é criado, 
    recebe um estado e um operador, que é apenas para fins de consulta (read-only). 
    Este tipo de mecanismos são úteis para construir estruturas robustas.
    """
    def __init__(self, estado, operador):
        self.__estado = estado
        self.__operador = operador

    @property
    def estado(self):
        """
        Método de leitura apenas (getter) para fazer a leitura do estado
        """
        return self.__estado
    
    @property
    def operador(self):
        """
        Método de leitura apenas (getter) para fazer a leitura do operador
        """
        return self.__operador

