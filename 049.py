"""
Make a program that reads six integer numbers
and returns the sum of those that are odd.
"""
sum = 0
for i in range(0,6):
    num = int(input('Enter a integer number: '))
    if num % 2 != 0:
        sum += num
print('The sum of odd numbers is {}.'.format(sum))
