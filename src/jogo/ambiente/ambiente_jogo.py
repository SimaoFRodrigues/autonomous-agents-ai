from .evento_jogo import EventoJogo

class AmbienteJogo:
    """Representa o ambiente onde o agente observa eventos e executa os comandos.

    Esta classe é responsável por manter o evento atual do jogo, disponibilizá-lo ao agente 
    e fazer os comandos resultantes das ações escolhidas. Na prática, funciona como uma interface
    entre a parte externa do jogo a a decisão do agente.
    """

    def __init__(self):
        """Inicializa o catálogo de eventos possíveis e o estado interno.

        Aqui é criada uma tabela de correspondência entre os símbolos introduzidos pelo utilizador e os
        valores do enumerado `EventoJogo`. O evento atual começa indefinido."""
        self.__eventos = {evento.value: evento for evento in EventoJogo}
        self.__evento = None

    @property
    def evento(self):
        """Devolve o evento atual no ambiente, este valor representa a situação mais recente do agente.
        """
        return self.__evento
    
    def observar(self):
        """Fornece ao agente a perceção correspondente ao evento atual.

        Este método não transforma o evento, apenas disponibiliza o estado atual do ambiente para que o agente o possa converter numa perceção.
        """
        return self.__evento
    
    def evoluir(self):
        """Atualiza o estado do ambiente lendo um novo evento do utilizador.

        A evolução do ambiente corresponde à entrada de uma nova situação no
        sistema. Depois de gerar o evento, o ambiente apresenta-o no ecrã para
        tornar visível o estado observado.
        """
        self.__evento = self.__gerar_evento()
        if self.__evento is not None:
            self.__evento.mostrar()

    
    def executar(self, comando):
        """Executa no ambiente o comando escolhido pelo agente.

        Neste domínio, a execução é representada pela apresentação do comando no ecrã. Assim, o 
        ambiente torna observável a ação selecionada pelo agente.
        """
        comando.mostrar()

    def __gerar_evento(self):
        """Converte a entrada do utilizador num evento válido do jogo.

        Este método faz a leitura da entrada textual e tenta mapeá-la para um dos eventos definidos 
        no enumerado. Se a entrada não corresponder a nenhum símbolo conhecido, devolve `None`.
        """
        texto = input("\nEvento? ")
        return self.__eventos.get(texto)