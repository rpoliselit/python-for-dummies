"""
Make a program that reads student's name, mean grade,
and status. Register it in a dictionary.
Show content.
"""

student = {}

student['name'] = str(input("Student's name: ")).strip().title()
student['grade'] = float(input("Student's grade: "))
if student['grade'] >= 7:
    student['status'] = 'APPROVED'
elif student['grade'] >= 5:
    student['status'] = 'FINAL EXAM'
else:
    student['status'] = 'DISAPPROVED'

# print(student)
# print(student.values())
# print(student.keys())
# print(student.items())
print('-'*30)
for k , v in student.items():
    print(f'{k.title()} = {v}')
