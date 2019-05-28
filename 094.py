"""
Enhance the script 092 so that
it works with several players,
including a detail display
for each player.
"""

team = []
player = {}
goals = []

while True:
    player.clear()
    player['name'] = str(input("Player's name: ")).strip().title()
    matches = int(input('How many played matches: '))
    for match in range(matches):
        goals.append(int(input(f'Goals in {match+1}º match: ')))
    player['goals'] = goals[:]
    player['total'] = sum(goals)
    team.append(player.copy())
    goals.clear()
    while True:
        ans = str(input('Continue [y/n]: ')).strip()[0]
        if ans in "YyNn":
            break
        print('ERROR! Type only "y" or "n".')
    if ans in 'Nn':
        break
print('-'*45)
print(f'cod', end = ' ')
for k in player.keys():
    print(f'{k:<15}', end = ' ')
print('')
print('-'*45)
for c , p in enumerate(team):
    print(f'{c:>3}', end = ' ')
    for d in p.values():
        print(f'{str(d):<15}', end = ' ')
    print('')
print('-'*45)
while ans != 999:
    ans = int(input('Enter player code (999 quit): '))
    if ans < len(team):
        print(f'{team[ans]["name"]} played {len(team[ans]["goals"])} matches.')
        for m , g in enumerate(team[ans]['goals']):
            print(f'    => Match {m+1}: {g} goals')
        print(f'A total of {team[ans]["total"]} goals.')
    elif ans != 999:
        print('ERROR! Try again.')
