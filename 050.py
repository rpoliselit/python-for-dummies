"""
Develop a program that read the first term
and the commun diference for an arithmetic
progression, and returns on console the
first ten term of this PA.
"""

a0 = float(input('First term of PA: '))
d = float(input('Commun difference of PA: '))

print('The first ten terms are: ', end = '')

for k in range(0,10):
    ai = a0 + k*d
    if k == 9:
        print('{}'.format(ai), end = '.\n')
    else:
        print('{}'.format(ai),end = ', ')
