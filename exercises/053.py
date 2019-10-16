"""
Create a program that reads the birth
year of seven people, and say how many
have already reached the majority as well as
how many have not reached the age of majority.
"""

from datetime import date

num = int(input('Enter the number of people: '))

adults = 0
kids = 0

for k in range(0,num):
    birth = int(input('{}º Year of birth: '.format(k+1)))
    age = date.today().year - birth
    if age < 21:
        kids += 1
    else:
        adults += 1

print('Number of alduls: {}\nNumber of kids: {}'.format(adults,kids))
