from .percepcao_jogo import PercepcaoJogo
from agente.agente import Agente

"""Agente para o domínio do jogo

Quanto à herança, a implementação assume a classe base Agente. Esta classe 
recebe instâncias de ambiente e controlo no construtor, mantém ambiente 
privado para acesso interno e converte eventos do ambiente em PercepcaoJogo.
"""

class AgenteJogo(Agente):
    """Especializa o agente base para o domínio do jogo.

    Esta classe liga diretamente três elementos do sistema: o ambiente, onde
    os eventos são observados; a perceção, que representa esses eventos de
    forma estruturada; e o controlo, que decide a ação a executar.

    O objetivo é adaptar o ciclo genérico perceção-ação da classe `Agente` ao
    funcionamento concreto do jogo.
    """

    def __init__(self, ambiente, controlo):
        """Inicializa o agente com ambiente e estratégia de controlo.

        O ambiente é guardado para permitir observação e execução de ações,
        enquanto o controlo fica responsável por transformar perceções em
        decisões.a
        """
        super().__init__(controlo)
        self.__ambiente = ambiente

    def _percepcionar(self):
        """Observa o ambiente e converte o evento numa perceção.

        Este método corresponde à fase de entrada de informação do agente.
        Primeiro lê o evento atual do ambiente e depois encapsula esse valor
        num objeto `PercepcaoJogo`, que passa a circular no resto do sistema.
        """
        evento = self.__ambiente.observar() # Obtém o evento atual do ambiente e transforma-o numa perceção.
        return PercepcaoJogo(evento)

    def _actuar_(self, acao):
        """Executa no ambiente o comando encapsulado na ação.

        Esta é a fase final do ciclo do agente. A ação já foi decidida pelo
        controlo; aqui apenas se extrai o comando correspondente e se delega a
        execução ao ambiente.
        """
        self.__ambiente.executar(acao.comando)