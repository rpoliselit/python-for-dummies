"""
Make a program that has a function
called vote, which one gets as parameter
the birth year of a person. It returns
a textual value: Deined, or optional, or
required.
"""

def vote(birth):
    #here 'birth' is a local variable
    from datetime import datetime
    today = datetime.now().year
    age = today - birth
    if age < 16:
        return (age, 'DO NOT VOTE YET.')
    elif age <18 or age > 65:
        return (age, 'OPTIONAL VOTE.')
    else:
        return (age, 'REQUIRED VOTE!')

print('-'*40)
birth = int(input('Enter your birth year: ')) #here 'birth' is a global variable
print(f'{vote(birth)[0]} years old: {vote(birth)[1]}')
