from sae.ambiente.elemento import Elemento

class MecDelib: 
    """
    O MacDelib gera os objetivos que devem ser alcançados relativos aos agentes 
    deliberativos.
    """
    def __init__(self, modelo_mundo):
        self.__modelo_mundo = modelo_mundo

    def deliberar(self):
        """
        O método retorna uma lista de estados do agente
        """
        self.objetivos = self._gerar_objetivos() # todos os objetivos possíveis
        if self.objetivos is not None: # verifica se há objetivos
            return self._selecionar_objetivos(self.objetivos) # se existir objetivos, seleciona os objetivos

    def _gerar_objetivos(self):
        """
        O método gera todos os objetivos possíveis e retorna uma 
        lista de estados do agente que tenham o elemento 'ALVO'.
        """
        return [estado for estado in self.__modelo_mundo.obter_estados() if self.__modelo_mundo.obter_elemento(estado) == Elemento.ALVO]

    def _selecionar_objetivos(self, objetivos):
        """
        O método filtra os objetivos gerando uma lista de estados de agente. O critério de seleção é o objetivo 
        vai ser recolher o objetivo mais próximo com o método distancia() do modelo do mundo.

        Para isto é necessário através da lista de objetivos, que contém os estados do agente, guardar a distãncia
        do estado atual para o sucessor em cada um dos estados, e ordena os estados baseado na distância. A ordenação 
        facilita a extração do estado mais próximo.
        """
        objetivos.sort(key=self.__modelo_mundo.distancia) # o método sort vai guardar todas as distâncias e ordenar a lista conforme a distância
        return [objetivos[:1]] # retorna o primeiro elemento da lista através do slice