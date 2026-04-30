# O módulo random permite gerar um valor aleatório entre 0 e 1,
# e o choice vai ser usado para escolher um elemento aleatório de uma lista de direções
from random import random, choice

from sae import Direccao

from agente_prosp.accoes.rodar import Rodar
from agente_prosp.accoes.avancar import Avancar
from ecr.comportamento import Comportamento

class Explorar(Comportamento):
    """
    A classe é relativa ao comportamento explorar, que tem como objetivo decidir que ação de exploração gerar (Rodar ou Avancar). 
    Este comportamento tem de ter o método ativar e vai rodar aleatoriamente com uma determinada probabilidade. O comportamento
    Explorar() derivado desta classe, pode originar comportamentos cíclicos e podem ficar presos em alguns cantos do mapa, o que 
    pode causar o funcionamento incorreto do agente. Para a solução foi implementar a classe ExplorarMem, que Avança e guarda os
    movimentos anteriores de forma a combater esses erros.
    
    """
    def __init__(self, prob_rotacao = 0.7):
        self.__prob_rotacao = prob_rotacao # probabilidade de rotação predefinida, que serve como threshold para ativar a ação aleatória

    def activar(self, percepcao):
        """
        Este método vai gerar e retornar uma ação aleatória. O parâmetro percepcao não vai ser usado porque
        a decisão é feita independentemente da percepção, ou seja, tem baixo acoplamento funcional neste caso.
        Além disso, usa polimorfismo porque pode ser trocada por outros comportamentos sem mudar o controlo, 
        neste caso é recebido o parâmetro percepcao apesar de no Explorar não ser utilizado.
        """
        if random() < self.__prob_rotacao: # se o valor aleatório for menor que a probabilidade de rotação, gera uma ação
            # o Rodar vai retornar uma ação baseada na escolha aleatória de um membro da lista de Direcções e essa ação é
            # guardada na variável acao
            acao = Rodar(choice(list(Direccao))) 
        else: 
            acao = Avancar() # o método Avancar() simplesmente avança na direção que já está ativa
    
        return acao # único ponto de saída para reduzir entropia