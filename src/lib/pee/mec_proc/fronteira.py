from abc import abstractmethod

class Fronteira:
    """
    Classe abstrata que define a estrutura de armazenamento de nós durante o processo de procura.
    As subclasses definem a estratégia de inserção (FIFO ou LIFO): FIFO (First In First Out) insere no final,
    remove do início (procura em largura); enquanto o LIFO (Last In First Out) insere no início, remove do 
    início (procura em profundidade).
    """
    def __init__(self):
        self.iniciar() # é chamado o método iniciar para não ficar com código repetido

    @property
    def vazia(self):
        """
        Método getter que retorna o valor booleano coorespondente ao estado 
        (vazio/não vazio) da fronteira

        O valor abaixo é gerado dinamicamente a partir do valor de outros atributos do projeto, 
        a esta propriedade chamamos propriedade derivada em que o valor retornado na propriedade 
        é derivada através de outros atributos
        """
        return len(self._nos) == 0 

    def iniciar(self):
        """
        Método que inicia a fronteira de Nós com uma lista vazia, limpa a fronteira
        """
        self._nos = []

    @abstractmethod
    def inserir(self, no):
        """
        Método abstrato que insere um elemento na fronteira, permite criar vários tipos de fronteira
        """

    def remover(self):
        """
        Método que remove o primeiro Nó da lista da fronteira e retorna o Nó
        """
        return self._nos.pop(0)

    