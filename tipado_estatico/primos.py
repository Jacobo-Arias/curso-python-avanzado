def is_primo(num: int) -> bool:
    if num < 1:
        raise ValueError("Debe ingresar un número mayor o igual a uno")
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


def run():
    print(is_primo(11))


if __name__ == "__main__":
    run()
