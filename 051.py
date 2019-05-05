"""
Make a program that reads a integer number,
and returns whether it is a prime number or
not.

The first 25 prime numbers:
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
89, 97.
"""
print('{:-^40}'.format(" PRIME ANALYSIS "))
num = int(input('Enter a number: '))

print('This number is divisible by:')

sum = 0
for k in range(1, num+1):
    if num % k == 0:
        sum += 1
        print('\033[1;36m' , end = '')
    else:
        print('\033[m' , end = '')
    print('{}'.format(k), end = ' ')


if sum == 2:
    print('\n\033[mThus {} is a PRIME number!'.format(num))
else:
    print('\n\033[mThus {} is NOT a prime number!'.format(num))
