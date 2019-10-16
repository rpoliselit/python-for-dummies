"""
Develop a program that read the first term
and the commun diference for an arithmetic
progression, and returns on console the
first ten term of this PA.

USE 'WHILE' INSTEAD 'FOR'
Ask how many term the user want to show.
"""

ai = a0 = float(input('First term of PA: '))
d = float(input('Commun difference of PA: '))
terms = more = 9
print('The first ten terms are: ', end = '')

while more != 0:
    if (ai == a0 + terms * d) or more == 1:
        print('{}.'.format(ai))
        more = int(input('How many terms do you want more? '))
        terms += more
    else:
        print('{}'. format(ai), end = ', ')
    ai += d
print('END')
