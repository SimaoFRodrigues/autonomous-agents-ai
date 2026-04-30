from pee.mec_proc.fronteira import Fronteira

"""
Fronteira LIFO (Last In, First Out) significa que os últimos elementos a entrar são os primeiros
a sair, como por exemplo uma pilha.
Esta classe usa a interface abstrata Fronteira para a procura em profundidade e é usada por 
ProcuraProfundidade através da composição no construtor da classe de procura.
"""
class FronteiraLIFO(Fronteira):

    def inserir(self, no):
        """
        Para inserir elementos quando a fronteira é LIFO, colocamos o nó no ínicio (posição 0) da lista.
        """
        self._nos.insert(0, no)