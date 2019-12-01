"""
2 - The underscore is used to ignore a given value.
You can just assign the values to underscore.
"""

x, _ , z = (1,2,3)

print(x, z)

a, *_ , b = (1,2,3,4,5)

print(a,b)

for _ in range(10):
    print('hello world')

