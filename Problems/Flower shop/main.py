from itertools import combinations

# flower_names = ['rose', 'tulip', 'sunflower']

for i in range(1, 4):
    for j in combinations(flower_names, i):
        print(j)

