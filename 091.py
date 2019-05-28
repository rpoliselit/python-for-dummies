"""
Make a program that reads name, birth year
(register the age), work permit, and register
them in a dictionary. Whether work permit is
different from zero, the dictionary gets
year of hiring, amd wage. Calculate the
retirement age and add it to dictionary.
"""

from datetime import datetime

person = {}
person['name'] = str(input("Name: ")).strip().title()
birth = int(input('Birth year: '))
person['age'] = datetime.now().year - birth
person['work permit'] = int(input('Work permit number (0 none): '))
if person['work permit'] != 0:
    person['year of hiring'] = int(input('Year of hiring: '))
    person['wage'] = float(input('Wage: US$'))
    person['retirement age'] = (person['year of hiring'] + 35) - birth
print('*'*40)
for k , v in person.items():
    print(f'{k.title()}: {v}')
