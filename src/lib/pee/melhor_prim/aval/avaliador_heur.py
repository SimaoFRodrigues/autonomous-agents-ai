from abc import abstractmethod

class AvaliadorHeur:
    """
    Esta é a Classe base para os avaliadores com heurística, sendo a superclasse 
    para AvaliadorAA e AvaliadorSof já que define o comportamento comum.
    
    Quanto à herançca, AvaliadorAA e AvaliadorSof herdam de AvaliadorHeur e cada 
    uma delas implementa prioridade() de forma diferente, sendo aqui usado o 
    conceito de polimorfismo. Quanto ao encapsulamento neste caso o acesso à heurística 
    é apenas através do getter e do setter, protegendo a integridade da heurística.
    """
    def __init__(self):
        """Inicializa com heurística privada"""
        self.__heuristica = None

    @property
    def heuristica(self):
        """Getter para heurística"""
        return self.__heuristica
    
    @heuristica.setter
    def heuristica(self, heuristica):
        """Setter que permite injetar heurística"""
        self.__heuristica = heuristica