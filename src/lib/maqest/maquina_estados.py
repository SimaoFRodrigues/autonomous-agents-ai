class MaquinaEstados:
    """Implementa uma máquina de estados baseada em transições."""

    def __init__(self, estado_inicial, transicoes):
        """Inicializa a estrutura interna de transições e estado atual.
        """
        self.__estado = estado_inicial
        self.__tte = {}
        self.__tae = {}

        # Transição automática para booleano, contentor vazio é False e um contentor com elementos é True
        if transicoes:
            for transicao in transicoes:
                # operador ternário usa a transição como está se tiver 4 elementos, senão, acrescenta `None` como ação por omissão.
                estado_ant, evento, estado_suc, acao = transicao \
                if len(transicao) == 4 else transicao + (None,) 
                # Destruturação do tuplo da transição em elementos individuais.
                # (None,) cria um novo tuplo para completar transições que não tenham.
                self.definir_transicao(estado_ant, evento, estado_suc, acao)

    @property
    def estado(self):
        return self.__estado

    def definir_transicao(self, estado_ant, evento, estado_suc, acao):
        """Regista uma transição para um par estado-evento.
        """
        self.__tte[(estado_ant, evento)] = estado_suc
        # O is not None não permite que a conversão booleana do if acao atrapalhe a lógica
        if acao is not None:
            self.__tae[(estado_ant, evento)] = acao
    
    def processar(self, evento):
        """
        Processa um evento e aplica a transição correspondente.
        Este método começa por obter a ação a partir da tabela da ação de estado com a chave 'estado_atual'
        e 'evento'. Depois obtém o novo estado a partir da tabela de transição de estado com a mesma chave 
        e no fim se esse novo estado existir faz se a transicao de estado, e no fim é retornada a ação.
        """
        acao = self.__tae.get((self.__estado, evento))
        novo_estado = self.__tte.get((self.__estado, evento))
        #Aqui acontece a transição de estado
        if novo_estado is not None:
            self.__estado = novo_estado
        return acao
    