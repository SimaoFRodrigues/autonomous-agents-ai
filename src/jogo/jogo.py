from ambiente.ambiente_jogo import AmbienteJogo
from personagem.personagem import Personagem
from ambiente.evento_jogo import EventoJogo

class Jogo:
    """Controla o ciclo principal entre o ambiente e o personagem."""
    def __init__(self):
        """Cria o ambiente e a personagem e mostra o estado inicial."""
        self.__ambiente = AmbienteJogo()
        self.__personagem = Personagem(self.__ambiente)
        self.__personagem.mostrar()

    def executar(self):
        """Executa o ciclo principal do jogo.

        Em cada iteração o ambiente evolui, se o evento observado for
        ``TERMINAR``, o ciclo termina. Caso contrário, a personagem executa
        a sua ação e o estado é apresentado.
        """
        while(True):
            self.__ambiente.evoluir()
            if (self.__ambiente.observar() == EventoJogo.TERMINAR):
                break
            self.__personagem.executar()
            self.__personagem.mostrar()
            

# Executar jogo
if (__name__ == "__main__"):
    Jogo().executar()
