from time import sleep


class FiboIter:
    def __init__(self, max: int = 1597):
        self.max = max

    def __iter__(self):
        self.counter = 0
        self.n1 = 1
        self.n2 = 0
        return self

    def __next__(self):
        if self.n1 + self.n2 <= self.max:
            if self.counter == 0:
                self.counter += 1
                return self.n1
            else:
                self.n2, self.n1 = self.n1, self.n1 + self.n2
                self.counter += 1
                return self.n1

        else:
            raise StopIteration

    def __del__(self):
        print(f"Se hicieron {self.counter} iteraciones")


if __name__ == "__main__":
    fibo = iter(FiboIter())
    while True:
        print(next(fibo))
        sleep(0.1)
