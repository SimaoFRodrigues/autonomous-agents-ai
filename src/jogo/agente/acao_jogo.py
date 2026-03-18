class AcaoJogo:
    """Representa uma ação concreta no domínio do jogo.

    Esta classe funciona como invólucro de um comando do ambiente. Em vez de
    o agente manipular diretamente comandos do jogo, passa a trabalhar com uma
    abstração, o que separa melhor a decisão da execução.
    """

    def __init__(self, comando):
        """Cria a ação associada a um comando específico.

        O comando fica guardado na ação para ser executado mais tarde pelo
        ambiente, quando o agente concluir o ciclo perceção-ação.
        """
        self.__comando = comando

    @property
    def comando(self):
        """Expõe o comando associado à ação.

        Este acesso é usado quando a ação precisa de ser traduzida numa
        operação concreta no ambiente.
        """
        return self.__comando