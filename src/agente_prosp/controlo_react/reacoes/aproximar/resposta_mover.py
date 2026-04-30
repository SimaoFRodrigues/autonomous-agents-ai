from ecr.resposta import Resposta

from agente_prosp.accoes.mover import Mover

class RespostaMover(Resposta):
    """Esta classe gera a resposta Mover(), e apenas é necessário invocar o construtor da classe Resposta, 
    que recebe uma Ação como parâmetro, neste caso uma instância Mover() que recebe como parâmetro a 
    direção recebida como parâmetro nesta classe(neste caso, None). 
    
    Esta classe é outro bom exemplo de reutilização de classes e acoplamento, um conceito da programação orientada a objetos.
    """
    def __init__(self, direcao=None):
        super().__init__(Mover(direcao))
    