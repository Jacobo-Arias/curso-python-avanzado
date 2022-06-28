"""
reglas para encontrar un closure

1. debemos tener una nested function
2. la nested function debe referenciar un valor de un scope superior
3. la función que envuelve la nested debe retornarla también
"""


def main():

    a = 1

    def nested():
        print(a)

    return nested


my_func = main()
my_func()

del main

my_func()

"""
la salida es 
1
1
porque una closure es cuando una función anidada (nested) 
recuerda el estado de una variable de un scope superior
"""
