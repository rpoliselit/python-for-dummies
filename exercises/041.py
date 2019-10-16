"""
A national swimming confederation needs
a program that reads an athlete's birth year,
and shows its category according to age:
< 9 years: Mirim
< 14 years: Infant
< 19 years: junior
< 20 years: senior
> 20 years: master
"""

import datetime

print('Which is your category?')
year = int(input('Enter your year of birth: '))
age = datetime.date.today().year - year

print('The athlete is {} years old.\nClassified to '.format(age), end ='')

if age <= 9:
    print('Mirim.'.upper())
elif 9 < age <= 14:
    print('Infant.'.upper())
elif 14 < age <= 19:
    print('Junior.'.upper())
elif age == 20:
    print('Senior.'.upper())
else:
    print('Master.'.upper())
