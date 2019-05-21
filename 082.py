"""
Make a program where the user types
any expression that uses parentheses.
Your application should analyze whether
the parentheses are open and closed in
the correct order.
"""

phrase = str(input('Enter an expression: ')).strip().lower()
count = 0

for k in phrase:
    if k == '(' and count >= 0:
        count += 1
    elif k == ')':
        count -= 1

if count == 0:
    valid = ' '
else:
    valid = ' NOT '
print(f'This is{valid}a valid expression.')
