from abc import abstractmethod
from lib.pee.mec_proc.no import No
from lib.pee.mec_proc.solucao import Solucao

class MecanismoProcura:
    def __init__(self, fronteira):
        self._fronteira = fronteira
    
    def _iniciar_memoria(self):
        """
        Método de implementação polimórfica que inicia a estrutura de memória de procura de acordo com o tipo de procura,
        incluindo a fronteira de exploração
        """
        self._fronteira.iniciar()
    
    def _memorizar(self, no):
        """
        Método de implementação polimórfica que memoriza um nó produzidos, e a sua concretização depende do tipo de procura
        """
        self._fronteira.inserir(no)

    def procurar(self, problema):
        """
        Método que implementa o algoritmo de procura desejado, este retorna a instância de Solucao que termina o nó
        """
        self._iniciar_memoria()
        no = No (problema.estado_inicial) # cria o nó inicial do problema
        self._memorizar(no) # após criar, memoriza-o criando a fronteira FIFO, LIFO ou prioridade

        while not self._fronteira.vazia: # enquanto a fronteira não tiver vazia
            no = self._fronteira.remover() # remove o primeiro nó da fronteira

            if problema.objectivo(no.estado): # se o estado associado ao nó for o objectivo do problema
                return Solucao(no) # retorna a solução que termina o nó
            
            for no_suc in self._expandir(problema, no): # por cada nó expandido
                self._memorizar(no_suc)
        

    def _expandir(self, problema, no):
        """
        Método que que implementa o algoritmo de expansão, que consiste em gerar os Nós sucessores de um Nó
        """
        sucessores = []
        estado = no.estado # obtém o estado do nó

        for operador in problema.operadores:
            estado_suc = operador.aplicar(estado)
            if estado_suc is not None:
                custo  = no.custo + operador.custo(estado, estado_suc) # custo acumulado até ao nó antecessor mais o custo da transição de estado
                no_suc = No (estado_suc, operador, no, custo) # gera o nó sucessor
                sucessores.append(no_suc) # junta o nó sucessor à lista de sucessores
        return sucessores
