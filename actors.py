from pykka import ThreadingActor



class ActorUno(ThreadingActor):
    def on_receive(self, funcion):
        print(funcion())

class ActorDos(ThreadingActor):
    def on_receive(self, funcion):
        print(funcion())


