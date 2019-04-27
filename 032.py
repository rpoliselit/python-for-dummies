"""
Make a program that identifies leap years.
"""
c = {'cl' : '\33[m', 'w' : '\33[1;37m'}

from datetime import date

year = int(input('Enter a year or 0 for current year.\n'.format()))
leap_year = False

if year == 0:
    year = date.today().year
if (year % 4 == 0 and year % 100 != 0) or (year %400 == 0):
    leap_year = True

print('-'*20)
print('Is {}{}{} a leap year?\n{}{}{}!'.format(c['w'],year,c['cl'],c['w'],leap_year,c['cl']))
