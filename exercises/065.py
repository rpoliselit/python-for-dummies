"""
Make a program that reads several integer
numbers, and stops only when typed number
is 999. Show in termnial:
1 - Number amount
2 - The sum of all numbers without flag.

Flag is the stopping condition.
"""

count = sum = 0
while True:
    num = float(input('Enter a number [999 stops]: '))
    if num == 999:
        break
    sum += num
    count += 1
print(f'The amout of numbers is {count}, and its sum is {sum:.2f}.')
