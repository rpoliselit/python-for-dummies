"""
Develop a program that read the first term
and the commun diference for an arithmetic
progression, and returns on console the
first ten term of this PA.

USE 'WHILE' INSTEAD 'FOR'
"""

ai = a0 = float(input('First term of PA: '))
d = float(input('Commun difference of PA: '))

print('The first ten terms are: ', end = '')

while ai != a0 + 9*d:
    print('{}'. format(ai), end = ', ')
    ai += d
print('{}.'.format(ai))
