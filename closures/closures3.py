def make_repeater_of(n: int):
    def repeater(string: str):
        assert type(string) == str, "Solo puedes ingresar cadenas"
        return string * n

    return repeater


def run():
    repeater_5 = make_repeater_of(5)
    print(repeater_5("hola"))
    repeter_10 = make_repeater_of(10)
    print(repeter_10("Jacobo "))


if __name__ == "__main__":
    run()
