from ecr.estimulo import Estimulo
from sae import Elemento

class EstimuloAlvo(Estimulo):
    """Esta classe implementa a interface Estimulo e visa calcular a intensidade de um alvo numa determinada percepção."""

    def __init__(self, direcao, gama=0.9):
        """Contrutor da classe EstimuloAlvo que recebe direção e a gama que é definido inicialmente como 0.9.
        Quanto mais baixa for a base, mais profunda será a exponencial e vice versa"""
        self.__direcao = direcao
        self.__gama = gama

    def detectar(self, percepcao):
        """Dada uma percepcao devolve um float relativo à intensidade, 
        Se estiver muito perto devolve 1, se estiver afastado vai decaindo exponencialmentre (f(x) = 0.9^x). 
        O agente tem sensores nas 4 direcoes (Norte, sul, este, oeste), ja que o EstimuloAlvo está associado a direcao
        """
        """A percepcao quando indexada numa direcao produz um tuplo com 3 parêmetros com o elemento detectado, a distancia e a posição"""
        (elemento, distancia, _) = percepcao[self.__direcao]
        """Aqui usamos o operador ternário do python para fazer o retorno do valor, que neste caso retorna o valor
        se a condição for verdadeira. Resumidamente, se o elemento for o elemento alvo, é calculada a intensidade 
        de acordo com o valor de gama, senão retorna 0. 
        """
        return self.__gama ** distancia if elemento == Elemento.ALVO else 0