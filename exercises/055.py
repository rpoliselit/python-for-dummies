"""
Make a program that reads the name,
age, and gender of four people, and
returns:
- The mean age of the group.
- The name of the older man.
- The number of women under the age of 21.
"""


"""
from numpy import mean

#dname = {}
name = []
age = []
gender = []
olderman = []
underage = 0

for k in range(0,4):
    print('{}º PERSON'.format(k+1))
    name.append(str(input('Name: ')).strip().upper())
    age.append(int(input('Age: ')))
    gender.append(str(input('Gender: ')).strip().upper())
#    dname[name] = k
    if gender[k].find('M') == 0:
        olderman.append(age[k])
    elif age[k] < 21:
        olderman.append(0)
        underage += 1
    else:
        olderman.append(0)

print("="*40)
print('The mean age is {:.0f} years old.'.format(mean(age)))
for k in range(0,4):
    if olderman[k] == max(olderman):
        print('The name of olderman is {}.'.format(name[k]))
print('Females under 21 years old: {}.'.format(underage))
"""


#simplest alternative

sum = 0
num = 0
olderman = ''
underageF = 0
old = 0

for k in range(0,4):
    print('{}º PERSON'.format(k+1))
    name = str(input('Name: ')).strip()
    age = int(input('Age: '))
    gender = str(input('Gender [m]ale or [f]emale: ')).strip()
    sum += age
    num += 1
    if gender in 'Ff' and age < 21:
        underageF += 1
    elif gender in 'Mm' and age > old:
        old = age
        olderman = name

mean = sum / num

print("="*40)

print('The mean age is {:.0f} years old.'.format(mean))
if olderman != '':
    print('The name of olderman is {}.'.format(olderman.title()))
print('Under age females: {}.'.format(underageF))
