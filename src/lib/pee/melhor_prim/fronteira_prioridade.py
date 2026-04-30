from lib.pee.mec_proc.fronteira import Fronteira
from heapq import heappush, heappop# biblioteca de filas com prioridade

"""
Classe referente ao tipo de fronteira com prioridade, esta prioridade refere-se ao custo, por isso 
quanto menor for maior a prioridade. Além disso, este tipo de fronteira será utilizada no algoritmo 
de procura melhor-primeiro.
"""
class FronteiraPrioridade(Fronteira):
    def __init__(self, avaliador):
        """Recebe um objeto que implementa a interface Avaliador."""
        super().__init__()
        self.__avaliador = avaliador

    def inserir(self, no):
        """
        Método que utiliza a biblioteca heapq e usa o método heappush que insere 
        um elemento na fila, mas de forma prioritária.
        Aqui, a prioridade do nó é obtida através do método prioridade(no) do avaliador 
        concreto recebido no construtor, demonstrando assim o uso de polimorfismo.
        """
        no.prioridade = self.__avaliador.prioridade(no) # o avaliador dá a prioridade do nó que serve para comparar as prioridades entre nós
        heappush(self._nos, no) # inserir nó na fronteira com prioridade

    def remover(self):
        """
        Método que utiliza a biblioteca heapq e usa o método heappop que remove um elemento da fila, 
        mas de forma prioritária.
        """
        return heappop(self._nos)
