from lib.pee.prof.fronteira_lifo import FronteiraLIFO
from lib.pee.mec_proc.mecanismo_procura import MecanismoProcura

"""
Classe de procura em profundidade, este tipo de procura não é ótima nem completa, 
ou seja, pode não encontrar solução. Esta classe herda de MecanismoProcura e concretiza o 
comportamento da memória ao inserir FronteiraLIFO no construtor.
"""
class ProcuraProfundidade(MecanismoProcura):
    def __init__(self):
        """
        Usa-se super() para aproveitar a inicialização já feita na classe base, evitando repetir código.
        A FronteiraLIFO é passada no construtor para definir logo o tipo de procura, em profundidade.
        """
        super().__init__(FronteiraLIFO())