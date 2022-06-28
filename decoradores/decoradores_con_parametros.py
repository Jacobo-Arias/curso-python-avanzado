from decoradores03 import execution_time


def decorador_parametro(text):
    def decorador_funcion(func):
        @execution_time
        def wrapper(*args, **kwargs):
            print(f"Este es el print del {text}")
            func(*args, **kwargs)

        return wrapper

    return decorador_funcion


@decorador_parametro("Decorador")
def funcion(funcion):
    print(f"Este es el print de la {funcion}")


if __name__ == "__main__":
    print(f"Este es el print del Main")
    funcion("Funcion")
