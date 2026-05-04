from agente_prosp.accoes.mover import Mover
import math

class OperadorMover:
    """
    A classe OperadorMover representa um operador que simula a transicao de movimento
    do agente para gerar um novo estado.
    Aqui existe encapsulamento da ação, do ângulo e da referência ao modelo do
    mundo. O mesmo tipo de operador pode ser criado para direçoes diferentes,
    o que permite usar polimorfismo quando o sistema trata operadores de forma
    uniforme.
    """
    def __init__(self, modelo_mundo, direcao):
        self.__modelo_mundo = modelo_mundo
        self.__ang = direcao.value
        self.__acao = Mover(direcao)

    def aplicar(self, estado):
        """
        Aplica a ação Mover sobre o estado recebido e retorna o estado sucessor
        """

    def custo(self, estado, estado_suc):
        """
        Retorna o custo de passagem do estado atual para o estado sucessor. O cálculo do custo 
        é a distância entre a posição do estado atual e a posição do estado sucessor. Esta linha 
        usa a ideia de programação funcional porque o valor é calculado diretamente a partir do 
        cosntrutor, sem alterar o estado interno do objeto. 
        """
        return max(math.dist(estado.posicao, estado_suc.posicao),1) # o custo nunca fica abaixo de 1 mesmo se a distância for zero

    @property
    def acao(self):
        """
        Getter da variável que contém a ação Mover
        """
        return self.__acao
    
    @property
    def ang(self):
        """
        Getter da variável que contém o valor do ângulo
        """
        return self.__ang
    
    def __repr__(self):
        """
        O __repr__ é um método especial do python que devolve uma representação em texto do
        objeto. Neste caso, serve para mostrar o operador de forma legível quando o
        objeto é impresso.
        """
        return "OperadorMover(%s)" %self.acao
    