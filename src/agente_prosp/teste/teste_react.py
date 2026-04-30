# Neste caso, como este é o modulo teste que está a ser executado, os modulos têm de ser todos o caminho absoluto e não o relativo.
from agente_prosp.agente_prosp import AgenteProsp
from agente_prosp.controlo_react.controlo_react import ControloReact
from agente_prosp.controlo_react.reacoes.recolher.recolher import Recolher
from sae import Simulador 

"""
Abaixo é criada uma instância de um agente prospetor. AgenteProsp tem no seu construtor um Agente,
e esse Agente tem no seu construtor um Controlo, que será o ControloReact. O ControloReact recebe
o comportamento Explorar e este é responsável por processar as perceções, delegando a decisão ao
comportamento que decide se a ação será rodar ou avançar.

Nesta simulação, por vezes o agente fica da cor vermelha. A justificação é que o numero aleatório gerado
na reação explorar é superior à probabilidade rotação (0.7), e como a ação derivada desse comportamento é Avançar(), 
é impossível realizar essa ação porque existe um obstáculo, logo, o agente é obrigado a encontrar outro caminho.

O que se poderá fazer para evitar essas situações?
R: Para evitar isso, temos de implementar tanto o EvitarObstáculos, tanto outras classes de reações no futuro.
"""

if __name__== "__main__": # verificar se o ficheiro é executável
    # Instância do comportamento responsável por decidir se a ação é rodar ou avançar
    comportamento = Recolher()
    # Instância do controlo que recebe um comportamento e ativa-o
    controlo = ControloReact(comportamento)
    # InstÂncia do agente prospetor que recebe um controlo
    agente = AgenteProsp(controlo) 
    simulador = Simulador(1, agente) # de acordo com a documentação os parâmetros adequados serão estes
    simulador.executar() # documentação infrma que é necessário esta linha para a execução