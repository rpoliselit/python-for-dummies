"""
Make a program that reads the year of birth,
and show in console:
-Too young to be kidnapp by army.
-It is time to military draft.
-You have finished the military service.
"""

from datetime import date

birth = int(input('Enter your year of birth:\n'))
sex = input('Type\n[ m ] male\n[ f ] female\nSex: ').strip()
year = date.today().year
age = year - birth

if age < 18 and sex == 'm':
    print('Too young to be kidnapped by army.')
    print('Only school is eligible to kidnapp you so far!')
    print('{} years left to military draft,'.format(18 - age), end = '')
    print(' i.e. {}.'.format(birth + 18))
elif age == 18 and sex == 'm':
    print('Military draft time!')
elif age > 18 and sex == 'm':
    print("Military service is done so far!")
    print("It's been {} years ago,".format(age - 18), end = '')
    print(' i.e. {}.'.format(birth + 18))
elif sex == 'f':
    print('Your are free!')
else:
    print('Invalid sex information.')
