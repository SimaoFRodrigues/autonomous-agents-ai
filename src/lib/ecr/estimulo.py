from abc import ABC, abstractmethod


class Estimulo(ABC):
    """Representa um estímulo no modelo de agentes reativos.

    Um estímulo corresponde a uma condição detetável a partir da perceção do
    ambiente. Essa condição pode representar proximidade de um obstáculo,
    presença de um alvo, existência de perigo ou qualquer outro fator
    relevante para o comportamento do agente.

    O papel desta classe é converter a perceção atual numa intensidade de
    ativação. Em vez de devolver apenas verdadeiro ou falso, o estímulo pode
    quantificar o grau de relevância da situação observada, permitindo uma
    resposta mais flexível.
    """
    def __init__(self):
        """Inicializa a classe base do estímulo.

        Esta classe é abstrata e serve apenas para definir o contrato comum
        dos estímulos concretos.
        """

    @abstractmethod
    def detectar(self, percepcao):
        """Avalia a perceção e devolve a intensidade do estímulo.

        Este método contém a lógica de deteção do estímulo. A implementação
        concreta decide como analisar a perceção e como traduzir essa análise
        num número.
        """
        raise NotImplementedError