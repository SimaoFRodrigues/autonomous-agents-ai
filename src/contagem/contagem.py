from mod_prob.heuristica_contagem import HeuristicaContagem
from mod_prob.problema_contagem import ProblemaContagem
from lib.pee.larg.procura_largura import ProcuraLargura
from lib.pee.prof.procura_profundidade import ProcuraProfundidade
from lib.pee.melhor_prim.procura_aa import ProcuraAA
from lib.pee.melhor_prim.procura_sofrega import ProcuraSofrega
from lib.pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from lib.pee.melhor_prim.procura_informada import ProcuraInformada
from lib.pee.prof.procura_prof_iter import ProcuraProfIter
from lib.pee.prof.procura_prof_lim import ProcuraProfLim

"""
Problema de contagem.

O objetivo é partir de um valor inicial, atingir ou superar um valor final,
e escolher entre vários incrementos possíveis. Esta classe é adaptada à interface Problema, 
para que o mecanismo de procura possa reutilizar o mesmo algoritmo em vários domínios.
"""

"""
O bloco abaixo lista de instâncias dos diferentes algoritmos de procura disponíveis 
e vai ser usado para testar o `ProblemaContagem` com estratégias distintas
"""
MECANISMOS_PROCURA = [
    ProcuraProfundidade(),
    ProcuraLargura(),
    ProcuraProfLim(),
    ProcuraProfIter(),
    ProcuraCustoUnif(),
    ProcuraSofrega(),
    ProcuraAA()
]


VALOR_INICIAL = 0
VALOR_FINAL = 8
INCREMENTOS = [1, 2, 3]
INCREM_CICLO = [1, 2, 3, -1] # o -1 cria ciclo no espaço de estados

def teste_contagem(valor_inicial, valor_final, incrementos, mecanismos_procura):
    """
    Este método executa os testes de procura para o problema de contagem.
    Para cada mecanismo de procura, cria um `ProblemaContagem` e chama
    `mec_proc.procurar(problema)`; se o mecanismo for informado, cria e passa
    uma `HeuristicaContagem`.
    Os resultados impressos por mecanismo são alista de incrementos escolhidos, 
    a dimensão da solução e o custo total.
    """

    print()
    print("Valor inicial:", valor_inicial)
    print("Valor final:", valor_final)
    print("Incrementos:", incrementos)

    problema =  ProblemaContagem(valor_inicial, valor_final, incrementos)
    for mec_proc in mecanismos_procura:
        if isinstance(mec_proc, ProcuraInformada):
            heuristica = HeuristicaContagem(valor_final)
            solucao = mec_proc.procurar(problema, heuristica)
        else:
            solucao = mec_proc.procurar(problema)
        print()
        print(mec_proc.__class__.__name__)
        print("Solução: ", [passo.operador.incremento for passo in solucao])
        print("Dimensão: ", solucao.dimensao)
        print("Custo: ", solucao.custo)

###
print("\n---------- Teste de problema sem ciclos ----------")
teste_contagem(VALOR_INICIAL, VALOR_FINAL, INCREMENTOS, MECANISMOS_PROCURA)
print("\n---------- Teste de problema com ciclos ----------")
teste_contagem(VALOR_INICIAL, VALOR_FINAL, INCREM_CICLO, MECANISMOS_PROCURA[1:])