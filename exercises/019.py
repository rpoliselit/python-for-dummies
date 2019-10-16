"""
One pie is raffled between four people.
Make a program that helps by reading the name of them,
and returns the chossen one.
"""

from random import choice

name_list = []
number_of_people = int(input('Enter the number of people: '))
for i in range(number_of_people):
    name_list.append(input('Enter the {}º name: '.format(i+1)))

#print('The winner is {}.'.format(names[randint(0, number_of_people-1)]))
print('The winner is {}.'.format(choice(name_list)))
