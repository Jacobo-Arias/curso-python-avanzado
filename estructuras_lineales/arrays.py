from functools import reduce
from random import randint

class Array():

    def __init__(self, capacity, fill_value = None) -> None:
        self.items = list()
        for _ in range(capacity):
            self.items.append(fill_value)
    
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __iter__(self):
        return iter(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, element):
        self.items[index] = element

class Array2():

    def __init__(self, capacity, fill_value = None) -> None:
        self.items = list()
        for _ in range(capacity):
            self.items.append(fill_value)
    
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __iter__(self):
        return iter(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, element):
        self.items[index] = element
    
    def __randfill__(self):
        for i in range(self.__len__()):
            self.__setitem__(i,randint(0,10))
        # print(self.items)

    def __sum__(self):
        tipo = type(self.__getitem__(0))
        tipos = [type(t) == tipo for t in self.items]
        if all(tipos):
            return reduce(lambda a,b: a+b,self.items)
        else:
            raise TypeError("Todos los elementos deben ser int o str")

def main():
    from arrays import Array2, Array

    menu = Array2(4,4)
    print(menu)
    # menu.__randfill__()
    print(menu.__sum__())

if __name__ == "__main__":
    main()