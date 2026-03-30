from ecr.estimulo import Estimulo

class EstimuloObst(Estimulo):
    """Esta classe implementa a interface Estímulo
    
    A linha abaixo refere-se a uma constante estática (ou seja, não pode ser alterada) definida
    para todas as instâncias da classe EvitarObst(). Esta constante serve para leitura, se for 
    instanciada o Python cria automaticamente uma cópia"""
    INTENS_OBST = 1 

    def detectar(self, percepcao):
        """
        O método detectar() recebe uma instância da classe percepção e permite detectar se há 
        algum obstáculo no caminho do agente. Para este efeito usamos o atributo .contacto_obst() 
        da instância de percepcionar para verificar se há ou não contacto com o obstáculo. Se houver
        contacto, retorna a constante de intensidade, senão retorna 0
        """
        return self.INTENS_OBST if percepcao.contacto_obst() else 0.0