from agente.controlo import Controlo
from modelo.modelo_mundo import ModeloMundo
from mec_delib import MecDelib

class ControloDelib(Controlo):
    """
    A classe ControloDelib implementa a interface Controlo e organiza o ciclo deliberativo do agente.
    Esta classe junta herança e implementação de interface já que herda de Controlo
    para respeitar o esperado pelo sistema, e coordena a assimilacao, deliberacao, planeamento e
    execução. O resultado é um controlador modular, mais fácil de reutilizar e de substituir por 
    outras estratégias de controlo.
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
        """
        Constrói um plano de ação a partir dos objetivos
        deliberados, delegando a tarefa ao `planeador` fornecido.
        """

    def _executar(self):
        """
        Executa o plano atual, invocando as ações sobre o modelo do mundo e atualizando 
        o plano conforme cada ação é consumida, reconsiderando se necessário.
        """

    def _mostrar(self):
        """
        Exibe o estado interno para visualização.
        """