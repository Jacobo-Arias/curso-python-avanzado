def divisor(num):
    assert num >= 0, "Debe ingresar un número mayor a cero"
    divisors = [x for x in range(1, num + 1) if num % x == 0]
    return divisors


def run():
    num = input(f"Ingresa un número: ")
    assert num.isnumeric(), "Debes ingresar un número"
    print(divisor(int(num)))
    print("termino mi programa")


if __name__ == "__main__":
    run()
