"""
Make a program that reads 3 numbers,
and returns which one is bigger/smaller.
"""

n1 = float(input('Enter three numbers:\n'))
n2, n3 = float(input()), float(input())

list = [n1,n2,n3]

print('_'*20)

for k in list:
    if k >= n1 and k >= n2 and k >= n3:
        print('Bigger one: {}'.format(k))
    if k <= n1 and k <= n2 and k <= n3:
        print('Smaller one: {}'.format(k))
