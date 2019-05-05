"""
Make a program that reads the mass of 5 people,
and returns which is the largest and smallest
mass among them.
"""

"""
num = int(input('Enter the number of people: '))
mass = []

for k in range(0,num):
    mass.append(float(input('{}º mass (Kg): '.format(k+1))))

print('Bigger mass: {:.1f}\nSmaller mass: {:.1f}'.format(max(mass),min(mass)))
"""

#alternative to functions max and min
num = int(input('Enter the number of people: '))
bigger = 0
smaller = 0

for k in range(0,num):
    mass = float(input('{}º mass (Kg): '.format(k+1)))
    if k == 0:
        bigger = mass
        smaller = mass
    elif mass > bigger:
        bigger = mass
    elif mass < smaller:
        smaller = mass
        
print('Bigger mass: {:.1f}\nSmaller mass: {:.1f}'.format(bigger,smaller))
