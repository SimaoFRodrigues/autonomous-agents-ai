from agente_prosp.agente_prosp import AgenteProsp
from agente_prosp.controlo_react.controlo_react import ControloReact
from agente_prosp.controlo_react.reacoes.explorar.explorar import Explorar

"""
Abaixo é criada uma instância de um agente prospetor. AgenteProsp tem no seu construtor um Agente,
e esse Agente tem no seu construtor um Controlo, que será o ControloReact. O ControloReact recebe
o comportamento Explorar e este é responsável por processar as perceções, delegando a decisão ao
comportamento que decide se a ação será rodar ou avançar.
"""
agente = AgenteProsp(ControloReact(Explorar())) 