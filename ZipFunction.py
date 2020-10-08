# In order to loop over 2 or more list together use zip function from itr tools library

names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spider Man', 'Superman', 'Dead Pool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'DC']

for name, hero, universe in zip(names, heroes, universes):
    print(f'{name} is actually {hero} in {universe} world.')

# To print related values in one tuple

for value in zip(names, heroes, universes):
    print(value)

