from ecr.resposta import Resposta

from agente_prosp.accoes.rodar import Rodar

class RespostaEvitar(Resposta):
    """
    Esta classe define a resposta para situações de obstáculo. RespostaEvitar especializa Resposta para
    devolver uma ação de rotação quando o comportamento de evitar obstáculo é ativado.
    """

    def _obter_accao(self, percepcao):
        """Este método deve rodar em função da direção do agente. Para isso, é guardada a direção
        atual do agente com o atributo .direccao da instância de percepcionar e de seguida sobre 
        isso é atribuido o .rodar() e o método retorna a ação Rodar() com o parâmetro da direção 
        do agente
        """
        dir_agente = percepcao.direccao # o atributo .direccao dá a direccao atual do agente
        dir_resposta = dir_agente.rodar() # o agente roda no sentido dos ponteiros do relógio
        return Rodar(dir_resposta) # roda na direção do agente