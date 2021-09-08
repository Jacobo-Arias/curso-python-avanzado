my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)

print(next(my_iter))
print(next(my_iter))
print(f"{'-'*50}")

my_iter2 = iter(my_list)

while True:
    try:
        element = next(my_iter2)
        print(element)
    except StopIteration:
        break
