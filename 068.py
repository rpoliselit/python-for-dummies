"""
Create a program that reads the
age, and gender of several people.
To each registered person the program
should ask if the user wants to continue.
In the end show:
[1] Number of people over 21
[2] Number of registered men
[3] Number of women under 21
"""
print(f"""
{'='*30}
{'REGISTER':^30}
{'='*30}""")

major = underage = men = 0
while True:
    age = int(input('Age: '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Sex [m/f]: ')).strip().upper()[0]
    if age >= 21:
        major += 1
    elif sex == 'F':
        underage += 1
    if sex == 'M':
        men += 1
    answer = ' '
    while answer not in 'YN':
        answer = str(input('Continue? [y/n] ')).strip().upper()[0]
    if answer == 'N':
        break

print(f"""
Number of legal age: {major}
          men: {men}
          underage women: {underage}""")
