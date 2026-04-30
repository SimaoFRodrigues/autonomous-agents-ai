from .mecanismo_procura import MecanismoProcura

"""
Especialização de MecanismoProcura para procura em grafo.
Esta classe reutiliza a estrutura da superclasse para gerir a fronteira e ciclo de procura e 
acrescenta memória de estados explorados para evitar revisitar nós.
"""
class ProcuraGrafo(MecanismoProcura):
    def _iniciar_memoria(self):
        """
        Este método protegido inicia a fronteira de exploração e o dicionário 
        com os nós explorados.
        """
        super()._iniciar_memoria() 
        self._explorados = {}

    def _memorizar(self, no):
        """
        O método memorizar acrescenta apenas uma validação que verifica se o nó
        deve ou não ser mantido, e se sim invoca a classe memorizar da classe base.
        Este método usa polimorfismo porque complementa a implementação da superclasse 
        em vez de a substituir completamente.
        """
        if self._manter(no): # Se for para manter o nó
            self._explorados[no.estado] = no # atualizamos os explorados no índice do estado do no, com o proprio nó
            super()._memorizar(no) # memorizar com o que já foi feito no MecansimoProcura

    def _manter(self, no):
        """
        Este método retorna True se o nó nesse estado não tiver sido explorado e 
        False se já tiver sido explorado.
        """
        return no.estado not in self._explorados
