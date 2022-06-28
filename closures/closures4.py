def make_divider_of(n: int):
    assert type(n) == int, "Debe ingresar numeros"
    assert n == 0, "No se puede dividir por cero"

    def divisor(m: int) -> float:
        assert type(m) == int, "Debe ingresar solo numeros"
        return m / n

    return divisor


def run():
    divider_by_3 = make_divider_of(3)
    print(divider_by_3(18))
    divider_by_5 = make_divider_of(5)
    print(divider_by_5(100))
    divider_by_18 = make_divider_of(18)
    print(divider_by_18(54))


if __name__ == "__main__":
    run()
