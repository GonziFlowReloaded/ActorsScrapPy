from actors import ActorUno, ActorDos
from scrapping import ryr_nombre, ryr_precio

if __name__ == '__main__':
    actor1 = ActorUno.start()
    actor2 = ActorDos.start()

    actor1.tell(ryr_nombre)
    actor2.tell(ryr_precio)

    actor1.stop()
    actor2.stop()
