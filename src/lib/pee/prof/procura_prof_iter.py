from .procura_prof_lim import ProcuraProfLim

"""
Classe que especializa a procura em profundidade, sendo esta uma procura iterativa. Este tipo de
procura é ótima e completa, ao contrário dos outros tipos de procura em profundidade.
Esta classe herda de ProcuraProfLim e reutiliza o mecanismo de procura em profundidade com limite, 
e esta é um exemplo de polimorfismo, já que redefine a procura sem 'estragar' a interface.
"""
class ProcuraProfIter(ProcuraProfLim):
    def procurar(self, problema, inc_prof=1, limite_prof=100):
        """
        Método responsável pela procura em profundidade iterativa. Este processo vai procurar em 
        profundidade com o limite de profundidade atual para o limite de profundidade crescente, 
        e se exitir solução retorna-a. Este método usa repetidamente o método ProcuraProfLim.procurar,
        delegando a validação do limite e da expansão para a classe base.
        """
        for prof_max in range(0, limite_prof + 1, inc_prof):
            solucao = super().procurar(problema, prof_max)
            if solucao:
                return solucao

