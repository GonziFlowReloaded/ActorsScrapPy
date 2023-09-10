from actors import ActorUno, ActorDos
from scrapping import ryr_precioYnombre_inpar, ryr_precioYnombre_par
import multiprocessing as mp
import time

def iniciar_actor1():
    actor1 = ActorUno.start()
    actor1.tell(ryr_precioYnombre_inpar)
    actor1.stop()
    
def iniciar_actor2():
    actor2 = ActorDos.start()
    actor2.tell(ryr_precioYnombre_par)
    actor2.stop()

if __name__ == '__main__':
    p1 = mp.Process(target=iniciar_actor1)
    p2 = mp.Process(target=iniciar_actor2)
    
    p1.start()
    p2.start()
    
    # Obtenemos los PID de los procesos después de iniciarlos
    pid1 = p1.pid
    pid2 = p2.pid
    
    p1.join()
    p2.join()
    
    print(f"PID del proceso 1: {pid1}")
    print(f"PID del proceso 2: {pid2}")
