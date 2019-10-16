"""
Make a program that has a function
called record, which one gets two
parameters:
1 - Player's name.
2 - Number of goals.

The function must work even with no
informed parameters.
"""

def record(name = 'unknown', goals = 0):
     print(f'The soccer player {name} scored {goals} goals.')


#main program
print('-'*40)
player = str(input("Player' s name: ")).strip().title()
score = str(input("Its score: ")).strip()
if score.isnumeric():
    score = int(score)
else:
    score = 0
if player == '':
    record(goals = score)
else:
    record(player, score)
