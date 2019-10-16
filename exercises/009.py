"""
Make a script that reads any integer number,
and returns its mathematical table.
"""

number = int(input('Type a integer number: \n'))

print('-'*15)
for i in range(11):
    print('{} x {:>2} = {:2}'.format(number , i , number * i))
print('-'*15)
