from agente_prosp.accoes.mover import Mover
from mod.operador import Operador
from estado_agente import EstadoAgente
import math

class OperadorMover(Operador):
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
        self.__ang = direcao.value # esta propriedade serve para calcular o ângulo de dx e dy, que vão ser usados para calcular a trajetória
        self.__acao = Mover(direcao)

    def aplicar(self, estado):
        """
        Aplica a ação Mover sobre o estado atual e retorna o estado sucessor.
        """
        x = estado.posicao[0]
        y = estado.posicao[1]
        dx = self.__acao.passo * math.cos(self.__ang)
        dy = -self.__acao.passo * math.sin(self.__ang)

        nova_pos = (x +  dx, y + dy) # construção de um tuplo da posição do proximo estado do agente
        estado_suc = EstadoAgente(nova_pos)
        if estado_suc in self.__modelo_mundo: 
            # o 'in' invoca por predefinição o método __contains__(), e cada método que quiser usar tem 
            # de definir a sua própria assinatura, como a classe ModeloMundo faz.
            return estado_suc # retorna o estado sucessor, se não fizer parte retorna None por omissão


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
    