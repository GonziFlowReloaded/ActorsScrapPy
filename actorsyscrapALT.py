from actors import ActorUno, ActorDos
from scrapping import ryr_precioYnombre_inpar, ryr_precioYnombre_par

if __name__ == '__main__':
    actor1 = ActorUno.start()
    actor2 = ActorDos.start()

    actor1.tell(ryr_precioYnombre_inpar)
    actor2.tell(ryr_precioYnombre_par)

    actor1.stop()
    actor2.stop()
