"""
Make a program that reads several
numbers, and returns the mean, maximum,
and minimum values.
The program must ask whether user want
to continue.
"""

sum = count = num = 0
more = ''
while more != 'n':
    num = float(input('Enter a number: '))
    sum += num
    if count == 0:
        max = num
        min = num
    elif num > max:
        max = num
    elif num < min:
        min = num
    count += 1
    more = str(input('Continue? [y/n]: ')).strip().lower()[0]
mean = sum / count
print('\nMEAN: {}\nMAX: {}\nMIN: {}'.format(mean, max, min))
