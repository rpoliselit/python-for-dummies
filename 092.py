"""
Create a program that manages the status
of a soccer player. The program reads the
name of the player, how many matches he has
played, number of goals in each match. All
this must be kept in a dictionary including
all the goals made during the championship.
"""

player = {}
goals = []

player['name'] = str(input("Player's name: ")).strip().title()
matches = int(input('How many played matches: '))
for match in range(matches):
    goals.append(int(input(f'Goals in {match+1}º match: ')))
player['goals'] = goals[:]
player['total'] = sum(goals)
print('-'*30)
for k , v in player.items():
    print(f'{k} = {v}')
print('-'*30)
print(f'{player["name"]} played {matches} matches.')
for m , g in enumerate(player['goals']):
    print(f'    => Match {m+1}: {g} goals')
print(f'A total of {player["total"]} goals.')
