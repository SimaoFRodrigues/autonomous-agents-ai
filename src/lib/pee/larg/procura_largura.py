from lib.pee.larg.fronteira_fifo import FronteiraFIFO
from lib.pee.mec_proc.procura_grafo import ProcuraGrafo

"""
Classe que define que o mecanismo de procura a ser realizado é procura em largura,
configurando o mecanismo de procura em grafo para usar fronteira FIFO.

Interação entre classes:
- Herda de ProcuraGrafo e reutiliza o algoritmo base de procura (abstração por herança).
- Injeta FronteiraFIFO no construtor, definindo a estratégia de exploração por composição.
- O polimorfismo ocorre quando MecanismoProcura chama operações da fronteira sem conhecer
    a implementação concreta (FIFO, LIFO, prioridade, etc.).
"""
class ProcuraLargura(ProcuraGrafo):
    def __init__(self):
        """
        Usa-se super() para aproveitar a inicialização já feita na classe base, evitando repetir código.
        A FronteiraFIFO é passada no construtor para definir logo o tipo de procura, em largura.

Nota de interface: esta classe não altera o contrato de procura, apenas concretiza
o comportamento da memória/fronteira através da implementação FIFO.
        """
        super().__init__(FronteiraFIFO())