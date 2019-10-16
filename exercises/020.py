"""
A teacher wants to sort the seminars order of four students,
make a program that helps him by reading the name of students,
and returns a random order of them.
"""
from random import shuffle

name_list = []
number_of_student = int(input('Enter the number of students: '))
for i in range(number_of_student):
    name_list.append(input('Enter name of {}sº student: '.format(i+1)))

print('The original list:',(number_of_student*'\n{}').format(*name_list))

shuffle(name_list)
print('The order of seminars is:',(number_of_student*'\n{}').format(*name_list))
