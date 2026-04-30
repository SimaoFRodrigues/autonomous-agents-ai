from lib.mod.problema import Problema
from .estado_contagem import EstadoContagem
from .operador_incremento import OperadorIncremento

"""
Problema de contagem.

O objetivo é partir de um valor inicial, atingir ou superar um valor final,
e escolher entre vários incrementos possíveis. Esta classe é adaptada à interface Problema, 
para que o mecanismo de procura possa reutilizar o mesmo algoritmo em vários domínios.
"""
class ProblemaContagem(Problema):
    
    def __init__(self, contagem_inicial, contagem_final, incrementos):
        """
        O construtor do Problema recebe o estado inicial, a lista de operadores e o valor final.
        """
        super().__init__(EstadoContagem(contagem_inicial), [OperadorIncremento(inc) for inc in incrementos])
        self.__contagem_final = contagem_final

    def objectivo(self, estado):
        """
        Método que verifica se a contagem do estado já atingiu ou ultrapassou o valor final.
        """
        return estado.contagem >= self.__contagem_final