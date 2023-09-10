import multiprocessing

def funcion_1():
    print("Función 1 ejecutándose")

def funcion_2():
    print("Función 2 ejecutándose")

if __name__ == "__main__":
    # Crear dos procesos, uno para cada función
    proceso1 = multiprocessing.Process(target=funcion_1)
    proceso2 = multiprocessing.Process(target=funcion_2)
    
    # Iniciar los procesos
    proceso1.start()
    proceso2.start()
    
    # Esperar a que ambos procesos terminen
    proceso1.join()
    proceso2.join()
    
    print("Ambos procesos han terminado")