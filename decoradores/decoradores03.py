from datetime import datetime


def execution_time(func):
    def wrapper(*args, **kwargs):
        inition = datetime.now()
        func(*args, **kwargs)
        final = datetime.now()
        total = final - inition
        print(f"El tiempo que tardó fue de {total.total_seconds()} segundos")

    return wrapper


@execution_time
def random_func():
    for _ in range(10000000):
        pass


@execution_time
def suma(*args, **kwargs) -> int:
    sumatoria = sum(args)
    print(sumatoria)
    return sumatoria


@execution_time
def saludo(nombre="Jacobo"):
    print(f"Hola {nombre}")


if __name__ == "__main__":
    random_func()
    suma(3, 4, 3, 4, 5, 4)
    saludo("Mundo")
