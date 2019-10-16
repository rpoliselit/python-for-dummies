"""
Make a program that reads a number,
and calculate its factorial using
WHILE.
"""
print('{:=^40}'.format(' FACTORIAL '))
num = int(input('\nEnter a number: '))
factor = result = 1
print('\n{}! = '.format(num), end = '')
while factor != num:
    print('{}'.format(factor), end = ' x ')
    factor += 1
    result *= factor
print('{} = {}'.format(factor,result))
