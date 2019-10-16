"""
Make a program that reads several values
and registers in a list. Show:
[1] amount of typed numbers
[2] list in descending order
[3] is number 5 in list?
"""

numbers = []

while True:
    num = input('Enter any number [empty stops]: ').strip().lower()
    if num.isalnum() == False:
        break
    elif num.isnumeric() == False:
        print('Try again. This is not a number.')
    elif float(num) not in numbers:
        numbers.append(float(num))
print('='*30)
print(f'You typed {len(numbers)} valid numbers.')
print('Descending order: ', end = '')
numbers.sort(reverse=True)
for n in numbers:
    print(f'{n}', end = '... ')
exist = ' ' if 5 in numbers else ' NOT '
print(f'\nNumber 5 was{exist}typed.')
