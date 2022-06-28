def my_gen():
    """Un ejemplo de generadores"""

    print("Hello wordl")
    n = 0
    yield n

    print("Hello heaven")
    n = 1
    yield n

    print("Hello space")
    n = 2
    yield n


a = my_gen()
print(next(a))
print("-" * 10)
print(next(a))
print("-" * 10)
print(next(a))
# print("-"*10)
# print(next(a))


print("---" * 10 + "\n")


my_list = [1, 2, 3, 4, 5, 6]

my_second_list = [x ** 2 for x in my_list]  # List comprehension
my_second_gen = (x ** 2 for x in my_list)  # Generator expression

print(type(my_second_list))
print(type(my_second_gen))
