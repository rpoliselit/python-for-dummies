"""
Make a program that the user enters
five numbers, which are saved in a list
already in ascending order.

Show list.

DO NOT use sorted().
"""

numbers = []

for n in range(5):
    while True:
        num = int(input('Enter a integer number: '))
        if num not in numbers:
            break
        else:
            print('Try another number.')
    if len(numbers) == 0 or num > numbers[-1]:
        numbers.append(num)
    else:
        pos = 0
        while True:
            if num < numbers[pos]:
                numbers.insert(pos, num)
                break
            pos += 1


print(f'{numbers}')
