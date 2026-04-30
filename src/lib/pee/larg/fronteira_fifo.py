from lib.pee.mec_proc.fronteira import Fronteira

"""
Fronteira FIFO (First In, First Out) significa que os primeiros elementos a entrar são os primeiros
a sair, como por exemplo uma fila.
"""
class FronteiraFIFO(Fronteira):

    def inserir(self, no):
        """
        Para inserir elementos quando a fronteira é FIFO, colocamos o nó no fim da lista.
        """
        self._nos.append(no)