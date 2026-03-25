from agente_prosp.agente_prosp import AgenteProsp
from agente_prosp.controlo_react.controlo_react import ControloReact
from agente_prosp.controlo_react.reacoes.explorar.explorar import Explorar
from sae.simulador import Simulador

"""
Abaixo é criada uma instância de um agente prospetor. AgenteProsp tem no seu construtor um Agente,
e esse Agente tem no seu construtor um Controlo, que será o ControloReact. O ControloReact recebe
o comportamento Explorar e este é responsável por processar as perceções, delegando a decisão ao
comportamento que decide se a ação será rodar ou avançar.
"""

if __name__== "__main__": # verificar se o ficheiro é executável
    # InstÂncia do comportamento responsável por decidir se a ação é rodar ou avançar
    comportamento = Explorar()
    # Instância do controlo que recebe um comportamento e ativa-o
    controlo = ControloReact(comportamento)
    # InstÂncia do agente prospetor que recebe um controlo
    agente = AgenteProsp(controlo) 
    simulador = Simulador(1, agente) # de acordo com a documentação os parâmetros adequados serão estes
    simulador.executar() # documentação infrma que é necessário esta linha para a execução