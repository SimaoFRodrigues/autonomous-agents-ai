from .procura_profundidade import ProcuraProfundidade

"""
Classe que especializa a procura em profundidade, impondo um limite máximo
de profundidade na expansão dos nós. Este tipo de procura não é ótima nem completa, 
ou seja, pode não encontrar solução.
Esta classe herda de ProcuraProfundidade e reutiliza o algoritmo base definido em MecanismoProcura.
"""
class ProcuraProfLim(ProcuraProfundidade):
    
    def procurar(self, problema, prof_max=10):
        """
        Define o limite máximo de profundidade para esta execução e delega
        o restante processo de procura para a classe base.
        """
        self.__prof_max = prof_max
        return super().procurar(problema)

    def _expandir(self, problema, no):
        """
        Expande só se a profundidade do nó a expandir for inferior ao limite de profundidade, a 
        profundidade máxima. A utilização do super(). aqui exemplifica polimorfismo por herança,
        já que preserva a assinatura do método da superclasse e altera apenas a condição da procura.
        """
        return super()._expandir(problema, no) \
                if no.profundidade < self.__prof_max else []