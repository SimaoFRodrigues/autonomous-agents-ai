from mod.problema import Problema

class ProblemaPlan(Problema):
    """
    Esta classe utiliza a interface Problema, podendo assim apenas declarar os métodos diferentes 
    da classe original, especializando para o que é desejado. Neste caso, é apenas criado o construtor 
    e os objetivos.
    """

    def __init__(self, modelo_plan, estado_final):
        super().__init__(modelo_plan.obter_estado(), modelo_plan.obter_operadores()) # a assinatura do estado inicial e operadores são declaradas
        self.__estado_final = estado_final

    def objetivo(self, estado):
        """Retorna um valor booleano"""