from abc import ABC, abstractmethod

"""
Classe que define o contrato funcional de avaliação da prioridade de um nó para
ordenação da fronteira por prioridade. Esta classe é abstrata porque tem como objetivo 
ter uma implementação diferente concretizada para cada tipo de procura.
Esta classe funciona como interface abstrata para FronteiraPrioridade e assim qualquer 
subclasse pode alterar a ordenação sem mudar a estrutura da fronteira.
"""
class Avaliador(ABC):

    @abstractmethod
    def prioridade(self, no):
        """Esta classe tem de retornar um valor do tipo double"""