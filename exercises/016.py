"""
Make a program that reads any real number,
and returns its integer part.
"""

#1-using int()
#number = float(input('Enter a real number: \n'))
#print('The integer part of {} is {}.'.format(number, int(number)))

#2-using math.floor()
#from math import floor
#number = float(input('Enter a real number: \n'))
#print('The integer part of {} is {}.'.format(number, floor(number)))

#3-using math.trunc()
from math import trunc
number = float(input('Enter a real number: \n'))
print('The integer part of {} is {}.'.format(number, trunc(number)))
