from abc import abstractmethod

class Problema:
    def __init__(self, estado_inicial, operadores):
        """
        Construtor da classe Problema que recebe o estado inicial do problema e os seus operadores.
        """
        self.__estado_inicial = estado_inicial
        self.__operadores = operadores

    @property
    def estado_inicial(self):
        """
        Método getter com restrição de read-only que retorna o valor do estado inicial
        """
        return self.__estado_inicial
    
    @property
    def operadores(self):
        """
        Método getter com restrição de read-only que retorna o valor do estado inicial
        """
        return self.__operadores

    @abstractmethod
    def objectivo(self, estado):
        """
        Tem de retornar um valor do tipo booleano, de forma a indicar se o estado é ou não
        igual ao objetivo
        """

    