from sae.ambiente.elemento import Elemento

class MecDelib: 
    """
    A classe MecDelib concentra a parte deliberativa que escolhe objetivos a partir do
    modelo interno do mundo.
    Esta classe separa a decisão de alto nivel do resto do comportamento do agente, o que 
    melhora a organizacao do código e facilita a extensão do sistema. O objeto trabalha sobre 
    o modelo do mundo sem expor diretamente os detalhes internos desse modelo.
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
        O método filtra os objetivos gerando uma lista de estados de agente. O critério de seleção é  
        recolher o objetivo mais próximo com o método distancia() do modelo do mundo.
        Para isto é necessário através da lista de objetivos, que contém os estados do agente, guardar 
        a distância do estado atual para o sucessor em cada um dos estados, e ordenar os estados baseado 
        na distância. A ordenação facilita a extração do estado mais próximo.
        """
        objetivos.sort(key=self.__modelo_mundo.distancia) # o método sort vai guardar todas as distâncias e ordenar a lista conforme a distância
        return [objetivos[:1]] # retorna o primeiro elemento da lista através do slice