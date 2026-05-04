from sae.ambiente.direccao import Direccao
from operador_mover import OperadorMover
from estado_agente import EstadoAgente
from sae.ambiente.elemento import Elemento
import math

class ModeloMundo:
    """
    O ModeloMundo mantém a informação da representação das ações que ele pode 
    realizar no mundo. Esta classe é composta por um conjunto de operadores e 
    tem um dicionário que contém uma representação interna do mundo.
    """
    def __init__(self):
        """"""
        self.__estado = None
        self.__alterado = False
        self.__estados = []
        self.__elementos = {}
        self.__operadores = [OperadorMover(self, direcao) for direcao in Direccao]

    @property
    def alterado(self):
        """
        Getter da variável que indica se foi alterado ou não
        """
        return self.__alterado
    
    def obter_estado(self):
        """
        Retorna o estado do agente
        """
        return self.__estado

    def obter_estados(self):
        """
        Retorna a lista com os estados do agente
        """
        return self.__estados

    def obter_operadores(self):
        """
        Retorna a lista de operadores mover do agente
        """
        return self.__operadores

    def obter_elemento(self, estado):
        """
        O método acede o dicionário Elemento usando o método .get() que acede a posição do estado. 
        Por fim retorna o elemento com base no estado do agente.
        """
        return self.__elementos.get() # o método .get() do dicionário faz com que se não existir, retorna None por omissão
        

    def distancia(self, estado):
        """
        Retorna o valor da distancia através do método dist() da biblioteca math do python.
        """
        return math.dist(estado.posicao, self.__estado.posicao) 

    def atualizar(self, percepcao):
        """
        O método recebe uma percepção e permite atualizar o estado atual do agente e atualizar a 
        variável booleanda que indica se foi ou não alterado (isto é, se os elementos que vêm da percepção 
        e os do mundo atual são diferentes).
        """
        self.__estado = EstadoAgente(percepcao.posicao)
        self.__alterado = self.__elementos != percepcao.elementos
        if self.__alterado:
            self.__elementos = percepcao.elementos # atualiza os elementos
            # os estados que o agente conhece são todos os estados das posições que a percepção traz
            self.__estados = [EstadoAgente(posicao) for posicao in percepcao.posicoes] 


    def mostrar(self, vista):
        """
        O método mostra o ambiente no painel, marcando todas as posições
        """
        for posicao, elemento in self.elementos.items(): # o método .items() dá-nos pares chave-valor 
            if elemento in [Elemento.ALVO, Elemento.OBSTACULO]:
                vista.mostrar_elemento(posicao, elemento) # vemos os alvos e obstáculos
        vista.marcar_posicao(self._estado.posicao) # vemos um retângulo amarelo na posição do agente

    def __contains__(self, estado):
        return estado in self.__estados