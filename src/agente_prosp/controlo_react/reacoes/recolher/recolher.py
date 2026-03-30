from ecr.hierarquia import Hierarquia

from agente_prosp.controlo_react.reacoes.aproximar.aproximar_alvo import AproximarAlvo
from agente_prosp.controlo_react.reacoes.evitar.evitar_obst import  EvitarObst
from agente_prosp.controlo_react.reacoes.explorar.explorar import Explorar
from agente_prosp.controlo_react.reacoes.explorar.explorar_mem import ExplorarMem


class Recolher(Hierarquia):
    """
    O Recolher é um comportamento capaz de recolher a ação gerada após o processamento dos comportamentos evitar obstaculo,
    explorar com memória, explorar sem memória e aproximar. O recolher é uma especialização de Hierarquia, logo apenas 
    temos de implementar a ordem de prioridade.
    """
    def __init__(self):
        """Construtor da classe Recolher que define a ordem do comportamento conjunto de forma hierárquica"""
        comportamentos = [
            AproximarAlvo(), # comportamento de aproximar alvo, este é o comportamento com prioridade mais alta
            EvitarObst(), # comportamento de evitar obstáculo
            ExplorarMem(), # Comportamento de exploração com memória
            Explorar()] # comportamento de exploração sem memória, este é o comportamento com menos prioridade
        
        super().__init__(comportamentos) # cria o comportamento composto de forma hierarquica