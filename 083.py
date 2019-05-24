"""
Make a program that reads name and weight
of several people, and saves in a list.
Show:
1 - Amount of registered people
2 - heavier people
3 - lighter people
"""

people, data = [] , []
heavier = lighter = 0

while True:
    data.append(str(input('Name: ')).strip())
    data.append(float(input('Weight [Kg]: ')))
    people.append(data[:])
    data.clear()
    ans = str(input('Continue? [Y/N]')).strip().lower()[0]
    if ans == 'n':
        break

for k in people:
    if k[1] > heavier or heavier == 0:
        heavier = k[1]
    if k[1] < lighter or lighter == 0:
        lighter = k[1]

print(f'Number of people: {len(people)}.')
print(f'Heavier weight is {heavier}Kg of ', end = '')
for k in people:
    if k[1] == heavier:
        print(f'{k[0]}', end = ', ')
print(f'\nLighter weight is {lighter}Kg of ', end = '')
for k in people:
    if k[1] == lighter:
        print(f'{k[0]}', end = ', ')
print('')
