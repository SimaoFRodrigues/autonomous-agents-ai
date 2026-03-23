from ecr.comport_comp import ComportComp
class Hierarquia(ComportComp):
    """
    A hierarquia é um comportamento composto de seleção de ação, em que os comportamentos
    estão organixados numa hierarquia fixa de subsunção. Nessa situação é preciso definir hierarquia para 
    escolher apenas uma ação final. É precisamente aqui que entra o polimorfismo: o `ComportComp` pode invocar
    `selecionar_acao` sem saber se a decisão está a ser feita por hierarquia, por prioridade ou por outro
    critério qualquer. Desde que a subclasse respeite, o resto do sistema funciona da mesma forma.
    """

    def selecionar_acao(self, accoes):
        """Seleciona uma ação a partir de uma lista hierárquica dada como parâmetro.

        A implementação deste método vai analisar o conjunto de ações disponíveis e 
        devolver a ação cujo nível hierárquico tem maior precedência no contexto atual, 
        nescte caso o primeiro elemento da lista de ações. 
        """
        if accoes:
            return accoes[0]
        else:
            return None

