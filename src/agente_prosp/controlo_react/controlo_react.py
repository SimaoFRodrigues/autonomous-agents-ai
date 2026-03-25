from agente.controlo import Controlo

class ControloReact(Controlo):
    """
    Um controlo reativo é um controlo que pertence ao agente reativo
    em que as percepcoes são processadas consoante o comportamento, esse
    comportamento pode ser contituído por sub-comportamentos.
    """
    def __init__(self, comportamento):
        self.__comportamento = comportamento
    
    def processar(self, percepcao):
        """
        Este código refere se a um passo do comportamento do agente em que é 
        recebida uma percepacao usada para ativar o comportamento, esse comportamento 
        é processado e retorna uma ação que vai ser retornada por este método.
        """
        
        return self.__comportamento.activar(percepcao) # vai retornar a ação