from abc import abstractmethod

class Estado:
    """
    Classe representativa de um estado, uma configuração possível de um problema. Estes abstraem os 
    aspetos estruturais do problema. Cada estado tem a sua identificação única.
    """
    def __hash__(self):
        """
        Método interno (estereótipo de identificação única) que retorna identificação única sobre a forma de um valor inteiro.
        O uso de hashable é uma forma de definir uma identificação única do estado em função 
        da sua informação (valor de estado), já que cada estado é único.
        """
        return self.id_valor()
    
    def __eq__(self, objecto):
        """
        Método interno (estereótipo de identificação única) que define a lógica de igualdade, neste caso o método compara se os objetos são
        instâncias da mesma classe (só podem ser iguais caso sejam da mesma classe). Se estes objetos forem iguais, eles têm
        então o mesmo valor de hash.
        """
        if isinstance(objecto, Estado): # se os dois objetos forem insância da mesma classe
            return self.__hash__() == objecto.__hash__() # retorna True se as identificações forem iguais
        else:
            return False

    @abstractmethod
    def id_valor():
        """
        Método responsável por gerar o identificador único .
        """

