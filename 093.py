"""
Make a program that reads name,
age, and gender of a bunch of
people, and register these data
in a dictionary, and all dictionary
are safe in a list.
Show:
1 - Number of registered people
2 - The mean age of people
3 - A list with all women
4 - A list with an age over the mean one
"""

people = []
person = {}
sum = 0

while True:
    person.clear()
    person['name'] = str(input('Name: ')).strip().title()
    person['age'] = int(input('Age: '))
    while True:
        person['gender'] = str(input('Gender [m/f]: ')).strip().upper()[0]
        if person['gender'] in 'MF':
            break
        print("ERROR! Type only 'm' or 'f'.")
    people.append(person.copy())
    while True:
        ans = str(input('Continue [y/n]: ')).strip()
        if ans in 'YyNn':
            break
        print("ERROR! Type only 'y' or 'n'.")
    if ans in 'Nn':
        break

for p in people:
    sum += p['age']
mean = sum / len(people)

print('-'*40)
print(f'Number of entries: {len(people)} people.')
print(f'Average age: {mean} years old.')
print(f'The women resgistered are: ', end = '')
for p in people:
    if p['gender'] == 'F':
        print(f'{p["name"]}', end = ' ')
print('\nList of people over average age:')
for p in people:
    if p['age'] > mean:
        for k , v in p.items():
            print(f'{k.title()} = {v}', end = ' ; ')
print('')
