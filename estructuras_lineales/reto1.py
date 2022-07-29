from arrays import Array2
from linked_list import SingleLinkedList
import time

lista = Array2(capacity=20000)
lista.__randfill__()

# print(lista)

linked_list = SingleLinkedList()
for item in lista:
    linked_list.append(item)


t1 = time.time()
for item in lista:
    print(item,end=" ")
t2 = time.time()
print(f"\n-------{t2-t1}-------")

t1 = time.time()
for item in linked_list.iter():
    print(item,end=" ")
t2 = time.time()
print(f"\n-------{t2-t1}-------")


# * Conclusión: Es más rapido de la segunda forma, la "manual"
# * si bien la diferencia son centesimas de segundos 
# * se recomienda usar cuando los nodos no sean números sino elementos más complejos
