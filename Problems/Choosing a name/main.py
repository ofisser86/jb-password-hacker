from itertools import product

# first_names = ['Anna', 'Catarina']
# middle_names = ['Luisa', 'Maria']

for i in product(first_names, middle_names):
    print(*i)