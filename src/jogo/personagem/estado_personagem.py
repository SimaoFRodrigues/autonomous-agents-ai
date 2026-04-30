from enum import Enum
class EstadoPersonagem(Enum):
    """Conjunto dos estados possíveis da personagem.

    Estes estados representam as fases internas do comportamento da personagem ao longo do jogo. 
    São usados pela máquina de estados para controlar a evolução da decisão."""

    PROCURA = 1
    INSPECAO = 2
    OBSERVACAO = 3
    REGISTO = 4
