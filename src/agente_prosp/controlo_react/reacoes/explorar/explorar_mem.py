from agente_prosp.accoes.avancar import Avancar

class ExplorarMem:
    """
    A classe tem como objetivo explorar recorrendo ao estado interno (memória) que 
    deverá estar, de acordo com a hierarquia de comportamentos do agente, entre EvitarObst
    e Explorar. O ExplorarMem serve como resolução do problema do comportamento Explorar(),
    resolvendo problemas de agentes sem memória, já que neste momento é capaz de produzir
    qualquer tipo de comportamento, é atualizado temporalmente e é mais capaz de evitar falhas.
    """
    def __init__(self, dim_max_mem=100):
        """
        Construtor da classe onde são criadas variáveis privadas, o tamanho da memória
        é criado inicialmente com o valor inteiro de 100 e uma lista vazia 
        que representa a memória
        """
        self.__dim_max_mem = dim_max_mem
        self.__memoria = []

    def activar(self, percepcao):
        """
        O seguinte método cria um tuplo que guarda a posição e a direção do agente, se essa 
        informação já existir em memória, o explorar com memória nao retorna nada, se ainda não 
        existir guarda esses valores na memória. De seguida, verifica se a memória já chegou ao
        limite, se chegar retira o elemento mais antigo, senão apenas avança.
        """
        atual = [percepcao.posicao, percepcao.direccao] # Obtem a situação atual
        if not atual in self.__memoria: # se não tiver em memória
            self.__memoria.append(atual) # adiciona à memória
            if len(self.__memoria) > self.__dim_max_mem: # verifica se já chegou ao tamanho máximo
                self.__memoria.pop(0) # retira o elemento mais antigo da lista
            return Avancar() # avança