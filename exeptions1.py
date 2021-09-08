def divisor(num):
    try:
        if num <= 0:
            raise ValueError("Debe ingresar un mayor que cero")
        divisors = [x for x in range(1, num + 1) if num % x == 0]
        return divisors
    except ValueError as e:
        print(e)
        return f"{num} es menor que 0"


def run():
    try:
        num = int(input(f"Ingresa un número: "))
        print(divisor(num))
        print("termino mi programa")
    except ValueError as e:
        print("Debe ingresar un número")


if __name__ == "__main__":
    run()
