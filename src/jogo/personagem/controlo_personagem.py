from agente.acao_jogo import AcaoJogo
from ambiente.comando_jogo import ComandoJogo
from ambiente.evento_jogo import EventoJogo
from maqest.maquina_estados import MaquinaEstados
from agente.controlo import Controlo
from .estado_personagem import EstadoPersonagem

class ControloPersonagem:
    """Implementa o mecanismo de decisão da personagem.

    Esta classe recebe a perceção atual do ambiente e, com base numa máquina
    de estados finitos, determina a ação mais adequada para a situação.

    O controlo é responsável por manter a coerência temporal do comportamento
    da personagem, garantindo que a ação escolhida depende não só do evento
    atual, mas também do estado interno em que a personagem se encontra.
    """

    def __init__(self):
        """Cria a instância de controlo associada à personagem.

        Durante a inicialização são construídas as ações possíveis e definida
        a máquina de estados que modela o comportamento global da personagem.
        """
        super().__init__()
        
        # Define as ações disponíveis no domínio do jogo.
        procurar = AcaoJogo(ComandoJogo.PROCURAR) 
        aproximar = AcaoJogo(ComandoJogo.APROXIMAR)  
        observar = AcaoJogo(ComandoJogo.OBSERVAR) 
        fotografar = AcaoJogo(ComandoJogo.FOTOGRAFAR)  

        # Define a máquina de estados que regula a evolução do comportamento.
        # Cada transição associa um evento a um novo estado e, quando aplicável,
        # à ação que deve ser executada nessa transição.
        self.__maqest = MaquinaEstados(
            EstadoPersonagem.PROCURA,  # Estado inicial
            [
                (EstadoPersonagem.PROCURA, EventoJogo.ANIMAL, EstadoPersonagem.OBSERVACAO, aproximar),
                (EstadoPersonagem.PROCURA, EventoJogo.RUIDO, EstadoPersonagem.INSPECAO, aproximar),
                (EstadoPersonagem.PROCURA, EventoJogo.SILENCIO, EstadoPersonagem.PROCURA, procurar),
                (EstadoPersonagem.INSPECAO, EventoJogo.SILENCIO, EstadoPersonagem.PROCURA),
                (EstadoPersonagem.INSPECAO, EventoJogo.ANIMAL, EstadoPersonagem.OBSERVACAO, aproximar),
                (EstadoPersonagem.INSPECAO, EventoJogo.RUIDO, EstadoPersonagem.INSPECAO, procurar),
                (EstadoPersonagem.OBSERVACAO, EventoJogo.FUGA, EstadoPersonagem.INSPECAO),
                (EstadoPersonagem.OBSERVACAO, EventoJogo.ANIMAL, EstadoPersonagem.REGISTO, observar),
                (EstadoPersonagem.REGISTO, EventoJogo.FUGA, EstadoPersonagem.PROCURA),
                (EstadoPersonagem.REGISTO, EventoJogo.FOTOGRAFIA, EstadoPersonagem.PROCURA),
                (EstadoPersonagem.REGISTO, EventoJogo.ANIMAL, EstadoPersonagem.REGISTO, fotografar)
            ]
        )

    def processar(self, percepcao):
        """Processa uma perceção e determina a ação adequada.
        O método extrai o evento observado da perceção e delega na máquina de estados a decisão da transição
        e da ação resultante. A lógica de controlo fica, assim, concentrada num modelo explícito de estados.
        """
        evento = percepcao.evento
        return self.__maqest.processar(evento)
    
    @property
    def estado(self):
        """Expõe o estado atual da máquina de estados da personagem."""
        return self.__maqest.estado
    