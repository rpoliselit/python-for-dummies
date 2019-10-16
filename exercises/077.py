"""
Make a program that reads five numerical
values, and save them as a list.
Show max and min typed values as well as
their repective positions.
"""

num = []

for n in range(5):
    num.append(float(input(f'Enter number of {n} position: ')))

print(f'\nYour list: {num}')
print(f'Maximum value {max(num)} is at positions', end = ' ')
for pos, n in enumerate(num):
    if n == max(num):
        print(f'{pos}', end='... ')
print(f'\nMinimum value {min(num)} is at positions', end=' ')
for pos, n in enumerate(num):
    if n == min(num):
        print(f'{pos}', end = '... ')
print('')
