class Hierarquia:
    """Representa uma estratégia hierárquica de seleção de ações.

    No contexto deste trabalho, quando um comportamento composto ativa vários
    comportamentos internos, podem surgir várias ações ao mesmo
    tempo. Nessa situação é preciso definir hierarquia para escolher apenas uma ação final.
    É precisamente aqui que entra o polimorfismo: o `ComportComp` pode invocar `selecionar_acao`
    sem saber se a decisão está a ser feita por hierarquia, por prioridade ou por outro
    critério qualquer. Desde que a subclasse respeite, o resto do sistema funciona da mesma forma.

    Esta separação é importante na arquitetura do trabalho porque isola a decisão do mecanismo de ativação dos comportamentos. 
    Os comportamentos produzem ações, a classe de seleção decide qual dessas ações prevalece.
    """

    def selecionar_acao(self, accoes):
        """Seleciona uma ação a partir de uma lista hierárquica.

        A implementação deste método deve analisar o conjunto de
        ações disponíveis e devolver a ação cujo nível hierárquico tem maior
        precedência no contexto atual. 
        """
        # Este método deve retornar uma ação. `accoes` representa a lista de
        # ações produzidas pelos comportamentos ativos.
        raise NotImplementedError