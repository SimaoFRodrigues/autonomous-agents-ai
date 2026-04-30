from enum import Enum

"""Define os comandos/ações que podem ser executados no jogo."""
class ComandoJogo(Enum):
    """Conjunto fechado de comandos executáveis no ambiente.

    Cada valor deste enumerado representa uma ação da personagem no jogo. O uso do enumerado 
    garante que os comandos válidos ficam centralizados e evita o uso de valores soltos.
    """
    PROCURAR = 1
    APROXIMAR = 2
    OBSERVAR = 3
    FOTOGRAFAR = 4

    def mostrar(self):
        """Mostra no ecrã o comando associado à ação atual.

        Este método permite representar externamente o comando escolhido pelo
        agente, tornando a execução observável.
        """
        print(f"\nAção: {self.name}")