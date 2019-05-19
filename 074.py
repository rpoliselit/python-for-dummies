"""
Make a program that reads four values
from the keyboard, and stores them in
a tuple. Show:
1 - how many times did the value 9
2 - In which position was the first value entered 3.
3 - What were even numbers?
"""

numbers = (int(input('Enter a number: ')),       \
          int(input('Enter another number: ')),  \
          int(input('Enter more one number: ')), \
          int(input('Enter the last number: ')))

even = False

print(f'The number 9 appears {numbers.count(9)} times.')
if numbers.count(3) != 0:
    print(f'First number 3 is at position {numbers.index(3)}.')
else:
    print(f'There is no number 3.')
print('Even numbers:', end = '')
for n in numbers:
    if n%2 == 0:
        print(f' {n}', end = '')
        even = True
if even == False:
    print(f' null', end = '')
print('.')
