"""
Create a program that will generate 5 random numbers inside a tuple.
Show:
1-Tuple
2-Highest tuple value
3-Lower tuple value
"""

from random import random

numbers = (random(),random(),random(),random(),random())

print(f"{' TUPLE ':*^40}")
for n in numbers:
    print(f'{n:.2f}')
print(f"""\nMax: {max(numbers):.2f}
Min: {min(numbers):.2f}
""")
