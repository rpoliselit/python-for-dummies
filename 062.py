"""
Make a program that show the n first
elements of Fibonacci.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
"""

print('{:=^40}'.format(' FIBONACCI '))

num = int(input('\nHow many Fibonacci elements do you want? '))
n = count = 0
while count != num:
    print('{}'.format(n), end = ' ')
    count += 1
    if n == 0:
        n += 1
        prev = 0
    else:
        n = n + prev
        prev = n - prev
print('\n')
