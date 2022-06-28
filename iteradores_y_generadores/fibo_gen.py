from time import sleep


def fibo_gen(max: int = 1597):
    n1 = 1
    n2 = 0
    counter = 0

    while True:
        if n1 + n2 <= max:
            if counter == 0:
                counter += 1
                yield n1
            else:
                counter += 1
                n2, n1 = n1, n1 + n2
                yield n1
        else:
            raise StopIteration


if __name__ == "__main__":
    fibo = fibo_gen(25)
    while True:
        print(next(fibo))
        sleep(0.1)
