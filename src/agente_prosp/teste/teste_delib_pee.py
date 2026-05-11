from plan.plan_pee.planeador_pee import PlaneadorPEE
from agente_prosp.controlo_delib.controlo_delib import ControloDelib
from agente_prosp.agente_prosp import AgenteProsp
from sae import Simulador 

"""

"""

if __name__== "__main__": # verificar se o ficheiro é executável
    # Instância do planeador de procura de espaço de estados
    planeador = PlaneadorPEE()
    # Instância do controlo deliberativo que recebe um planeador
    controlo = ControloDelib(planeador)
    # InstÂncia do agente prospetor que recebe um controlo
    agente = AgenteProsp(controlo) 
    simulador = Simulador(1, agente, vista_modelo=True) # de acordo com a documentação os parâmetros adequados serão estes
    simulador.executar() # documentação infrma que é necessário esta linha para a execução