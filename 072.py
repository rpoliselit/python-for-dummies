"""
Make a tuple filled with the 20 best
skateboarder in all time following
the rank.
Make a program to show:
1 - Top 5 skaters
2 - The last 4 skaters
3 - List in alphabetical order
4 - What is the Dawon Song's position?

https://www.ranker.com/list/best-skateboarders-of-all-time/ranker-sports
"""

skaters = ('Rodney Mullen', 'Tony Hawk', 'Eric Koston', 'Nyjan Huston',     \
         'Bob Burnquist', 'Andrew Reynolds', 'Danny Way', 'Paul Rodriguez', \
         'Dawon Song', 'Steve Caballero', 'Mark Gonzales', 'Chris Cole',    \
         'Tony Alva', 'Chris Joslin', 'Luan Oliveira', 'Bucky Lasek',       \
         'Christina Hosoi', 'Chad Muska', 'Ryan Sheckler', 'Geoff Rowley')

# print(f"""Top 5: {skaters[:5]}
# Last 4: {skaters[:-5:-1]}
# Alphabetical order: {sorted(skaters)}
# Dawon song is {skaters.index('Dawon Song')+1}th.
# """)


print(f"{' TOP FIVE ':*^40}")
for pos, skater in enumerate(skaters[0:5]):
    print(f'{pos+1}º {skater}')
input('\nPress any button')
print(f"{'LAST ONES':-^40}")
for pos, skater in enumerate(skaters[-4:]):
    print(f"{pos+17}º {skater}")
input('\nPress any button')
print(f"{'ALPHABETICAL ORDER':=^40}")
for skater in sorted(skaters):
    print(f'{skater}')
input('\nPress any button')
print(f"{'-='*20}")
print(f"Dawon Song is {skaters.index('Dawon Song')+1}th.")
