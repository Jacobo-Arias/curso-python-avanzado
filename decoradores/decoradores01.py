def decorador(func):
    def envoltura():
        print("Esta es una funcionalidad añadida")
        func()

    return envoltura


def saludo():
    print("Hola Mundo")


saludo()
# Hola Mundo

saludo = decorador(saludo)
saludo()
# Esta es una funcionalidad añadida
# Hola Mundo

print("\n")
##############################################


def decorador2(func):
    def envoltura():
        print("Esta es una funcionalidad añadida")
        func()

    return envoltura


@decorador2
def saludo2():
    print("Hola Mundo")


saludo()
# Hola Mundo

# Esta es una funcionalidad añadida
# Hola Mundo
