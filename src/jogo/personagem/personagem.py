from agente.agente_jogo import AgenteJogo
from .controlo_personagem import ControloPersonagem

class Personagem(AgenteJogo):
    """Representa a personagem controlada pelo agente no jogo.

    Esta classe concretiza o agente, ligando o ambiente do jogo ao mecanismo de controlo
    específico da personagem. O seu comportamento emerge da combinação entre observação do 
    ambiente, controlo pela máquina de estados e execução das ações.
    """

    def __init__(self, ambiente):
        """Inicializa a personagem com o ambiente e o controlo.

        A personagem recebe o ambiente onde atua e cria internamente o
        controlo responsável por decidir as ações em cada passo.
        """
        super().__init__(ambiente, ControloPersonagem())

    def mostrar(self):
        """Apresenta no ecrã o estado atual da personagem.

        Esta representação facilita a leitura do comportamento interno da
        personagem durante a execução do jogo.
        """
        print(f"\nEstado: {self._controlo.estado}")