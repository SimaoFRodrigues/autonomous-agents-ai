from abc import ABC, abstractmethod

class Planeador(ABC):
    """
    Um Planeador recebe um conjunto de objetivos e o modelo de planeamento, e regra um plano 
    na saída. O modelo de planeamento define o estado inicial, o conjunto de estados válidos 
    e o conjunto de operadores definidos; já os objetivos dados como entrada ao planeador são os objetivos 
    a atingir.
    """

    @abstractmethod
    def planear(self, modelo_plan, objetivos):
        """
        Este método retorna um Plano, recebendo como entrada o modelo do plano e a lista de 
        objetivos a atingir. A lógica deste método, por conta de ser abstrato, deixa as implementações 
        para as classes expecifiquem Planeador.
        """