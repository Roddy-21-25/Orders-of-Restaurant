from collections import deque
import time

class Queue():
    def __init__(self):
        self.invoce = deque()
        self.tiempo_inicio = time.time()

    def add_food(self, val):
        for idx ,food in enumerate(val):
            time.sleep(1)
            self.invoce.appendleft(food)
            print(f"Orden numero:  #{idx + 1} : {val[idx].upper()} [ACEPTADA]\n")

        time.sleep(1.5)
        print(f"las ordenes: {val} han sido ACEPTADAS!!!\n")

        tiempo_fin = time.time()
        tiempo_transcurrido = tiempo_fin - self.tiempo_inicio
        print(f"el tiempo que tomo en procesar la ordenes, es de: {int(tiempo_transcurrido)} segundos\n")

    def serve_food(self, val):
        print("---------------------",
              "the order is loading",
              "---------------------\n")
        time.sleep(1)
        for idx, food in enumerate(val):
            time.sleep(2)
            print("-------------------------\n",
                  f"ORDEN NUMERO: {idx + 1} : {food}\n",
                  "-------------------------\n")
        print("Su orden ha sido Entregada")

orders = ['pizza','samosa','pasta','biryani','hamburguesa']

o = Queue()
# add to invoce
o.add_food(orders)
# server food
o.serve_food(o.invoce)






