import itertools

# teams = ['Best-ever', 'Not-so-good', 'Amateurs']

for i in itertools.combinations(teams, 2):
    print(i)