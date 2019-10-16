"""
Make a code that reads the score of a student,
and calculate this mean. The console must show
this mean and the following messages:
-approved,
-failed,
-eligible to final exam.
"""

import numpy as np

num = int(input('How many exams? '))
tests = []

for i in range(num):
    tests.append(float(input('Score of {}º exam: '.format(i+1))))

mean = np.mean(tests)

print('The mean score is {:.1f}.'.format(mean))

if mean < 5:
    print('Failed!')
elif 5 <= mean < 7:
    print('Student eligible to finel exam!')
elif mean >= 7:
    print('Congratulations! Student approved.')
