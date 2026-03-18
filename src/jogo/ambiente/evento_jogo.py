from enum import Enum

"""Define os eventos que podem ser observados no ambiente do jogo."""
class EventoJogo(Enum):
    """Conjunto fechado de eventos observáveis pelo agente.

    Cada evento representa uma situação do ambiente com significado para a
    tomada de decisão da personagem. O enumerado concentra esses valores num
    único ponto, tornando o modelo mais claro e consistente.
    """
    SILENCIO = "s"
    RUIDO = "r"
    ANIMAL = "a"
    FUGA = "f"
    FOTOGRAFIA = "o"
    TERMINAR = "t"

    def mostrar(self):
        """Mostra no ecrã o nome do evento atualmente observado.

        A apresentação do evento torna explícita a situação recebida pelo
        agente em cada passo do ciclo.
        """
        print(f"\nEvento: {self.name}")