from pykka import ThreadingActor



class ActorUno(ThreadingActor):
    def on_receive(self, funcion: function):
        funcion()

class ActorDos(ThreadingActor):
    def on_receive(self, funcion: function):
        funcion()


