"""
Make a program that reads several values
and registers in a list.

Make other list with even numbers and
another one with odd numbers.

Show all lists.
"""

numbers, even, odd = [], [], []

while True:
    num = input('Enter any number ['' stops]: ').strip().lower()
    if num.isalnum() == False:
        break
    elif num.isnumeric() == False:
        print('Try again. This is not a number.')
    elif int(num) not in numbers:
        numbers.append(int(num))

for n in numbers:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print(f'All numbers: {sorted(numbers)}')
print(f'Even numbers: {sorted(even)}')
print(f'Odd numbers: {sorted(odd)}')
