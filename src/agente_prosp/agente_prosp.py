import sae
from agente.agente import Agente
class AgenteProsp(Agente):
    """Classe base para um agente prospetivo.

    Um agente prospetivo combina a observação do ambiente com a decisão da ação orientada. Esta classe 
    define o mínimo do ciclo de operação, que é percecionar e atuar.
    """

    def __init__(self, controlo):
        """Inicializa a estrutura base do agente prospetivo.
        """
        super.__init__(controlo)

    
    def _percepcionar(self):
        """Obtém a perceção atual do ambiente.

        Este método deve ser implementado nas subclasses para transformar o
        estado observado numa representação percetiva usada pela decisão. É feita delegação do
        método do Transdutor para não repetir.
        """
        return sae.transdutor.percepcionar() 
    
    
    def _actuar(self, accao):
        """Executa a ação escolhida pelo agente.

        Este método deve ser implementado nas subclasses para aplicar no
        ambiente a ação decidida no ciclo de controlo. É feita delegação do método do Transdutor
        para não repetir.
        """
        return sae.transdutor.actuar(accao) 