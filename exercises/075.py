"""
166/5000
Make a program that has a unique tuple
containing items and their respective
prices in sequence. Show a price list
by arranging the data tabularly.
"""

itens = ('Sword', 53.2, 'Brave Sword', 87.3, 'Dagger', 22.54, 'Staff', 31.50, \
         'Bow', 45.69, 'Hammer', 199.90, 'Axe', 45.32, 'Shield', 31.30, \
         'Massamune', 3599.99, 'Holy Moonlight Sword', 23999.99)

print('-'*50)
print(f"{' WEAPON SHOP ':*^50}")
print('-'*50)
for item in itens:
    if type(item) == str:
        print(f"{item:.<40}$", end = ' ')
    else:
        print(f'{item:8.2f}')
print('-'*50)
