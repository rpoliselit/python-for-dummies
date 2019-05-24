"""
Make a program that reads the name and
two grades of several students, and register
them in a compound list. Show:
1 - Table with name and mean
2 - grades of a single student
"""

from numpy import mean
from time import sleep

group = []
student = []
grades = []

while True:
    student.append(str(input('Name: ')).strip())
    for i in range(2):
        grades.append(float(input(f'Grade {i+1}: ')))
    student.append(grades[:])
    grades.clear()
    group.append(student[:])
    student.clear()
    ans = str(input('Continue? [y/n] ')).strip().lower()
    if 'n' in ans:
        break
print('='*48)
print(f'No. {"NAME":<40}MEAN')
print('-'*48)
for pos , ind in enumerate(group):
    print(f'{pos:2.0f}  {ind[0]:<40}{mean(ind[1]):.1f}')
print('-'*48)

while True:
    ans = int(input('Show grades by [999 quit]: '))
    if ans == 999:
        print('SEE YOU LATER...')
        sleep(0.5)
        print('END!')
        break
    print(f"{group[ans][0]}'s grades are {group[ans][1]}.")
    print('-'*48)
