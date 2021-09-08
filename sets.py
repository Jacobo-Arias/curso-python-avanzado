set1 = {1, 2, 3}

set2 = {3, 4, 5}

print(f"Set1: {set1}")
print(f"Set2: {set2}")
print()

# * Union
set3 = set1 | set2
print(f"Union: {set3}")
# set1.union(set2)

# * Interseccion
set4 = set1 & set2
print(f"Intercepcion: {set4}")
# set1.intersection(set4)

# * Diferencia
set5 = set1 - set2
print(f"Diferencia :{set5}")
# set1.difference(set2)

# * Diferencia Simétrica
set6 = set1 ^ set2
print(f"Diferencia simetrica: {set6}")
# set1.symmetric_difference(set2)
