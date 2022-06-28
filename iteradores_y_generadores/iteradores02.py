class NumerosPares:

    """Clase que implementa un iterador
    de todos los números pares, o los
    números pares hasta un maximo
    """

    def __init__(self, max: int = None):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if not self.max or self.num <= self.max:
            result = self.num
            self.num += 2
            return result
        else:
            raise StopIteration

    def __del__(self):
        print(self.num)
        print("Adios")


my_iter = iter(NumerosPares())
for i in range(30):
    print(next(my_iter))


# my_iter2 = NumerosPares().__iter__()

# for i in range(10):
#     print(my_iter2.__next__())
