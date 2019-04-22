"""
Make a code that reads the score of a student, and calculate this mean.
"""

tests = []
number = int(input('What is the number of tests? '))
sum = 0

for i in range(number):
    tests.append(float(input('Score of test {}: '.format(i+1))))
    sum = sum + tests[i]

mean = sum / len(tests)

print('The mean score is: {:.2f}'.format(mean))
