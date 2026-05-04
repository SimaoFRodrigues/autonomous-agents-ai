from agente.controlo import Controlo
from modelo.modelo_mundo import ModeloMundo
from mec_delib import MecDelib

class ControloDelib(Controlo):
    """
    O ControloDelib processa internamente um ciclo de tomada de decisão e ação 
    que foi criado antes, ou seja, perante as percepções obtidas do ambiente, 
    gera as ações que devem ser realizadas. Esta classe realiza a interface Controlo 
    do pacote agente, já que o agente pode ser criado desde que tenha uma classe 
    que realize a interface Controlo associada.
    Esta classe dá a estrutura base usando o mecanismo deliberativo modularizado na 
    classe mec_delib.
    """
    def __init__(self, planeador):
        self.__planeador = planeador
        self.__modelo_mundo = ModeloMundo()
        self.__mec_delib = MecDelib(self.__modelo_mundo)
        self.__objetivos = []
        self.__plano = None

    def processar(self, percepcao):
        """
        O método processar gera uma ação a realizar
        """

    def _assimilar(self, percepcao):
        """
        O método privado assimilar vai atualizar o modelo do mundo baseando-se no
        parâmetro de percepção.
        """
        return self.__modelo.mundo.atualizar(percepcao)

    def _reconsiderar(self):
        """
        O método retorna um booleano que indica se é ou não para reconsiderar.
        """
        return self.__modelo_mundo.alterado or not self.__plano 


    def _deliberar(self):
        """
        Este método inicia os objetivos preenchendo a lista com os objetivos 
        deliberados.
        """
        self.__objetivos = self.__mec_delib.deliberar()

    def _planear(self):
        """"""

    def _executar(self):
        """"""

    def _mostrar(self):
        """"""