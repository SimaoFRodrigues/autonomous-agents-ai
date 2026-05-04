from mod.estado import Estado

class EstadoAgente(Estado):
    """
    A classe EstadoAgente especializa a classe Estado através de herança.
    A ideia é representar uma posição concreta do agente no ambiente, mas com um identificador estavel 
    calculado uma única vez. Isto mostra reutilização de comportamento da classe base e adaptacao do 
    estado ao problema do agente.
    """
    def __init__(self, posicao):
        """
        Os algoritmos de hash usam formulas matematicas para garantir que a chave é unica. Para 
        evitar esse cálculo para uma ação que é feita apenas 1 vez, no próprio construtor calculamos 
        o hash da posição e guardamos numa variável para ser retornada no método id_valor().
        """
        self.__posicao = posicao
        self.__id_valor = hash(self.posicao)
    
    def id_valor(self):
        """
        Método que retorna o valor do identificador hash (identificador único). Neste caso
        o valor é calculado uma vez quando é criado o EstadoAgente em vez de fazer o cálculo 
        cada vez que se invoca este método.
        """
        return self.__id_valor
    
    @property
    def posicao(self):
        """
        Getter da variável com o valor da posição
        """
        return self.__posicao