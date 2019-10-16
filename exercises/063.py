"""
Make a program that reads several integer
numbers, and stops only when typed number
is 999. Show in termnial:
1 - Number amount
2 - The sum of all numbers without flag.

Flag is the stopping condition.
"""

count = sum = num = 0
while num != 999:
    sum += num
    count += 1
    num = float(input('Enter a number [999 stops]: '))
else:
    count -= 1
print('The amout of numbers is {}, and its sum is {}.'.format(count,sum))
