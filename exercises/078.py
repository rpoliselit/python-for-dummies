"""
Make a program that the user can enter
several numerical values, and register
them in a list. The list cannot contain
repeted values.
Show values in ascending order.
"""

values = []

while True:
    num = input('Enter any number ([s]top): ').strip().lower()
    if 's' in num:
        break
    elif num.isnumeric() == False:
        print(f'This is not a number. Try Again.')
    elif float(num) not in values:
        values.append(float(num))
print('='*30)
print('Ascending order: ', end = '')
for n in sorted(values):
    if n == sorted(values)[-1]:
        print(f'{n}.')
    else:
        print(f'{n}', end = ', ')
