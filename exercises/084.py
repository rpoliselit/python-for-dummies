"""
Make a program that the user type
seven numerical values, and register
them a list. This one must keep
even and odd values separated.
Show both values in ascending order.
"""

numbers = [ [] , [] ]

for k in range(7):
    value = int(input(f'{k+1}º integer number: '))
    if value % 2 == 0:
        numbers[0].append(value)
    else:
        numbers[1].append(value)


print(f'Even numbers: {sorted(numbers[0])}')
print(f'Odd numbers: {sorted(numbers[1])}')
