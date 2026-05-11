from plan.plano import Plano

class PlanoPEE(Plano):
    """
    A PlanoPEE é uma classe de plano baseado em procura em espaço de estados, usa a interface Plano e
    escreve os seus métodos abstratos. Aqui é guardada a sequência de passos da solução e definido como 
    obter a próxima ação e como mostrar visualmente o plano.
    """
    def __init__(self, solucao):
        self.__passos = [passo for passo in solucao] # estrutura tem propriedade estado e propriedade operador

    def obter_acao(self, estado):
        """
        Só se pode existir ação se existir passo na lista de passos se existir re temos de confirmar se o estado 
        do passo corresponde ao estado atual, se for igual, indica que o plano esta sincronizado.
        """
        if self.__passos: # se existir passos na lista de passos
            passo = self.__passos.pop(0) # retira o primeiro passo da lista
            if passo == estado: # se o estado correspondente for igual ao atual
                return passo.operador # é retornado o operador do passo

    def mostrar(self, vista):
        """
        O método mostrar vai mostrar os passos (setas visualmente) que representam os operadores.
        A lógica implica perceber se existem passos a realizar, e se houver, são percorridos todos
        da lista e mostrados com as setas na devida posição e direção.
        """
        if self.__passos:
            for passo in self.__passos:
                # mostra visualmente a seta na posição correta e virada para a direção correta.
                vista.mostrar_vetor(passo.estado.posicao, passo.operador.ang)