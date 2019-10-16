"""
Make a program that show every even number
in a interval from 0 to 50.
"""

#this solution has less iterations
for k in range(0,51,2):
    print('{} '.format(k), end = '')
print('\nEND')

#way by using if
#for j in range(0,51):
#    if j % 2 == 0:
#        print('{} '.format(j), end = '')
#print('\nEND')
