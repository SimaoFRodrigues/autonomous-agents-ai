from .passo_solucao import PassoSolucao

class Solucao:
    """
    A classe Solução é referente ao caminho da árvore que liga a raíz à folha objetivo
    """
    def __init__(self, no_final):
        self.no_final = no_final
        self.__dimensao = no_final.profundidade
        self.__custo = no_final.custo
        self.__passos = []
        no = no_final
        """
        Cada nó guarda o operador que o gerou e a referência do nó antecessor.
        Para reconstruir um passo da solução o estado do passo tem de ser o estado do antecessor e o
        o operador do passo tem de ser o operador do nó atual. Como a reconstrução começa no nó final 
        e avança para trás, cada passo é inserido no início da lista para manter a ordem da raiz até ao objetivo.
        """
        while no.antecessor:
            passo = PassoSolucao(no.antecessor.estado, no.operador)
            self.__passos.insert(0, passo)
            no = no.antecessor # atualiza o nó para o anterior

    @property
    def dimensao(self):
        return self.__dimensao
    
    @property
    def custo(self):
        return self.__custo
    
    def __iter__(self):
        """
        Método interno (estereótipo de iteração) que deve retornar um objeto iterator (que é quem sabe buscar o próximo valor).
        """
        return iter(self.__passos)


    #def __getitem__(self, index):
        #"""Método interno (estereótipo de iteração) que permite iterar de forma indexável, neste caso não usaremos"""
        #return self.__passos[index]
    
    
